---
title: PostgreSQL LDAP Auth Troubleshooting
tags:
  - studies
  - programming
  - LDAP
  - PostgreSQL
  - troubleshooting
  - authentication
  - security
  - network
  - performance
  - configuration
  - errors
  - common mistakes
  - logging
  - SSL/TLS
use: Documentation
languages: SQL, shell
dependences: PostgreSQL
---

<details> <summary>Table of Contents 🔖</summary>

- [PostgreSQL LDAP Authentication Troubleshooting Guide](#postgresql-ldap-authentication-troubleshooting-guide)
  - [Common Error Messages and Solutions](#common-error-messages-and-solutions)
    - [Error: "LDAP authentication failed"](#error-ldap-authentication-failed)
      - [Diagnostic Steps](#diagnostic-steps)
        - [Verify LDAP Server Connectivity](#verify-ldap-server-connectivity)
        - [Test Service Account Credentials](#test-service-account-credentials)
        - [Verify User Search](#verify-user-search)
      - [Common Causes and Solutions](#common-causes-and-solutions)
        - [Wrong Search Attribute Configuration](#wrong-search-attribute-configuration)
        - [Incorrect Base DN Structure](#incorrect-base-dn-structure)
        - [Username Format Issues](#username-format-issues)
    - [Error: "Could not connect to LDAP server"](#error-could-not-connect-to-ldap-server)
      - [Diagnostic Steps](#diagnostic-steps-1)
        - [Network Connectivity](#network-connectivity)
        - [DNS Resolution](#dns-resolution)
        - [Firewall and Security Groups](#firewall-and-security-groups)
      - [Solutions](#solutions)
        - [Verify LDAP Server Status](#verify-ldap-server-status)
        - [Configure Firewall Rules](#configure-firewall-rules)
    - [Error: "LDAP bind failed"](#error-ldap-bind-failed)
      - [Diagnostic Steps](#diagnostic-steps-2)
        - [Test Service Account Credentials](#test-service-account-credentials-1)
        - [Check Bind DN Format](#check-bind-dn-format)
        - [Verify Account Status](#verify-account-status)
        - [Solutuions](#solutuions)
  - [Advanced Troubleshooting Techniques](#advanced-troubleshooting-techniques)
    - [Enable Detailed PostgreSQL Logging](#enable-detailed-postgresql-logging)
    - [LDAP Debug Tools and Commands](#ldap-debug-tools-and-commands)
      - [Comprehensive LDAP Testing](#comprehensive-ldap-testing)
      - [LDAP Server Log Analysis](#ldap-server-log-analysis)
    - [Username Mapping Configuration](#username-mapping-configuration)
    - [SSL/TLS Certificate Issues](#ssltls-certificate-issues)
      - [Self-Signed Certificate Configuration](#self-signed-certificate-configuration)
      - [Certificate Debugging](#certificate-debugging)
  - [Performance Troubleshooting](#performance-troubleshooting)
    - [Connection Timeout Issues](#connection-timeout-issues)
    - [Slow LDAP Queries](#slow-ldap-queries)
  - [Common Configuration Mistakes](#common-configuration-mistakes)
      - [Mistake 1: Incorrect Search Scope](#mistake-1-incorrect-search-scope)
      - [Mistake 2: Case Sensitivity Issues](#mistake-2-case-sensitivity-issues)
      - [Mistake 3: Special Characters in Passwords](#mistake-3-special-characters-in-passwords)
  - [Troubleshooting Checklist](#troubleshooting-checklist)
- [References](#references)

</details>

---
# PostgreSQL LDAP Authentication Troubleshooting Guide
LDAP authentication issues can be complex to diagnose due to the multiple layers involved: *PostgreSQL configuration*, *network connectivity*, *LDAP server setup*, and *user directory structure*[^1]. This guide provides systematic approaches to identify and resolve common LDAP authentication problems.

## Common Error Messages and Solutions

### Error: "LDAP authentication failed"
This is the most common LDAP error and can have multiple root causes[^2]:

```shell
psycopg2.OperationalError: LDAP authentication failed for user "user@company.com"
```

#### Diagnostic Steps
##### Verify LDAP Server Connectivity
This will garantee that your PostgreSQL server can reach the LDAP server:

```bash
# Basic connectivity test
nc -zv ldap.company.com 389

# LDAP protocol test
ldapsearch -x -H ldap://ldap.company.com -s base -b "" "(objectclass=*)"
```

If the above commands fail, check your network settings, firewall rules, and DNS resolution.

##### Test Service Account Credentials
To check if the service account used for LDAP binding is correct - if the binding fails, it indicates an issue with the service account credentials or permissions[^2], use the following command:

```bash
# Test bind credentials manually
ldapsearch -x -H ldap://ldap.company.com -D "cn=admin,dc=company,dc=com" -w adminpassword -s base
```

> [!INFO]
> User binding is the process of authenticating to the LDAP server using a service account.

##### Verify User Search
If the connection and binding are successful, the next step is to verify that the user can be found in the LDAP directory, that's why the understanding of the LDAP search base and attributes is crucial, also will be required a basic knowledge of yours LDAP directory structure and schemas. User the following command to search for a `specific_user`:

```bash
# Search for specific_user
ldapsearch -x -H ldap://ldap.company.com -D "cn=admin,dc=company,dc=com" -w adminpassword -b "ou=users,dc=company,dc=com" "(uid=specific_user)"
```

#### Common Causes and Solutions
Here are some common causes of LDAP authentication failures and their solutions.

##### Wrong Search Attribute Configuration
The `ldapsearchattribute` must match your LDAP schema[^3]:

```bash
# For Active Directory, use sAMAccountName
ldapsearchattribute=sAMAccountName

# For standard LDAP, use uid
ldapsearchattribute=uid

# For email-based authentication, use mail
ldapsearchattribute=mail
```

##### Incorrect Base DN Structure
Verify your directory structure:

```bash
# Check organizational units
ldapsearch -x -H ldap://ldap.company.com -D "cn=admin,dc=company,dc=com" -w adminpassword -b "dc=company,dc=com" "(objectClass=organizationalUnit)"

# Common base DN patterns
# Standard LDAP: ou=users,dc=company,dc=com
# Active Directory (Azure): CN=Users,DC=company,DC=com
# Custom OUs: ou=employees,ou=people,dc=company,dc=com
```

##### Username Format Issues
Different LDAP servers expect different username formats[^4]:

```bash
# Test different username formats
# Full email: user@company.com
# Just username: user
# Distinguished name: cn=user,ou=users,dc=company,dc=com
# Domain\username: DOMAIN\user (Active Directory)
```

---
### Error: "Could not connect to LDAP server"
Network connectivity issues are common in enterprise environments[^5]:

```
FATAL: could not connect to LDAP server: Can't contact LDAP server
```

In order to solve this error, you need to check the network connectivity, DNS resolution, and firewall settings.

#### Diagnostic Steps

##### Network Connectivity
Test if the PostgreSQL server can reach the LDAP server:

```bash
# Test LDAP server connectivity
telnet ldap.company.com 389

# Test LDAPS connectivity
telnet ldaps.company.com 636

# Test with timeout
timeout 5 bash -c "</dev/tcp/ldap.company.com/389" && echo "Port 389 is open"
```
> - `telnet` is used to check if the LDAP server is reachable on the specified port.
> - `timeout` is used to limit the connection attempt duration, preventing long hangs if the server is unreachable.
> - `bash -c "</dev/tcp/ldap.company.com/389"` is a method to test TCP connectivity in bash, which is useful if `telnet` is not available.

##### DNS Resolution
Check if the LDAP server's hostname resolves correctly:

```bash
# Verify DNS resolution
nslookup ldap.company.com
dig ldap.company.com

# Test with IP address if DNS fails
ldapsearch -x -H ldap://192.168.1.100 -D "cn=admin,dc=company,dc=com" -w adminpassword -s base
```
> - `nslookup` and `dig` are used to verify that the LDAP server's hostname resolves to the correct IP address.
> - If DNS resolution fails, you can use the LDAP server's IP address directly in your commands.

##### Firewall and Security Groups
Check if the firewall or security groups allow traffic to the LDAP server:

```bash
# Check local firewall
sudo ufw status
iptables -L

# Common LDAP ports that need to be open
# 389 - Standard LDAP
# 636 - LDAPS (SSL)
# 3268 - Active Directory Global Catalog
# 3269 - Active Directory Global Catalog SSL
```
> - `sudo ufw status` checks the status of the Uncomplicated Firewall (UFW) on Ubuntu/Debian systems.
> - `iptables -L` lists the current iptables rules, which can help identify if any rules are blocking LDAP traffic.
> - Ensure that the firewall allows inbound and outbound traffic on the necessary LDAP ports (389 for standard LDAP, 636 for LDAPS).

#### Solutions
If any of the above tests fail, you can take the following actions:

##### Verify LDAP Server Status
To ensure the LDAP server is running and accessible, you can check its status using system commands. The command may vary depending on the LDAP server type (OpenLDAP, Active Directory, etc.):

```bash
# Check if LDAP service is running
systemctl status slapd    # For OpenLDAP
systemctl status ldap     # For some distributions
systemctl status ntds     # For Windows Active Directory
```

##### Configure Firewall Rules
If the firewall is blocking LDAP traffic, you need to allow the necessary ports. The commands below are examples for Ubuntu/Debian and CentOS/RHEL systems:

```bash
# Ubuntu/Debian firewall configuration
sudo ufw allow from 192.168.1.0/24 to any port 389
sudo ufw allow from 192.168.1.0/24 to any port 636

# CentOS/RHEL firewall configuration
sudo firewall-cmd --permanent --add-port=389/tcp
sudo firewall-cmd --permanent --add-port=636/tcp
sudo firewall-cmd --reload
```

---
### Error: "LDAP bind failed"
Authentication issues with the service account[^6]:

```
FATAL: LDAP bind failed: Invalid credentials
```

#### Diagnostic Steps

##### Test Service Account Credentials
To verify that the service account used for LDAP binding is correct, you can use the `ldapsearch` command to attempt a bind operation with the service account credentials. This will help confirm whether the credentials are valid and if the service account has the necessary permissions to perform LDAP operations.

```bash
# Test bind credentials directly
ldapsearch -x -H ldap://ldap.company.com -D "cn=admin,dc=company,dc=com" -w adminpassword -s base -b "cn=admin,dc=company,dc=com"
```

##### Check Bind DN Format
Ensure the `ldapbinddn` is correctly formatted for your LDAP server. The format can vary between standard LDAP and Active Directory:

```bash
# Standard LDAP format
ldapbinddn="cn=admin,dc=company,dc=com"

# Active Directory format
ldapbinddn="CN=PostgreSQL Service,CN=Users,DC=company,DC=com"

# Alternative Active Directory format
ldapbinddn="DOMAIN\serviceaccount"
```

##### Verify Account Status
Check if the service account is enabled and not locked out or expired. This can be done using LDAP search commands to retrieve the `userAccountControl` attribute for Active Directory or similar attributes for other LDAP servers.

```bash
# Check if account is enabled and not expired
ldapsearch -x -H ldap://ldap.company.com -D "cn=admin,dc=company,dc=com" -w adminpassword -b "cn=serviceaccount,cn=users,dc=company,dc=com" "(objectclass=*)" userAccountControl
```

##### Solutuions
If the bind operation fails, you can take the following actions:
- Verify the service account credentials and ensure they are correct.
- Check if the service account has the necessary permissions to bind to the LDAP server.
- Ensure the service account is not locked out or expired.

---
## Advanced Troubleshooting Techniques

### Enable Detailed PostgreSQL Logging
To configure PostgreSQL for comprehensive LDAP debugging[^7]:

```bash
# postgresql.conf
log_connections = on
log_disconnections = on
log_statement = 'all'
log_min_messages = debug1
log_line_prefix = '%t [%p]: [%l-1] user=%u,db=%d,app=%a,client=%h '
```

This will log all connection attempts, disconnections, and detailed messages, which can help identify LDAP-related issues and possible attacks and security breaches.

### LDAP Debug Tools and Commands

#### Comprehensive LDAP Testing
Is important to test LDAP connections and queries thoroughly. Here are some useful commands:

```bash
# Test LDAP connection with verbose output
ldapsearch -x -H ldap://ldap.company.com -D "cn=admin,dc=company,dc=com" -w adminpassword -b "ou=users,dc=company,dc=com" "(uid=testuser)" -v

# Test with specific user authentication
ldapsearch -x -H ldap://ldap.company.com -D "uid=testuser,ou=users,dc=company,dc=com" -w userpassword -s base -b "uid=testuser,ou=users,dc=company,dc=com"

# Test Active Directory specific attributes
ldapsearch -x -H ldap://ad.company.com -D "CN=admin,CN=Users,DC=company,DC=com" -w adminpassword -b "CN=Users,DC=company,DC=com" "(sAMAccountName=testuser)" sAMAccountName mail memberOf
```
> - `-v` enables verbose output, which can provide additional information about the LDAP operations being performed;
> - The `-s base` option specifies a base search scope, which is useful for testing specific user entries;
> - The `sAMAccountName` and `mail` attributes are commonly used in Active Directory environments, and the `memberOf` attribute can help verify group memberships;
> - Ensure that the `ldapsearch` command is installed on your system. If not, you can install it using your package manager (e.g., `apt-get install ldap-utils` on Debian/Ubuntu or `yum install openldap-clients` on CentOS/RHEL).

#### LDAP Server Log Analysis
To analyze LDAP server logs for authentication issues, you can use the following commands. The exact log file location may vary depending on your LDAP server configuration (e.g., OpenLDAP, Active Directory).

```bash
# OpenLDAP logs
tail -f /var/log/slapd.log
journalctl -u slapd -f

# Active Directory logs (Windows Event Viewer)
# Look for Event IDs: 4625 (failed logon), 4624 (successful logon)

# Generic LDAP logs
tail -f /var/log/ldap.log
tail -f /var/log/auth.log | grep ldap
```
> - `tail -f` allows you to monitor the log file in real-time, which is useful for troubleshooting ongoing issues;
> - `journalctl -u slapd -f` is used to follow the OpenLDAP service logs on systems using `systemd`;
> - For Active Directory, you can use the Windows Event Viewer to filter logs by specific Event IDs related to authentication faliures (e.g., `4625` for failed logon attempts and `4624` for successful logons);
> - `grep ldap` filters the authentication logs to show only LDAP-related entries, which can help you quickly identify issues.

### Username Mapping Configuration
When LDAP usernames don't match PostgreSQL role names, use mapping[^8]:

```bash
# pg_ident.conf - Username mapping
# MAPNAME       SYSTEM-USERNAME         PG-USERNAME
ldapmap         john.doe                johndoe
ldapmap         jane.smith              janesmith
ldapmap         "user@domain.com"       user_domain_com
ldapmap         "DOMAIN\user"           domain_user
```

Maps allow you to translate LDAP usernames to PostgreSQL usernames, which is useful when the LDAP naming conventions differ from PostgreSQL's expectations. Remember to always reference the map in `pg_hba.conf` file:

```bash
host    all    all    192.168.1.0/24    ldap    ldapserver=ldap.company.com ldapport=389 ldapbinddn="cn=admin,dc=company,dc=com" ldapbindpasswd="adminpassword" ldapsearchattribute=uid ldapbasedn="ou=users,dc=company,dc=com" map=ldapmap
```

### SSL/TLS Certificate Issues
Certificate problems are common with LDAPS[^9]:

> [!QUESTION]
> Why use LDAPS?
> LDAPS (LDAP over SSL) encrypts LDAP traffic, protecting sensitive data during transmission. It is essential for secure communication between PostgreSQL and the LDAP server, especially in production environments.

#### Self-Signed Certificate Configuration
If you're using a self-signed (or internal CA) certificate, you need to configure PGSQL and the LDAP client to trust it:

```bash
# Temporarily disable certificate validation (NOT for production)
# echo "TLS_REQCERT never" >> /etc/ldap/ldap.conf

# Better approach - configure CA certificate
echo "TLS_CACERT /path/to/ca-cert.pem" >> /etc/ldap/ldap.conf
echo "TLS_REQCERT demand" >> /etc/ldap/ldap.conf
```
> - `TLS_REQCERT never` disables certificate validation, which isn't recommended for prod environments;
> - `TLS_CACERT` specifies the path to the CA certificate that should be trusted;
> - `TLS_REQCERT demand` enforces certificate validation, ensuring that the LDAP server presents a valid certificate.

#### Certificate Debugging
To debug LDAPS certificate issues, you can use the `openssl` command to connect to the LDAP server and inspect the certificate chain:

```bash
# Test LDAPS certificate
openssl s_client -connect ldaps.company.com:636 -showcerts

# Verify certificate chain
openssl verify -CAfile /path/to/ca-cert.pem /path/to/server-cert.pem

# Test LDAP with StartTLS
ldapsearch -x -H ldap://ldap.company.com -D "cn=admin,dc=company,dc=com" -w adminpassword -Z -b "ou=users,dc=company,dc=com" "(uid=testuser)"
```
> - `openssl s_client` connects to the LDAP server over LDAPS and shows the server's certificate chain, which can help indentify and understand what issues may exist;
> - `openssl verify` checks if the server certificate is valid and trusted by the specified CA certificate;
> - `ldapsearch -Z` tests the LDAP server with StartTLS, which is an alternative to LDAPS that upgrades an existing unencrypted connection to a secured one.

## Performance Troubleshooting
Resolving performance issues with LDAP authentication can involve several strategies, including increasing connection timeouts and optimizing LDAP queries[^1].

### Connection Timeout Issues
To address connection timeouts, you can adjust the timeout settings in both PGSQL and the LDAP client configuration. Increasing the throughput is particularly useful in environments with high latency or slow LDAP servers.

```bash
# Increase connection timeout in postgresql.conf
authentication_timeout = 60s

# Test with longer timeout
ldapsearch -x -H ldap://ldap.company.com -D "cn=admin,dc=company,dc=com" -w adminpassword -b "ou=users,dc=company,dc=com" "(uid=testuser)" -o nettimeout=30
```

### Slow LDAP Queries
If LDAP queries are slow, consider the following optimizations:

```bash
# Optimize LDAP search with specific attributes
ldapsearch -x -H ldap://ldap.company.com -D "cn=admin,dc=company,dc=com" -w adminpassword -b "ou=users,dc=company,dc=com" "(uid=testuser)" uid mail cn
```

Use indexed attributes for better performance, ensure uid, sAMAccountName, or mail are indexed on LDAP server. To create indexes on LDAP attributes, you may need to modify the LDAP server schema or configuration:
- For OpenLDAP, you can add indexes in the `slapd.conf` or `cn=config` directory: `index uid,mail eq`;
- For Active Directory, ensure that the attributes you frequently search on are indexed by default, or create custom indexes using the Active Directory Administrative Center or PowerShell;
- For other LDAP servers, refer to their documentation for indexing capabilities.

## Common Configuration Mistakes
Some configuration mistakes can lead to auth issues or unexpected behavior. Here are some common mistakes and how to fix them:

#### Mistake 1: Incorrect Search Scope
The search scope is the amount of the directory tree that the LDAP server will search when looking for the user entries. If the scope is too narrow, it may not return the expected results.

```bash
# Wrong - searches only one level
ldapsearchattribute=uid
ldapbasedn="dc=company,dc=com"

# Correct - searches in specific OU
ldapsearchattribute=uid
ldapbasedn="ou=users,dc=company,dc=com"
```
> - The `ldapbasedn` should be set to the specific organizational unit (OU) where user entries are located, rather than the root of the tree;
> - The `ldapsearchattribute` should match the attribute used for user identification in your LDAP schema, such as `uid` for standard LDAP or `sAMAccountName` for AD environments;
> - Ensure that the search base is set to the correct OU or subtree where the users are located, as this will improve the performance and the accuracy of the search.

#### Mistake 2: Case Sensitivity Issues
The LDAP attributes are case-sensitive, and using the wrong case can lead to auth failures or unexpected behavior. Always use the correct case for attrs and values.

```bash
# LDAP attributes are case-sensitive
# Wrong
ldapsearchattribute=UID

# Correct
ldapsearchattribute=uid
```

#### Mistake 3: Special Characters in Passwords
Special characters in passwords can cause issues if not properly escaped. Ensure that your password is correctly formatted to avoid authentication errors.

```bash
# Escape special characters in passwords
# If password contains quotes, escape them
ldapbindpasswd="pass\"word"

# Or use different quote style
ldapbindpasswd='pass"word'
```

----
## Troubleshooting Checklist

When LDAP authentication fails, work through this checklist:
- [ ] **Network connectivity**: Can PostgreSQL server reach LDAP server?
- [ ] **LDAP server status**: Is the LDAP service running and responding?
- [ ] **Bind credentials**: Are the service account credentials correct?
- [ ] **User search**: Can the service account find the user in LDAP?
- [ ] **User credentials**: Are the user's LDAP credentials valid?
- [ ] **PostgreSQL role**: Does a matching role exist in the database?
- [ ] **Permissions**: Does the user have necessary database permissions?
- [ ] **Username format**: Is the username format consistent between LDAP and PostgreSQL?
- [ ] **Certificate validation**: Are SSL/TLS certificates properly configured?
- [ ] **Firewall rules**: Are the necessary ports open?

---
# References
[^1]: [PostgreSQL LDAP Authentication Documentation](https://www.postgresql.org/docs/current/auth-ldap.html)
[^2]: [Common LDAP Error Codes](https://ldap.com/ldap-result-code-reference/) 
[^3]: [LDAP Schema Reference](https://tools.ietf.org/html/rfc4519) 
[^4]: [Active Directory User Principal Names](https://docs.microsoft.com/en-us/windows/win32/adschema/a-userprincipalname) 
[^5]: [Network Troubleshooting for LDAP](https://tools.ietf.org/html/rfc4511) 
[^6]: [LDAP Bind Operation](https://tools.ietf.org/html/rfc4511#section-4.2) 
[^7]: [PostgreSQL Logging Configuration](https://www.postgresql.org/docs/current/runtime-config-logging.html) 
[^8]: [PostgreSQL User Name Maps](https://www.postgresql.org/docs/current/auth-username-maps.html) 
[^9]: [LDAP TLS/SSL Configuration](https://tools.ietf.org/html/rfc4513)
