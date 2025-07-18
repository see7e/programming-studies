---
title: Database Migration in PostgreSQL
tags:
  - studies
  - programming
  - database
  - postgresql
  - migration
  - error-handling
  - filename-conventions
  - pgadmin
  - deep-dive
use: Documentation
languages: SQL
dependences: PostgreSQL, pgAdmin
---

<details> <summary>Table of Contents 🔖</summary>

- [Database Migration in PostgreSQL](#database-migration-in-postgresql)
	- [PostgreSQL Table Migration: Comprehensive Strategies](#postgresql-table-migration-comprehensive-strategies)
		- [1. Using pgAdmin for Table Migration](#1-using-pgadmin-for-table-migration)
		- [2. Advanced `COPY` Command Techniques](#2-advanced-copy-command-techniques)
		- [3. Cross-Database Migration Strategies](#3-cross-database-migration-strategies)
	- [Handling Duplicate Key Violations: Advanced Conflict Resolution](#handling-duplicate-key-violations-advanced-conflict-resolution)
		- [Understanding the Duplicate Key Error](#understanding-the-duplicate-key-error)
		- [`INSERT ON CONFLICT`: The PostgreSQL Upsert Solution](#insert-on-conflict-the-postgresql-upsert-solution)
		- [Performance Considerations for Conflict Resolution](#performance-considerations-for-conflict-resolution)
		- [Alternative Approaches for Duplicate Handling](#alternative-approaches-for-duplicate-handling)
	- [Filename conventions impacts](#filename-conventions-impacts)
		- [Understanding Windows 8.3 Filename Convention](#understanding-windows-83-filename-convention)
			- [Historical Context and Technical Background](#historical-context-and-technical-background)
			- [8.3 Filename Generation Algorithm](#83-filename-generation-algorithm)
			- [Modern Implications and System Behavior](#modern-implications-and-system-behavior)
			- [Disabling 8.3 Filename Generation](#disabling-83-filename-generation)
			- [PostgreSQL and Filesystem Compatibility](#postgresql-and-filesystem-compatibility)
	- [Best Practices for Database Migration Projects](#best-practices-for-database-migration-projects)
		- [Pre-Migration Assessment](#pre-migration-assessment)
		- [Migration Strategy Selection](#migration-strategy-selection)
		- [Data Integrity Verification](#data-integrity-verification)
	- [Error Handling and Recovery Strategies](#error-handling-and-recovery-strategies)
		- [Comprehensive Error Classification](#comprehensive-error-classification)
		- [Automated Error Recovery](#automated-error-recovery)
		- [Rollback and Recovery Planning](#rollback-and-recovery-planning)
	- [Advanced Migration Tools and Techniques](#advanced-migration-tools-and-techniques)
		- [Third-Party Migration Solutions](#third-party-migration-solutions)
		- [Custom Migration Scripts](#custom-migration-scripts)
	- [Monitoring and Performance Optimization](#monitoring-and-performance-optimization)
		- [Migration Performance Metrics](#migration-performance-metrics)
		- [Optimization Strategies](#optimization-strategies)
- [References](#references)

</details>

---
# Database Migration in PostgreSQL
> A Deep Dive into Table Copying, Error Handling, and Filename Conventions

Sometimes we face a scenario common in database administration: migrating tables between PostgreSQL databases while handling potential conflicts and system-specific challenges. This comprehensive exploration delves into the *nuances of PGSQL table migration*, advanced *conflict resolution strategies*, and the technical considerations that arise when working across different operating systems.

## PostgreSQL Table Migration: Comprehensive Strategies

### 1. Using [pgAdmin](https://www.pgadmin.org/) for Table Migration
PostgreSQL's pgAdmin provides several robust methods for table migration[^1][^2]. The most straightforward approach involves using the GUI to execute the backup and restore functionalities:
- **Backup Process:**
	- Right-click on the source table in pgAdmin's tree control
	- Select "Backup" from the context menu
	- Configure the backup format (Custom, Tar, or Plain)
	- Specify the destination file location
- **Restore Process:**
	- Connect to the target database
	- Right-click and select "Restore"
	- Navigate to the backup file
	- Configure restore options as needed

The Custom format is particularly recommended for medium to large databases as it **supports compression and selective restoration**[^3]. This format *provides flexibility in choosing which database objects to restore from the backup file*.

### 2. Advanced `COPY` Command Techniques
Moving a little bit from the GUI, we have the `COPY` command which offers powerful capabilities for data transfer[^4][^5]. Beyond basic usage, advanced techniques include:

**Direct Server-to-Server Transfer:**

```sql
COPY (SELECT * FROM source_table) 
TO PROGRAM 'ssh user@target.server.com "psql -d target_db -c \"COPY target_table FROM STDIN\""'
```

This approach uses SSH to pipe data directly between servers, eliminating the need for intermediate files[^5].

**Compressed Transfer:**

```sql
COPY (SELECT * FROM source_table) 
TO PROGRAM 'gzip -c > /tmp/compressed_data.gz'
```

Data can be compressed on-the-fly during export, reducing storage requirements and transfer times[^5].

### 3. Cross-Database Migration Strategies
When migrating between different PostgreSQL instances, several strategies ensure data integrity and minimize downtime[^6][^7]:

**Dump and Restore Method:**
The most straightforward approach for most migrations, involving:
1. Creating a full backup using `pg_dump`
2. Transferring the backup file to the target server
3. Restoring using `pg_restore`

**Logical Replication:**
For minimal downtime scenarios, logical replication allows continuous synchronization between source and target databases during migration[^8].

**[Foreign Data Wrappers (FDW)](https://wiki.postgresql.org/wiki/Foreign_data_wrappers):**
Enable direct queries between PostgreSQL instances, facilitating gradual migration strategies[^9].

## Handling Duplicate Key Violations: Advanced Conflict Resolution

### Understanding the Duplicate Key Error
The `duplicate key value violates unique constraint` error *occurs when attempting to insert a record that violates a unique constraint*[^10][^11]. This is particularly common during data imports from CSV files or when merging datasets.

### `INSERT ON CONFLICT`: The PostgreSQL Upsert Solution
PostgreSQL's `INSERT ... ON CONFLICT` statement provides elegant solutions for handling duplicate data[^12][^13][^14]:

**Basic Syntax:**

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...)
ON CONFLICT (unique_constraint) DO UPDATE SET
  column1 = EXCLUDED.column1,
  column2 = EXCLUDED.column2;
```

**Advanced Implementation for CSV Import:**

```sql
-- Create temporary table for staging
CREATE TEMP TABLE temp_users AS
SELECT * FROM public.app_users WHERE FALSE;

-- Import CSV data to temporary table
\copy temp_users FROM 'data.csv' DELIMITER ',' CSV HEADER;

-- Perform upsert operation
INSERT INTO public.app_users 
SELECT * FROM temp_userldap
ON CONFLICT (id) DO UPDATE SET
  -- ... additional columns
  password = EXCLUDED.password,
  last_login = EXCLUDED.last_login;

-- Cleanup
DROP TABLE temp_userldap;
```

### Performance Considerations for Conflict Resolution
The choice between different conflict resolution strategies has significant performance implications[^11]:

| Approach                            | Dead Tuples | Transaction ID Usage | Autovacuum Impact |
| :---------------------------------- | :---------- | :------------------- | :---------------- |
| Regular `INSERT` (with error)       | Yes         | Yes                  | High              |
| `INSERT ON CONFLICT ... DO NOTHING` | No          | No                   | Minimal           |
| `INSERT ON CONFLICT ... DO UPDATE`  | Minimal     | Minimal              | Low               |

### Alternative Approaches for Duplicate Handling
**Temporary Table Strategy:**
When `INSERT ON CONFLICT` isn't suitable, the temporary table approach provides robust duplicate handling[^15], similarly to the CSV example above:
1. Create a temporary table with the same structure
2. Import all data into the temporary table
3. Use selective insertion to avoid duplicates:
```sql
INSERT INTO main_table 
SELECT DISTINCT * FROM temp_table t1 
WHERE NOT EXISTS (
  SELECT 1 FROM main_table t2 
  WHERE t1.unique_column = t2.unique_column
);
```

**Pre-processing with Unix Tools:**
For environments supporting Unix utilities, data deduplication can occur before database import[^16]:

```bash
# Remove duplicates from CSV
sort -u input.csv > deduplicated.csv

# Compare with existing data
cat existing_export.csv new_data.csv | sort | uniq -d > duplicates.csv
cat new_data.csv duplicates.csv | sort | uniq -u > unique_new_data.csv
```

> [!TIP]
> Is also possible to use `diff` to compare both files. There's plenty of options.

## Filename conventions impacts

### Understanding Windows 8.3 Filename Convention

#### Historical Context and Technical Background
The appearance of `APP_LO~1.CSV` comes from the legacy *DOS 8.3 filename convention*[^17][^18]. This naming system, originally designed for MS-DOS compatibility, limits filenames to eight characters plus a three-character extension.

#### 8.3 Filename Generation Algorithm
When a long filename exceeds the 8-character limit, Windows automatically generates a short name using the following algorithm[^19][^20]:
1. **Truncation**: Take the first 6 characters of the filename
2. **Suffix Addition**: Append `~1` (or `~2`, `~3`, etc., for subsequent conflicts)
3. **Extension Preservation**: Maintain the original file extension
4. **Case Conversion**: Convert to uppercase for consistency

#### Modern Implications and System Behavior
Despite being a legacy feature, 8.3 naming continues to impact modern systems[^21][^19]:
**Security Considerations:**
- Short names can *expose file structures* that should remain hidden[^17][^22]
- Web servers may *inadvertently serve files via their short names*
- *Potential information disclosure vulnerabilities*

**Performance Impact:**
- 8.3 name generation *adds overhead* to file operations[^19]
- Can cause *synchronization issues* in distributed systems
- May *lead to naming conflicts* in automated processes

#### Disabling 8.3 Filename Generation
For modern systems, disabling 8.3 filename generation *is recommended*[^19][^22], I would say required, but it all comes down to your current case:

```powershell
# Windows Server 2012 and later
fsutil.exe 8dot3name set C: 1

# Windows Server 2008 and earlier
fsutil.exe behavior set disable8dot3 1
```

**Benefits of Disabling:**
- Improved security posture
- Reduced file system overhead
- Elimination of naming conflicts
- Cleaner system behavior

#### PostgreSQL and Filesystem Compatibility
PGSQL interaction with different filesystems reveals important considerations[^21]:
- **NTFS Requirements:**
	- *PostgreSQL requires NTFS* for production deployments
	- FAT32 filesystems are *explicitly not supported*
	- Security features *depend on NTFS access controls*
	- Tablespace functionality *requires NTFS reparse points*
- **Cross-Platform Considerations:**
	- *Filename encoding differences* between systems
	- *Path length limitations* (260 characters on Windows)[^23]
	- *Case sensitivity* variations
	- *Special character* handling

## Best Practices for Database Migration Projects

### Pre-Migration Assessment
Before initiating any migration project, conduct a comprehensive assessment[^6][^7]:

**Database Version Compatibility:**

```sql
SELECT version();
SHOW server_version;
```

**Extension Inventory:**

```sql
SELECT * FROM pg_extension;
```

**Schema Analysis:**
- Identify custom data types
- Document stored procedures and functions
- Catalog constraints and indexes
- Review security settings and permissions

### Migration Strategy Selection
Choose the appropriate migration strategy based on specific requirements:
- **Full Migration (Big Bang Approach):**
	- Suitable for planned maintenance windows
	- Complete system cutover
	- Minimal complexity but higher downtime
- **Phased Migration (Trickle Approach):**
	- Gradual data transfer
	- Reduced downtime risk
	- Higher complexity but better for critical systems
- **Hybrid Approaches:**
	- Combination of replication and batch transfers
	- Custom solutions for specific requirements
	- Balance between complexity and risk mitigation

### Data Integrity Verification
Implement comprehensive verification procedures, a good example is using a `checksum` hash function to compare the data chunks and verify the symmetry.

```sql
-- Row count verification
SELECT COUNT(*) FROM source_table;
SELECT COUNT(*) FROM target_table;

-- Checksum comparison
SELECT MD5(string_agg(column_name::text, '' ORDER BY primary_key)) 
FROM source_table;

-- Sample data verification
SELECT * FROM source_table 
ORDER BY primary_key 
LIMIT 10;
```

## Error Handling and Recovery Strategies

### Comprehensive Error Classification
Database migration errors fall into several categories[^10][^11]:
- **Constraint Violations:**
	- Primary key duplicates
	- Foreign key conflicts
	- Check constraint failures
	- Unique constraint violations
- **Data Type Mismatches:**
	- Character encoding issues
	- Numeric precision problems
	- Date/time format inconsistencies
	- Boolean representation differences
- **System-Level Issues:**
	- Insufficient disk space
	- Network connectivity problems
	- Permission and authentication failures
	- Resource limitations

### Automated Error Recovery
Implement robust error handling mechanism, here's a simple function example:

```sql
DO $$
BEGIN
    -- Attempt main operation
    INSERT INTO target_table SELECT * FROM source_table;
EXCEPTION 
    WHEN unique_violation THEN
        -- Handle duplicate key errors
        INSERT INTO target_table 
        SELECT * FROM source_table
        ON CONFLICT (id) DO UPDATE SET
          updated_at = EXCLUDED.updated_at;
    
    WHEN foreign_key_violation THEN
        -- Handle referential integrity issues
        RAISE NOTICE 'Foreign key constraint violation detected';
        -- Implement custom resolution logic
        
    WHEN OTHERS THEN
        -- General error handling
        RAISE NOTICE 'Unexpected error: %', SQLERRM;
        -- Log error details for investigation
END;
$$;
```

### Rollback and Recovery Planning
Design comprehensive rollback strategies:
- **Point-in-Time Recovery:**
	- Maintain transaction logs throughout migration
	- Implement checkpoint mechanisms
	- Enable rapid rollback to known good states
- **Backup Verification:**
	- Test backup integrity before migration
	- Validate restore procedures
	- Maintain multiple backup copies
- **Monitoring and Alerting:**
	- Real-time migration progress tracking
	- Automated error detection and notification
	- Performance metrics collection

## Advanced Migration Tools and Techniques

### Third-Party Migration Solutions
Several specialized tools enhance PostgreSQL migration capabilities[^24]:
- **Ispirer Toolkit:**
	- Automatic schema conversion
	- Data type mapping
	- Stored procedure translation
	- Multi-database support
- **pgloader:**
	- High-performance data loading
	- Support for multiple source formats
	- Built-in transformation capabilities
	- Error handling and reporting
- **DBConvert Solutions:**
	- Real-time change data capture
	- Cloud integration capabilities
	- Cross-platform synchronization
	- Enterprise-scale processing

### Custom Migration Scripts
Develop tailored solutions for specific requirements:

```python
import psycopg2
import csv
import logging

class PostgreSQLMigrator:
    def __init__(self, source_conn, target_conn):
        self.source = source_conn
        self.target = target_conn
        self.logger = logging.getLogger(__name__)
    
    def migrate_table_with_upsert(self, table_name, primary_key):
        """Migrate table data with conflict resolution"""
        try:
            # Extract data from source
            source_cursor = self.source.cursor()
            source_cursor.execute(f"SELECT * FROM {table_name}")
            
            # Prepare upsert statement
            columns = [desc[^0] for desc in source_cursor.description]
            upsert_sql = self._build_upsert_query(table_name, columns, primary_key)
            
            # Execute batch upsert
            target_cursor = self.target.cursor()
            for batch in self._batch_generator(source_cursor, 1000):
                target_cursor.executemany(upsert_sql, batch)
                self.target.commit()
                
        except Exception as e:
            self.logger.error(f"Migration failed for {table_name}: {e}")
            self.target.rollback()
            raise
    
    def _build_upsert_query(self, table_name, columns, primary_key):
        """Generate optimized upsert SQL"""
        column_list = ', '.join(columns)
        value_placeholders = ', '.join(['%s'] * len(columns))
        update_set = ', '.join([f"{col} = EXCLUDED.{col}" 
                               for col in columns if col != primary_key])
        
        return f"""
        INSERT INTO {table_name} ({column_list})
        VALUES ({value_placeholders})
        ON CONFLICT ({primary_key}) DO UPDATE SET {update_set}
        """
```

## Monitoring and Performance Optimization

### Migration Performance Metrics
Track key performance indicators throughout the migration process:
- **Throughput Metrics:**
	- Rows transferred per second
	- Data volume per time unit
	- Transaction commit rates
	- Error occurrence frequency
- **Resource Utilization:**
	- CPU consumption patterns
	- Memory usage statistics
	- Disk I/O performance
	- Network bandwidth utilization
- **System Health Indicators:**
	- Connection pool status
	- Lock contention levels
	- Autovacuum activity
	- Log file growth rates

### Optimization Strategies
**Parallel Processing:**
```sql
-- Configure parallel workers for large operations
SET max_parallel_workers_per_gather = 4;
SET parallel_tuple_cost = 0.1;
SET parallel_setup_cost = 1000;
```

**Batch Size Optimization:**
- Balance between memory usage and transaction overhead
- Consider target system capabilities
- Monitor performance metrics and adjust accordingly

**Index Management:**
- Drop non-essential indexes during bulk operations
- Rebuild indexes after data migration
- Consider partial indexes for large tables

---

The evolution from simple table copying to comprehensive database migration strategies *reflects the increasing complexity of modern data management requirements*. The interaction demonstrates how seemingly straightforward operations—copying tables between databases—can reveal **deeper technical challenges** ranging from *conflict resolution* to *cross-platform compatibility issues*.

**Key Takeaways:**
1. **PostgreSQL provides robust tools** for table migration through pgAdmin, COPY commands, and programmatic approaches, each suited to different scenarios and requirements[^1][^4][^5].
2. **Conflict resolution strategies** like `INSERT ON CONFLICT...` offer elegant solutions to duplicate key problems, with significant performance advantages over traditional error-handling approaches[^12][^11][^13].
3. **Cross-platform considerations** such as filename conventions can impact migration success, requiring awareness of legacy systems and their modern implications[^17][^21][^19].
4. **Comprehensive planning** including pre-migration assessment, strategy selection, and error handling significantly improves migration success rates[^6][^7].

**The technical depth required for successful database migration projects extends far beyond basic SQL operations**. Understanding the interplay between database features, operating system behaviors, and application requirements ensures robust, reliable data management solutions that can adapt to evolving business needs.

Whether dealing with legacy 8.3 filename conventions or implementing sophisticated *UPSERT* (UPDATE+INSERT) strategies, the principles of thorough preparation, comprehensive testing, and robust error handling remain fundamental to successful database migration projects. As organizations continue to modernize their infrastructure, these considerations become increasingly critical for maintaining data integrity and system reliability.


# References
[^1]: https://hostman.com/tutorials/how-to-migrate-a-postgresql-database/
[^2]: https://www.c-sharpcorner.com/article/how-to-take-backup-and-restore-a-table-in-postgresql/
[^3]: https://www.pgadmin.org/docs/pgadmin4/development/backup_dialog.html
[^4]: https://www.postgresql.org/docs/current/sql-copy.html
[^5]: https://www.cybertec-postgresql.com/en/copy-in-postgresql-moving-data-between-servers/
[^6]: https://www.heroku.com/blog/planning-your-postgresql-migration/
[^7]: https://www.nucamp.co/blog/coding-bootcamp-back-end-with-python-and-sql-data-migration-strategies-in-postgresql
[^8]: https://docs.digitalocean.com/products/databases/postgresql/how-to/migrate/
[^9]: https://www.linkedin.com/advice/0/what-most-effective-postgresql-data-migration-sut6c
[^10]: https://dev.to/emmanuelomale/how-to-fix-duplicate-key-value-violates-unique-constraint-in-postgresql-a-developers-survival-1oca
[^11]: https://aws.amazon.com/blogs/database/hidden-dangers-of-duplicate-key-violations-in-postgresql-and-how-to-avoid-them/
[^12]: https://www.dbvis.com/thetable/postgresql-upsert-insert-on-conflict-guide/
[^13]: https://neon.com/postgresql/postgresql-tutorial/postgresql-upsert
[^14]: https://www.prisma.io/dataguide/postgresql/inserting-and-modifying-data/insert-on-conflict
[^15]: https://textquery.app/2022/07/21/import-csv-without-duplicates-postgres/
[^16]: https://www.postgrespro.com/list/thread-id/1550336
[^17]: https://www.acunetix.com/blog/articles/windows-short-8-3-filenames-web-security-problem/
[^18]: https://learn.microsoft.com/en-us/answers/questions/524512/behavior-when-converting-longname-thats-only-space
[^19]: https://kb.peersoftware.com/kb/8-3-short-file-names-cause-out-of-sync-file-folder
[^20]: https://www.eevblog.com/forum/programming/converting-long-filenames-to-8-3/
[^21]: https://wiki.postgresql.org/wiki/Running_\&_Installing_PostgreSQL_On_Native_Windows
[^22]: https://www.invicti.com/web-vulnerability-scanner/vulnerabilities/windows-short-filename/
[^23]: https://stackoverflow.com/questions/1880321/why-does-the-260-character-path-length-limit-exist-in-windows
[^24]: https://wiki.postgresql.org/wiki/Converting_from_other_Databases_to_PostgreSQL
[^25]: https://techcommunity.microsoft.com/blog/adforpostgresql/moving-data-with-postgresql-copy-and-copy-commands/1561266
[^26]: https://stackoverflow.com/questions/14826862/how-to-restore-a-single-table-from-a-sql-postgresql-backup
[^27]: https://www.youtube.com/watch?v=OftuG2VaT0I
[^28]: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Procedural.Importing.Copy.html
[^29]: https://www.postgresql.org/docs/9.0/migration.html
[^30]: https://www.pgadmin.org/docs/pgadmin4/development/restore_dialog.html
[^31]: https://www.postgresql.org/docs/current/libpq-copy.html
[^32]: https://support.dataclaritycorp.com/hc/en-us/articles/360050455532-How-to-back-up-and-restore-a-DB-table-in-pgAdmin
[^33]: https://neon.com/postgresql/postgresql-administration/postgresql-copy-database
[^34]: https://dba.stackexchange.com/questions/161857/how-to-backup-restore-in-postgresql-pgadmin-4
[^35]: https://stackoverflow.com/questions/40364920/importing-csv-file-into-postgresql-but-have-duplicates
[^36]: https://geshan.com.np/blog/2024/12/postgres-insert-on-conflict-update/
[^37]: https://www.reddit.com/r/PostgreSQL/comments/1gol6al/duplicate_key_error/
[^38]: https://github.com/go-gorm/gorm/issues/4135
[^39]: https://www.postgresql.org/message-id/44775536.q0neeYZfuk@linux-wzza.aruprakshit
[^40]: https://codedamn.com/news/sql/on-conflict-upsert-in-postgresql
[^41]: https://www.postgresql.org/message-id/B056671652AA4D418763981054BCEAB40929EB@PA-MBX04.na.tibco.com
[^42]: https://postgrespro.com/list/thread-id/1515713
[^43]: https://www.alibabacloud.com/help/en/analyticdb/analyticdb-for-postgresql/developer-reference/use-insert-on-conflict-to-overwrite-data
[^44]: https://stackoverflow.com/questions/56324074/can-i-change-the-error-message-thrown-for-duplicate-key-in-postgresql
[^45]: https://github.com/dbeaver/dbeaver/issues/34852
[^46]: https://stackoverflow.com/questions/36359440/postgresql-insert-on-conflict-update-upsert-use-all-excluded-values
[^47]: https://github.com/brianc/node-postgres/issues/1602
[^48]: https://stackoverflow.com/questions/66887694/in-the-file-path-what-does-mean
[^49]: https://www.postgresql.org/docs/current/storage-file-layout.html
[^50]: https://superuser.com/questions/211355/what-does-the-mean-in-a-file-path
[^51]: https://docs.jade.fyi/postgres/postgres-16.html
[^52]: https://stackoverflow.com/questions/52569369/get-dos-8-3-filename
[^53]: https://learn.microsoft.com/en-us/dotnet/standard/io/file-path-formats
[^54]: https://www.reddit.com/r/programming/comments/12u9giq/the_weird_world_of_windows_file_paths/
[^55]: https://www.pgadmin.org/docs/pgadmin4/development/release_notes_8_3.html
[^56]: https://stackoverflow.com/questions/10227144/convert-long-filename-to-short-filename-8-3-using-cmd-exe/10227629
[^57]: https://www.lenovo.com/ca/en/glossary/path/
[^58]: https://pgsql.interfaces.pgadmin.support.narkive.com/RWBY0alc/pgadmin-support-malfunction-in-dropping-database-with-pgadmin
[^59]: https://www.idera.com/blogs/converting-file-paths-to-8-3-part-1/
[^60]: https://isgovern.com/blog/how-to-fix-the-windows-unquoted-service-path-vulnerability/
