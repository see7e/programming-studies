---
title: Basic builder configurations of ASP.NET
tags: studies, programming, dotnet
use: Documentation
languages: C#
dependences: ASP.NET
---

<details> <summary>Table of Contents 🔖</summary>

- []

</details>

---

> [!NOTE]
> The `WebApplication.CreateBuilder(args)` method sets up some essential configurations for your application. These are built-in defaults that help you get started quickly with ASP.NET Core. Here's a breakdown of the basic configurations provided by the builder:

---

# Configurations

## 1. **Application Host Configuration**
The builder sets up settings related to how your app is hosted.

- **Environment Variables**:  
  - Determines the runtime environment (e.g., Development, Production, or Staging) using the `ASPNETCORE_ENVIRONMENT` variable.
  - Accessed via `builder.Environment.IsDevelopment()` or `builder.Environment.EnvironmentName`.

- **Command-Line Arguments**:  
  - Command-line parameters (`args`) passed during the application startup are processed.

- **Kestrel Web Server**:  
  - Configures the internal Kestrel server (used for handling HTTP requests) with default settings.


## 2. **Configuration System**
The builder sets up a hierarchical configuration system using providers like:
- **`appsettings.json`**:
  - Reads key-value pairs from `appsettings.json` and `appsettings.{Environment}.json` (if it exists, e.g., `appsettings.Development.json` for the Development environment).

- **Environment Variables**:
  - Reads environment-specific settings prefixed with `DOTNET_` or `ASPNETCORE_`.

- **Command-Line Arguments**:
  - Overrides settings from configuration files or environment variables.

This configuration system is accessible via `builder.Configuration`.

---

### 3. **Logging**
Logging is pre-configured to capture application events. The builder integrates:
- **Console Logging**:
  - Displays logs in the terminal or command prompt.
- **Debug Logging**:
  - Writes logs to the Debug window in development tools.
- **Event Source Logging**:
  - For diagnostic tools.

You can customize logging settings using `builder.Logging`.

---

### 4. **Dependency Injection Container**
The builder creates a **Service Collection**, a central place to register and manage dependencies for your app.

Example:
- The line `builder.Services.AddRazorPages();` registers Razor Pages into the service collection.
- Other services, such as database contexts, logging providers, and authentication handlers, are also registered here.

---

### 5. **Middleware Pipeline**
The builder pre-configures middleware components that you can add to the HTTP request pipeline. For example:
- HTTPS redirection.
- Static file handling.
- Routing.

These are managed in the `Program.cs` file with `app.UseXyz()` calls.

---

### 6. **Routing System**
Routing is pre-configured to handle incoming requests.
- You can add Razor Pages, API controllers, or custom endpoints.
- Routes are managed by the `UseRouting()` middleware.

---

### 7. **HTTPS**
HTTPS is enabled by default in Development and Production environments. The builder configures:
- Automatic redirection from HTTP to HTTPS (`app.UseHttpsRedirection()`).
- Support for the HSTS protocol in Production (`app.UseHsts()`).

---

### **How to Access These Configurations**

- **Environment**:  
  ```csharp
  var environment = builder.Environment.EnvironmentName; // e.g., "Development"
  ```

- **Configuration Values**:  
  ```csharp
  var someValue = builder.Configuration["KeyName"];
  ```

- **Logging**:  
  ```csharp
  builder.Logging.AddConsole();
  ```

---

These default configurations make ASP.NET Core flexible and powerful, giving you sensible defaults for most scenarios while allowing extensive customization as your application grows.
