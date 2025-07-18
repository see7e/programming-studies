---
title: Understanding and Managing Linux DNS Resolution
tags:
  - studies
  - programming
  - troubleshooting
  - linux
  - dns
  - networking
  - systemd-resolved
use: Documentation
languages: 
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [Understanding and Managing Linux DNS Resolution](#understanding-and-managing-linux-dns-resolution)
  - [What Is `/etc/resolv.conf`?](#what-is-etcresolvconf)
  - [The Default `Systemd-Resolved` Behavior](#the-default-systemd-resolved-behavior)
  - [What Happens When You Replace `127.0.0.53` with `8.8.8.8`](#what-happens-when-you-replace-1270053-with-8888)
  - [Why Would Anyone Change the Default?](#why-would-anyone-change-the-default)
  - [How to Fix Systemd-Resolved Instead of Disabling It](#how-to-fix-systemd-resolved-instead-of-disabling-it)
  - [If You Must Bypass Systemd-Resolved Permanently](#if-you-must-bypass-systemd-resolved-permanently)
  - [Take-Home Checklist](#take-home-checklist)
- [References](#references)

</details>

---
# Understanding and Managing Linux DNS Resolution
The `/etc/resolv.conf` file plays a critical role in **how your Linux system translates human-readable domain names** (like `example.com`) into numerical IP addresses that computers use to communicate. This article explains its purpose, how it works in modern distributions, why you might want to change it, and the implications of switching from the default stub resolver (`127.0.0.53`) to an external DNS server like Google’s `8.8.8.8`.

## What Is `/etc/resolv.conf`?
`/etc/resolv.conf` is a text file that **defines how the system resolver library looks up domain names**. It typically contains:
- **`nameserver` entries** — the IP addresses of DNS servers to query.
- **search domains** — suffixes added to unqualified names.
- **options** — resolver behaviors such as timeouts and retries.

**Example:**

```conf
nameserver 8.8.8.8
nameserver 1.1.1.1
search mycompany.local
options timeout:2 attempts:3
```

When you use commands like `ping`, `curl`, or when applications resolve hostnames, *the resolver library consults this file*[^1].

## The Default `Systemd-Resolved` Behavior
Modern Linux distributions often run `systemd-resolved`, which introduces a **local DNS stub resolver** bound to `127.0.0.53`. Here’s how it works:
- Applications send DNS queries to `127.0.0.53:53`.
- `systemd-resolved` *forwards these queries to upstream DNS servers* learned dynamically (via DHCP, VPNs, or configured manually).
- `/etc/resolv.conf` is usually a **symlink** to `/run/systemd/resolve/stub-resolv.conf` containing:
    ```
    nameserver 127.0.0.53
    options edns0
    ```
- This setup provides benefits like:
    - DNS caching.
    - Per-interface DNS configurations (split DNS).
    - DNSSEC validation.
    - Automatic updates when network connections change[^2] [^3].

## What Happens When You Replace `127.0.0.53` with `8.8.8.8`
If you manually edit `/etc/resolv.conf` to:

```
nameserver 8.8.8.8
```

**you bypass `systemd-resolved` entirely**. The resolver library **will now send DNS queries directly** to Google Public DNS instead of using the **stub resolver**.

**Advantages:**  
✅ Immediate troubleshooting for DNS failures.  
✅ Avoids problems with a misconfigured or non-functioning local stub.

**Drawbacks:**  
❌ No DNS caching.  
❌ No per-interface (split) DNS.  
❌ No DNSSEC validation.  
❌ The file can be overwritten by system services like `NetworkManager` or DHCP on reboot unless you make it immutable with `chattr +i` [^4][^5].

## Why Would Anyone Change the Default?
There are several reasons:
1. **Troubleshooting Connectivity**
    - If `ping` or other lookups fail with `127.0.0.53` but work with `8.8.8.8`, this proves `systemd-resolved` cannot reach upstream DNS (e.g., no servers received via DHCP, firewalls blocking port 53, or the service is down)[^6].
2. **Custom or Fixed DNS Requirements**
    - You might want to use a specific public DNS resolver for speed, privacy, or policy compliance.
3. **Firewall or VPN Constraints**
    - Some enterprise VPNs require bypassing local stub resolvers.
4. **Containerized Environments**
    - Docker and Kubernetes sometimes mount their own `/etc/resolv.conf` and expect explicit nameservers[^7].

## How to Fix Systemd-Resolved Instead of Disabling It
If you prefer to **repair** the default configuration:
1. **Restart systemd-resolved and inspect status:**
    ```shell
    sudo systemctl restart systemd-resolved
    resolvectl status
    ```
    Check whether DNS servers are listed.
2. **Manually set DNS servers:**
    ```
    sudoedit /etc/systemd/resolved.conf
    [Resolve]
    DNS=8.8.8.8 1.1.1.1
    FallbackDNS=9.9.9.9
    ```
3. **Restore the symlink:**
    ```shell
    sudo ln -sf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
    sudo systemctl restart systemd-resolved
    ```

## If You Must Bypass Systemd-Resolved Permanently
Be aware this is **not recommended** for laptops or VPN users:
1. Disable systemd-resolved:
    ```shell
    sudo systemctl disable --now systemd-resolved
    ```
2. Remove the symlink and replace with a static file:
    ```shell
    sudo rm /etc/resolv.conf
    echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
    ```
3. Protect it:
    ```shell
    sudo chattr +i /etc/resolv.conf
    ```

## Take-Home Checklist
- **Use `resolvectl status` to verify upstream servers.**
- **Repair `systemd-resolved` if possible** instead of hardcoding DNS.
- **Understand the impact on split-DNS, DNSSEC, and privacy.**
- For troubleshooting, **a temporary switch to `8.8.8.8` is fine**, but consider reverting once resolved.

---

While it's possible to bypass `systemd-resolved`, it’s generally better to fix issues with it rather than disable it. Understanding **how DNS resolution works** in Linux, especially with modern tools like `systemd-resolved`, will help you maintain a *stable* and *secure* networking environment.

# References
[^1] [man7.org: resolv.conf](https://man7.org/linux/man-pages/man5/resolv.conf.5.html)
[^2] [systemd-resolved documentation](https://www.freedesktop.org/software/systemd/man/systemd-resolved.service.html)
[^3] [Arch Linux Wiki: systemd-resolved](https://wiki.archlinux.org/title/Systemd-resolved)
[^4] [Ask Ubuntu: How to permanently change DNS](https://askubuntu.com/questions/1012641/dns-set-to-systemds-127-0-0-53-how-to-change-permanently)
[^5] [ServerFault: Where's my stub-resolv.conf?](https://serverfault.com/questions/1000859/wheres-my-stub-resolve-conf)
[^6] [LinuxQuestions: Why does 127.0.0.53 fail sometimes?](https://www.linuxquestions.org/questions/linux-newbie-8/my-dns-127-0-0-53-a-4175733098/)
[^7] [Docker Docs: DNS services](https://docs.docker.com/config/containers/container-networking/#dns-services)
