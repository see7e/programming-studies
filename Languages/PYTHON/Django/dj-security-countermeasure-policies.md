---
title: Django Security Countermeasure Policies Against Reconnaissance Attacks
tags:
  - studies
  - programming
  - security
  - django
  - web-security
  - web-development
use: Documentation
languages: Python
dependences: Django
---

<details> <summary>Table of Contents 🔖</summary>

- [Django Security Countermeasure Policies Against Reconnaissance Attacks](#django-security-countermeasure-policies-against-reconnaissance-attacks)
  - [Overview](#overview)
  - [Core Reconnaissance Threats Identified](#core-reconnaissance-threats-identified)
  - [Django-Specific Countermeasure Policies](#django-specific-countermeasure-policies)
    - [Subdomain and DNS Security](#subdomain-and-dns-security)
    - [JavaScript Security Hardening](#javascript-security-hardening)
      - [Content Security Policy (CSP)](#content-security-policy-csp)
      - [JavaScript Secret Management](#javascript-secret-management)
    - [HTTP Security Headers](#http-security-headers)
      - [Comprehensive Header Configuration](#comprehensive-header-configuration)
      - [Custom Middleware Example](#custom-middleware-example)
    - [API Endpoint Protection](#api-endpoint-protection)
      - [API Security Configuration](#api-security-configuration)
        - [`DEFAULT_AUTHENTICATION_CLASSES`](#default_authentication_classes)
        - [`DEFAULT_PERMISSION_CLASSES`](#default_permission_classes)
        - [`DEFAULT_THROTTLE_CLASSES`](#default_throttle_classes)
        - [`DEFAULT_THROTTLE_RATES`](#default_throttle_rates)
      - [Custom API Key Authentication](#custom-api-key-authentication)
    - [Static Files and Media Security](#static-files-and-media-security)
      - [Static File Protection](#static-file-protection)
      - [Custom middleware for media file protection](#custom-middleware-for-media-file-protection)
    - [Directory Traversal Protection](#directory-traversal-protection)
      - [Example Use Case](#example-use-case)
    - [Rate Limiting and Brute Force Protection](#rate-limiting-and-brute-force-protection)
    - [Debug and Development Security](#debug-and-development-security)
- [References](#references)

</details>

---

# Django Security Countermeasure Policies Against Reconnaissance Attacks

## Overview

[This video](https://www.youtube.com/watch?v=sQicUuAhVes) demonstrates sophisticated reconnaissance techniques used by attackers to map and exploit web applications. These techniques include **subdomain enumeration**, **JavaScript analysis**, **endpoint discovery**, and **asset graphing**. This analysis (tries to) provides comprehensive countermeasure policies specifically for Django applications, along with broader security recommendations for other frameworks.

## Core Reconnaissance Threats Identified
The video reveals several critical attack vectors:
1. **Subdomain Enumeration**: Discovering hidden subdomains and development environments
2. **JavaScript Analysis**: Extracting API endpoints, tokens, and secrets from client-side code
3. **HTTP Fingerprinting**: Identifying technology stacks and server configurations
4. **Endpoint Discovery**: Finding unprotected API endpoints and admin panels
5. **Asset Graphing**: Mapping interconnected infrastructure components
6. **Passive Information Gathering**: Using public databases and historical data

## Django-Specific Countermeasure Policies

### Subdomain and DNS Security
Some attempts can be noticed by Django's security mechanism when raising `DisallowedHost` in an [`Invalid HTTP_HOST Header` Error](dj-invalid-HTTP_HOST-error.md).

**Policy Implementation:**

```python
# settings.py
ALLOWED_HOSTS = [
    'yourdomain.com',
    'www.yourdomain.com',
    # Never use wildcards in production
]

# Use specific host validation
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

**Subdomain Isolation Policy:**[^1][^2]

```python
# Custom middleware for subdomain validation
class SubdomainValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        host = request.get_host()
        if not self.is_valid_subdomain(host):
            return HttpResponseForbidden("Invalid subdomain")
        return self.get_response(request)
```

**DNS Security Recommendations:**[^3][^4]
- Implement **[Domain Name System Security Extensions (DNSSEC)](https://www.icann.org/resources/pages/dnssec-what-is-it-why-important-2019-03-05-en)** for domain authentication
- Use **DNS filtering** to block malicious domains
- Configure **DNS rate limiting** to prevent enumeration
- **Restrict zone transfers** to authorized servers only

### JavaScript Security Hardening
**Why it’s important:**  
Modern web apps rely heavily on JavaScript. If not properly controlled, malicious scripts can:
- Steal cookies and tokens (XSS)
- Inject malware into user sessions
- Hijack user accounts

Django doesn’t automatically enforce browser-level JavaScript policies, so you must configure **Content Security Policy (CSP)** and follow **secret management practices**.

#### Content Security Policy (CSP)
[^5][^6][^7]
Is an HTTP header (or Django setting) that tells browsers **which sources of content are allowed to be loaded**.  
It is one of the most effective defenses against **Cross-Site Scripting (XSS)**.

Django doesn’t include CSP by default, but you can use the [django-csp](https://github.com/mozilla/django-csp) package to set policies in `settings.py`.

```python
CSP_DEFAULT_SRC = ("'self'",)
```
> **Default sources:**
> All content (scripts, styles, images, etc.) must be loaded **only from your own domain**.
> - `'self'` means the same origin as your website.

```python
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'")
```
> **JavaScript sources:**
> - `'self'`: Load scripts from your server.
> - `'unsafe-inline'`: Allow inline `<script>` tags.

> [!WARNING]
> `'unsafe-inline'` **weakens CSP significantly**—use carefully.
> It’s better to remove this and use **non-inline scripts** with [Subresource Integrity](https://developer.mozilla.org/docs/Web/Security/Subresource_Integrity) checks.

```python
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")
```
> **CSS sources:**
> Same as `SCRIPT_SRC`, allowing inline `<style>` blocks.

```python
CSP_IMG_SRC = ("'self'", "data:", "https:")
```
> **Image sources:**
> - `'self'`: Images served by your app.
> - `data:`: Allow base64-encoded images.
> - `https:`: Allow images from any HTTPS origin.

```python
CSP_CONNECT_SRC = ("'self'",)
```
> **XHR/WebSocket sources:**
> Restricts AJAX and WebSocket connections to your server only.

```python
CSP_FONT_SRC = ("'self'", "https://fonts.gstatic.com")
```
> **Font sources:**
> -  Your server
> -  Google Fonts CDN (`fonts.gstatic.com`)

```python
CSP_OBJECT_SRC = ("'none'",)
```
> **Plugins:**
> Prohibits `<object>`, `<embed>`, and `<applet>`.
> **Highly recommended** to prevent Flash or Java plugin injection.

```python
CSP_BASE_URI = ("'self'",)
```
> **Base URL:**
> Restricts `<base>` tags to your own domain.

```python
CSP_FRAME_ANCESTORS = ("'none'",)
```
> **Framing / Clickjacking:**
> Prevents your site from being embedded in `<iframe>`.
> **Great protection against clickjacking attacks.**

#### JavaScript Secret Management
[^8][^9][^10]
JavaScript is **public**: any variable you expose in your HTML templates is accessible to anyone inspecting the page.

So you must **never** embed secrets in JavaScript.

```python
# Never expose sensitive data in JavaScript
# Use environment variables for secrets
import os
from django.conf import settings

SECRET_API_KEY = os.getenv('SECRET_API_KEY')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
```
This ensures:
- Secrets are **never committed to version control**.
- They **aren’t rendered in templates**.

```python
# Template context processor to avoid exposing secrets
def safe_context(request):
    return {
        'api_endpoint': settings.PUBLIC_API_ENDPOINT,
        # Never include secret keys or tokens
    }
```
This prevents:
- Accidental leaks of credentials
- Exposing tokens or passwords in rendered HTML

Example:

```html
<script>
  window.APP_CONFIG = {
    apiEndpoint: "{{ api_endpoint|escapejs }}"
  };
</script>
```

### HTTP Security Headers

#### Comprehensive Header Configuration
[^11][^12]

```python
SECURE_BROWSER_XSS_FILTER = True
```
> **X-XSS-Protection:**
> - This header instructs older browsers to **enable their built-in XSS filters**.
> - When set to `True`, Django sends: `X-XSS-Protection: 1; mode=block`
> If an XSS attack is detected, the browser **blocks rendering** instead of sanitizing.

> [!NOTE]
> Modern browsers (Chrome, Edge) no longer rely on this header because **Content Security Policy (CSP)** is preferred, but it doesn’t hurt to leave this as extra defense for legacy clients.

```python
SECURE_CONTENT_TYPE_NOSNIFF = True
```
> **X-Content-Type-Options:**
> - This header prevents **MIME sniffing**.
> - Without it, a browser might "guess" a file type incorrectly, which can lead to content-type confusion attacks (e.g., uploading a JavaScript file but serving it as a harmless image).
> - When enabled, Django sets: `X-Content-Type-Options: nosniff`

```python
SECURE_FRAME_DENY = True
```
> **X-Frame-Options:**
> - This header prevents your site from being loaded in an `<iframe>`.
> - Protects against **clickjacking**.
> - When `True`, Django sends: `X-Frame-Options: DENY`

> [!NOTE]
> If you *need* to embed your app in iframes (e.g., on trusted domains), you can instead use:
> ```python
> X-Frame-Options: SAMEORIGIN
> ```
> …but `DENY` is more restrictive and safer.

```python
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
```
> **HTTP Strict Transport Security (HSTS):**
> - Enforces HTTPS connections for your domain and **all subdomains**.
> - Prevents protocol downgrade attacks (MITM).
> - Works in combination with `SECURE_HSTS_SECONDS`:

```python
SECURE_HSTS_SECONDS = 31536000
```
> **HSTS duration:**
> - Tells browsers to remember the HTTPS requirement for **1 year (31,536,000 seconds)**.
> - Sends this header: `Strict-Transport-Security: max-age=31536000; includeSubDomains`

```python
SECURE_HSTS_PRELOAD = True
```
> **HSTS Preload:**
> - Signals you want to submit your domain to the [HSTS preload list](https://hstspreload.org/).
> - This list is built into browsers and enforces HTTPS **from the first visit**.
> - Adds `preload` directive: `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`

> [!WARNING]
> Make sure your HTTPS is correctly configured **before enabling preload**, because once you’re on the list, you can’t easily remove yourself.

```python
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
```
> **Referrer-Policy:**
> - Controls what gets sent in the `Referer` header when navigating from your site.
> - `strict-origin-when-cross-origin` means:
>   - For same-origin requests, full URL is sent.
>   - For cross-origin requests, only the origin is sent.
>   - Downgrades (HTTPS → HTTP) send no referrer.
> - This helps prevent leaking sensitive URLs to third parties.

#### Custom Middleware Example
The example middleware allows you to **add or override headers** beyond Django’s settings:

```python
# Custom middleware for additional headers
class SecurityHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        response = self.get_response(request)
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        return response
```

**What happens here?**
- Every response gets these headers added.
- This approach is helpful if:
    - You use a version of Django that doesn’t have all `SECURE_*` settings.
    - You want to set different headers for certain paths or views.

> [!TIP]
> Always place this middleware **near the top of `MIDDLEWARE`** so it can enforce headers early.

### API Endpoint Protection
Django REST Framework (DRF) makes it easy to build APIs, but **it’s our job to secure them properly**.

The configuration you shared touches on **authentication**, **permissions**, **throttling**, and **custom API keys**—all critical parts of API hardening.

#### API Security Configuration
[^13][^14]

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}
```

##### `DEFAULT_AUTHENTICATION_CLASSES`
This determines **how incoming requests are authenticated**.

**What does each class do?**
- `TokenAuthentication`
  - Expects clients to send a token header: `Authorization: Token <your-token>`
  - Suitable for **API clients (mobile apps, JavaScript frontends)**.
  - Requires issuing and managing tokens (e.g., via `rest_framework.authtoken`).
- `SessionAuthentication`
  - Uses Django’s **session cookie** for authentication.
  - Useful when your API is called by web pages rendered from Django templates.
  - Automatically logs in users authenticated via the Django login view.

> [!TIP]
> Many production APIs disable `SessionAuthentication` to avoid CSRF complexities, relying only on tokens or JWT.

##### `DEFAULT_PERMISSION_CLASSES`
This controls **who has access to the API endpoints by default**.
- `IsAuthenticated`
  - Only authenticated users can access your API.
  - All unauthenticated requests return: `HTTP 401 Unauthorized`
✅ **Good practice** to set this globally—then you can override per view if needed (e.g., for public endpoints).

##### `DEFAULT_THROTTLE_CLASSES`
This configures **rate limiting**, which helps prevent:
- Abuse
- Brute-force attacks
- Denial of Service (DoS)

**Classes:**
- `AnonRateThrottle`: Limits anonymous (unauthenticated) users.
- `UserRateThrottle`: Limits authenticated users.

##### `DEFAULT_THROTTLE_RATES`
**Limits:**
- Anonymous users: **100 requests per day**
- Authenticated users: **1000 requests per day**

If clients exceed the limit, they get: `HTTP 429 Too Many Requests`

> [!TIP]
> Adjust these numbers based on your app’s needs and expected load.

#### Custom API Key Authentication

```python
# Custom API key authentication
class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.META.get('HTTP_X_API_KEY')
        if not api_key:
            return None
        
        # Validate API key securely
        if not self.is_valid_api_key(api_key):
            raise AuthenticationFailed('Invalid API key')
        return (None, None)
```

What does this do?
- **`request.META`** is a dictionary of all HTTP headers (and WSGI environment).
    - `HTTP_X_API_KEY` looks for: `X-API-KEY: <your-key>`
- If no key is provided, it returns `None` (so other authentication methods can try).
- If the key is invalid, it raises `AuthenticationFailed`, returning: `HTTP 401 Unauthorized`
- `is_valid_api_key()` is your custom validation logic (e.g., lookup in the DB or compare with a known secret).

### Static Files and Media Security
Many developers focus heavily on securing _views_ and _APIs_, but forget that **static and media files can also be attack vectors**:
- Leaking sensitive uploads (e.g., user documents)
- Exposing unprotected downloads
- Serving outdated JavaScript or CSS

This configuration helps ensure **your files are served safely and responsibly**.

#### Static File Protection
[^15][^16][^17]

```python
# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Secure static file serving
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Media file security
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

```

> [!WARNING]
> In production use `ManifestStaticFilesStorage`, it solves two big problems:
> 1. **Cache Invalidation:**
>   - Your users always get the latest version after deployment.
>   - No need to ask them to clear their browser cache.
> 2. **Efficient Caching:**
>   - You can configure your web server or CDN to cache static files **forever** (e.g., `Cache-Control: max-age=31536000`) because filenames change whenever content changes.
> 
> If you use a CDN or aggressive caching, **always use hashed filenames**.

#### Custom middleware for media file protection
This middleware restricts access to **authenticated users only**:

```python
class MediaProtectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.path.startswith('/media/'):
            # Check authentication for sensitive files
            if not request.user.is_authenticated:
                return HttpResponseForbidden()
        return self.get_response(request)
```

**How does this work?**
- Every request for `/media/...` files is intercepted.
- If the user is **not logged in**, it returns: `HTTP 403 Forbidden`

**Benefits:**
- Protects sensitive uploads.
- Simple and effective for small projects.

**Limitations:**
- This approach works **only if Django serves the files.**
- If you use Nginx or S3, **you must configure protection there instead**.

> [!TIP]
> ##### Alternative Approaches for Media File Security
> Depending on your infrastructure, consider:
> - **Nginx internal redirect:** Use `X-Accel-Redirect` to serve files after Django checks permissions.
> - **AWS S3 signed URLs:** Generate time-limited URLs for download.
> - **Storage backends:** Use [django-storages](https://django-storages.readthedocs.io/) to manage permissions on S3 or other backends.
> - **Per-file permissions:** Store metadata about each file and validate it before serving.

### Directory Traversal Protection
[^18][^19][^20]
*Path Traversal* (aka Directory Traversal) is **an attack where an attacker manipulates file paths to access files outside the intended directory**.

**Examples of attacks:**
- `../../etc/passwd`
- `/var/www/media/../../secret.txt`
- `%2e%2e%2f` (encoded `../`)

**If your application directly uses user input in file paths**, an attacker could:
- Read sensitive system files (e.g., `passwd`, SSH keys)
- Download private user data
- Overwrite critical files

The `safe_file_path()` function **sanitizes and validates user-provided paths**:

```python
import os
from django.core.exceptions import SuspiciousOperation

def safe_file_path(user_input, base_path):
    """Safely resolve file paths to prevent directory traversal"""
    # Normalize the path
    normalized_path = os.path.normpath(user_input)
    
    # Check for directory traversal attempts
    if '..' in normalized_path or normalized_path.startswith('/'):
        raise SuspiciousOperation("Directory traversal attempt detected")
    
    # Construct full path
    full_path = os.path.join(base_path, normalized_path)
    
    # Ensure the path is within the base directory
    if not full_path.startswith(base_path):
        raise SuspiciousOperation("Path traversal attempt detected")
    
    return full_path
```
**Why all these steps are needed:**  
Relying on just one check isn’t enough. Attackers can combine:
- Encoded characters (`%2e%2e/`)
- Symlinks
- Double slashes
- Trailing dots
**Layered checks are the safest approach.**

#### Example Use Case
Suppose you have an endpoint:

```bash
/download/?file=report.pdf
```

You might use:

```python
safe_path = safe_file_path(request.GET["file"], settings.MEDIA_ROOT)
with open(safe_path, "rb") as f:
    return FileResponse(f)
```

**This ensures:**
- Users can only download files inside `MEDIA_ROOT`.
- No traversal to other directories.

> [!INFO]
> #### Why raise `SuspiciousOperation`?
> 
> ```python
> raise SuspiciousOperation("Directory traversal attempt detected")
> ```
> 
> `SuspiciousOperation` is a **Django-specific exception** that:
> - Signals that the request is malicious.
> - Automatically returns `400 Bad Request`.
> - Logs the incident for you to review.
> 
> ✅ Much safer than returning a 500 error or exposing file paths.

### Rate Limiting and Brute Force Protection
[^21]
Web apps are frequent targets for:
- **Credential stuffing** (testing breached passwords)  
- **Brute-force attacks** (guessing credentials by repeated login attempts)  
- **Enumeration** (finding valid usernames)

If you don’t put protection in place, attackers can automate thousands of login attempts in minutes.

**Rate limiting + lockouts stop this.**

Django Defender is a popular library that adds:
- Login attempt monitoring
- Automatic lockouts
- Cool-off periods
- Redis-based persistence (so it works across multiple servers)

Django Defender Integration

```python
# settings.py
INSTALLED_APPS = [
    'defender',
    # ... other apps
]

DEFENDER_REDIS_URL = 'redis://localhost:6379/0'
DEFENDER_LOCKOUT_COOLOFF_TIME = 300  # 5 minutes
DEFENDER_FAILURE_LIMIT = 5
DEFENDER_LOGIN_FAILURE_LIMIT = 5
DEFENDER_LOCKOUT_TEMPLATE = 'defender/lockout.html'
```

> [!TIP]
> #### Advanced Recommendations
> If you want stronger protection:
> - **Use IP whitelisting:** Allow unlimited attempts from internal IPs.
> - **Set longer cooldowns:** E.g., 15 minutes instead of 5.
> - **Enable user notifications:** Alert users if their account was locked due to failed attempts.
> - **Combine with 2FA:** Two-Factor Authentication makes brute-force attempts nearly useless.
> - **Use reCAPTCHA:** Combine with Django Defender for extra friction.
> - **Monitor Redis:** Make sure your Defender keys don’t fill up your Redis instance.

### Debug and Development Security
[^1][^22][^23]
Many developers:
- Leave `DEBUG=True` in production.  
- Forget to restrict `ALLOWED_HOSTS`.  
- Keep the default Django admin URL exposed.

These mistakes can:
- Leak stack traces with environment variables.
- Allow **Host header attacks**.
- Make brute-force admin attacks easier.

These configuration helps prevent all of that.

```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']

# Remove server identification
SECURE_SERVER_HEADER = False

# Disable admin in production URLs
# urls.py
if not settings.DEBUG:
    # Change default admin URL
    admin.site.site_url = None
    admin.site.site_header = 'Secure Admin'
```

---

Defending against sophisticated reconnaissance attacks *requires a multi-layered approach* combining **framework-specific hardening**, and more [broad framework security considerations](../../../Docs/broad-framework-security-considerations.md) like **universal security practices**, and **continuous monitoring**.

Django's built-in security features provide a solid foundation, but additional measures are essential to protect against the advanced techniques demonstrated in the video.

The key is to assume that attackers will always find ways to gather information, so the focus should be on minimizing information disclosure, implementing robust authentication and authorization, and maintaining comprehensive monitoring to detect and respond to threats quickly.

Regular security assessments, keeping frameworks updated, and following the **Principle of Least Privilege (POLP)** are fundamental to maintaining a strong security posture against reconnaissance-based attacks across all web application frameworks.

# References
[^1]: https://corgea.com/Learn/django-security-best-practices-a-comprehensive-guid-for-software-engineers
[^2]: https://forum.djangoproject.com/t/truly-separate-subdomain-sessions/40867
[^3]: http://vercara.digicert.com/resources/securing-your-authoritative-dns-server-and-domains
[^4]: https://controld.com/blog/dns-security-best-practices/
[^5]: https://www.digitalocean.com/community/tutorials/how-to-secure-your-django-application-with-a-content-security-policy
[^6]: https://www.stackhawk.com/blog/django-content-security-policy-guide-what-it-is-and-how-to-enable-it/
[^7]: https://django-csp.readthedocs.io/en/latest/configuration.html
[^8]: https://zappycode.com/tutorials/keep-secrets-secret-how-to-hide-sensitive-data-in-django
[^9]: https://github.com/LeeHanYeong/django-secrets-manager
[^10]: https://pypi.org/project/django-encrypted-secrets/
[^11]: https://stackoverflow.com/questions/51635076/which-is-best-practice-to-add-security-headers-for-django-application
[^12]: https://www.stackhawk.com/blog/django-http-strict-transport-security-guide-what-it-is-and-how-to-enable-it/
[^13]: https://stackoverflow.com/questions/65564064/which-is-the-best-way-to-protect-a-django-api
[^14]: https://www.linkedin.com/pulse/django-api-authentication-comprehensive-guide-your-apis-satyakama
[^15]: https://docs.djangoproject.com/en/5.2/howto/static-files/
[^16]: https://www.hostinger.com/tutorials/django-static-files
[^17]: https://forum.djangoproject.com/t/securing-uploaded-files/6723
[^18]: https://www.stackhawk.com/blog/django-path-traversal-guide-examples-and-prevention/
[^19]: https://github.com/advisories/GHSA-9jmf-237g-qf46
[^20]: https://github.com/appsecengineer/django-path-traversal
[^21]: https://github.com/jazzband/django-defender
[^22]: https://www.digitalocean.com/community/tutorials/how-to-harden-your-production-django-project
[^23]: https://docs.djangoproject.com/en/5.2/topics/security/