---
title: PostgreSQL LDAP Authentication
tags:
  - studies
  - programming
  - database
  - authentication
  - security
  - ldap
  - active-directory
use: Documentation
languages: SQL, shell
dependences: PostgreSQL, LDAP
---

<details> <summary>Table of Contents 🔖</summary>

- [PostgreSQL LDAP Authentication Configuration Guide](#postgresql-ldap-authentication-configuration-guide)
  - [Prerequisites](#prerequisites)
  - [Basic LDAP Configuration](#basic-ldap-configuration)
    - [Standard LDAP Configuration](#standard-ldap-configuration)
    - [Essential LDAP Parameters](#essential-ldap-parameters)
    - [Simple LDAP Example](#simple-ldap-example)
  - [Advanced Configuration Examples](#advanced-configuration-examples)
    - [Active Directory Configuration](#active-directory-configuration)
    - [Secure LDAP (LDAPS) Configuration](#secure-ldap-ldaps-configuration)
    - [Multiple LDAP Servers (Failover)](#multiple-ldap-servers-failover)
    - [LDAP with StartTLS](#ldap-with-starttls)
  - [Database Role Requirements](#database-role-requirements)
  - [Testing Your Configuration](#testing-your-configuration)
    - [Using psql to Test](#using-psql-to-test)
    - [Connection String Testing](#connection-string-testing)
- [Next Steps](#next-steps)
- [References](#references)

</details>

---
# PostgreSQL LDAP Authentication Configuration Guide
LDAP (Lightweight Directory Access Protocol) authentication allows PostgreSQL to authenticate users against an external directory service such as Active Directory (Azure), OpenLDAP, or other LDAP-compliant servers[^1]. This approach **centralizes user management and provides single sign-on capabilities for database access**.

## Prerequisites
Before configuring LDAP authentication, ensure you have:
- **PostgreSQL v.9.1+** (LDAP support improved significantly in recent versions)[^2]
- **Network connectivity** to your LDAP server
- **LDAP server credentials with (at least) search permissions**
- Understanding of your *LDAP directory structure*

## Basic LDAP Configuration

### Standard LDAP Configuration
The basic LDAP configuration in `pg_hba.conf` follows this pattern:

```bash
# pg_hba.conf - Basic LDAP configuration
# TYPE  DATABASE    USER    ADDRESS    METHOD  OPTIONS
host    database    user    address    ldap    ldapserver=server ldapport=port ldapbinddn="bind_dn" ldapbindpasswd="password" ldapsearchattribute=attribute ldapbasedn="base_dn"
```

### Essential LDAP Parameters

|Parameter|Description|Example|
|---|---|---|
|`ldapserver`|LDAP server hostname or IP|`ldap.company.com`|
|`ldapport`|LDAP server port (389 for LDAP, 636 for LDAPS)|`389`|
|`ldapbinddn`|Distinguished name for binding to LDAP|`cn=admin,dc=company,dc=com`|
|`ldapbindpasswd`|Password for the bind DN|`adminpassword`|
|`ldapsearchattribute`|Attribute to search for username|`uid` or `sAMAccountName`|
|`ldapbasedn`|Base DN for user searches|`ou=users,dc=company,dc=com`|

### Simple LDAP Example

```bash
# pg_hba.conf - Simple LDAP setup
host    myapp    all    192.168.1.0/24    ldap    ldapserver=ldap.company.com ldapport=389 ldapbinddn="cn=readonly,dc=company,dc=com" ldapbindpasswd="readonlypass" ldapsearchattribute=uid ldapbasedn="ou=people,dc=company,dc=com"
```

## Advanced Configuration Examples

### Active Directory Configuration
Active Directory requires specific configuration due to its unique schema and naming conventions[^3]:

```bash
# pg_hba.conf - Active Directory
host    all         all         192.168.1.0/24  ldap        ldapserver=ad.company.com ldapport=389 ldapbinddn="CN=PostgreSQL Service,CN=Users,DC=company,DC=com" ldapbindpasswd="servicepassword" ldapsearchattribute=sAMAccountName ldapbasedn="CN=Users,DC=company,DC=com"
```

Key differences for Active Directory:
- Use `sAMAccountName` instead of `uid`
- DN format uses `CN=` (Common Name) instead of `cn=`
- Users typically located in `CN=Users` container

### Secure LDAP (LDAPS) Configuration
For production environments, always use encrypted connections[^4]:

```bash
# pg_hba.conf - Secure LDAP
host    all         all         192.168.1.0/24  ldap        ldapserver=ldaps.company.com ldapport=636 ldapscheme=ldaps ldapbinddn="cn=admin,dc=company,dc=com" ldapbindpasswd="adminpassword" ldapsearchattribute=uid ldapbasedn="ou=users,dc=company,dc=com"
```

Additional LDAPS considerations:
- Requires valid SSL certificates
- May need CA certificate configuration
- Default port is 636

### Multiple LDAP Servers (Failover)
For high availability, configure multiple LDAP servers[^5]:

```bash
# pg_hba.conf - Multiple LDAP servers
host    all         all         192.168.1.0/24  ldap        ldapserver="ldap1.company.com ldap2.company.com" ldapport=389 ldapbinddn="cn=admin,dc=company,dc=com" ldapbindpasswd="adminpassword" ldapsearchattribute=uid ldapbasedn="ou=users,dc=company,dc=com"
```

### LDAP with StartTLS
StartTLS provides encryption on the standard LDAP port[^6]:

```bash
# pg_hba.conf - LDAP with StartTLS
host    all         all         192.168.1.0/24  ldap        ldapserver=ldap.company.com ldapport=389 ldapscheme=ldap ldapbinddn="cn=admin,dc=company,dc=com" ldapbindpasswd="adminpassword" ldapsearchattribute=uid ldapbasedn="ou=users,dc=company,dc=com" ldaptls=1
```

## Database Role Requirements
PostgreSQL requires database roles to exist for LDAP-authenticated users[^7]:

```sql
-- Create database role that matches LDAP username
CREATE ROLE johndoe LOGIN;

-- Grant necessary permissions
GRANT CONNECT ON DATABASE myapp TO johndoe;
GRANT USAGE ON SCHEMA public TO johndoe;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO johndoe;

-- For email-based usernames, handle special characters
CREATE ROLE "john.doe@company.com" LOGIN;
```

## Testing Your Configuration
### Using psql to Test
To verify your LDAP configuration, use the `psql` command-line tool:

```bash
# Test LDAP authentication
psql -h localhost -U johndoe -d myapp

# Test with specific parameters
PGPASSWORD=userpassword psql -h localhost -U johndoe -d myapp
```
> - the `-h` flag specifies the host, `-U` specifies the user, and `-d` specifies the database.
> - Ensure the user exists in both PostgreSQL and LDAP.
> - If using a password, set the `PGPASSWORD` environment variable or use the `-W` flag to prompt for it.

### Connection String Testing
To test your LDAP connection string, you can use the following command:

```bash
# Test connection string
psql "host=localhost dbname=myapp user=johndoe password=userpassword"
```
> This command will attempt to connect to the PostgreSQL database using the specified parameters. If the connection is successful, you will see a prompt for SQL commands.

> [!NOTE]
> If any issue happens, please refer to the most common ones and how to [troubleshoot](pg-ldap-troubleshooting.md) them.

---
# Next Steps
This guide covers the basic LDAP configuration. For detailed troubleshooting, error resolution, and advanced features, see the related articles:
- [PostgreSQL LDAP Troubleshooting Guide](pg-ldap-troubleshooting.md)
- [LDAP Authentication Security Best Practices](pg-ldap-security.md)
- [Advanced LDAP Features and Optimization](pg-ldap-advanced.md)

# References
[^1]: [PostgreSQL Documentation - LDAP Authentication](https://www.postgresql.org/docs/current/auth-ldap.html)
[^2]: [PostgreSQL Version History - Authentication Improvements](https://www.postgresql.org/docs/current/release.html)
[^3]: [Microsoft Active Directory Schema Reference](https://docs.microsoft.com/en-us/windows/win32/adschema/active-directory-schema) 
[^4]: [LDAP Security Best Practices](https://tools.ietf.org/html/rfc4513)
[^5]: [PostgreSQL High Availability Documentation](https://www.postgresql.org/docs/current/high-availability.html)
[^6]: [StartTLS RFC Specification](https://tools.ietf.org/html/rfc4511)
[^7]: [PostgreSQL User Management](https://www.postgresql.org/docs/current/user-manag.html)
