---
title: ASP.NET
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
> Starting with a basic C# web application created with `dotnet new webapp` can feel overwhelming if you're new to the ecosystem. Let’s break it down step-by-step.

---

## **Folder and File Structure**

1. **`wwwroot`**:  
   - This is the root folder for serving static files like CSS, JavaScript, images, and more. By default, any file placed here is publicly accessible on the web server.
   
2. **`Pages`**:  
   - Contains Razor Pages (`.cshtml` and `.cshtml.cs` files), which are used to define the UI and related server-side logic.
   - For example, an `Index.cshtml` page defines the homepage content.

3. **`Program.cs`**:  
   - The entry point of the application. It sets up the web server, middleware, and routes.
   
4. **`appsettings.json`**:  
   - Stores configuration settings, such as connection strings, API keys, or custom app settings.
   - You can override these with environment-specific settings.

5. **`obj`** and **`bin`** folders:  
   - **Generated** during build and runtime, these contain compiled application code and dependencies. At start will only be the `obj` folder.

---

## **Understanding `Program.cs`**

### The `Program.cs` file is responsible for setting up and starting your application. Here’s a breakdown of its content:

```csharp
var builder = WebApplication.CreateBuilder(args);
```
Creates a `builder` object to configure the application. It also sets up default configurations like environment settings, logging, and dependency injection.


```csharp
builder.Services.AddRazorPages();
```
Adds **Razor Pages** support to the application. In short, Razor Pages are a simpler alternative to MVC for building dynamic web pages in ASP.NET Core.


```csharp
var app = builder.Build();
```
Builds the app using the [configurations](./builder-configurations.md) specified in the builder.

---

### **HTTP Request Pipeline Configuration**
This section defines how incoming HTTP requests are processed by middleware.

```csharp
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}
```
- Checks if the app is running in a **non-development** environment (e.g., production).
- **`app.UseExceptionHandler("/Error")`**:
  - Configures a default error-handling page (e.g., `/Error`).
- **`app.UseHsts()`**:
  - Enables HTTP Strict Transport Security, forcing secure HTTPS communication.

---

```csharp
app.UseHttpsRedirection();
```
- Redirects all HTTP requests to HTTPS for security.

---

```csharp
app.UseRouting();
```
- Enables endpoint routing to map incoming requests to the appropriate handlers.

---

```csharp
app.UseAuthorization();
```
- Adds authorization middleware to enforce access control. If your app doesn’t have authentication yet, this won't do much.

---

### **Static Assets and Razor Pages**

```csharp
app.MapStaticAssets();
```
- Maps the `wwwroot` folder to serve static files like CSS, JS, and images.

```csharp
app.MapRazorPages()
   .WithStaticAssets();
```
- Maps the Razor Pages defined in the `Pages` folder to routes and ensures static assets required by these pages are accessible.

---

```csharp
app.Run();
```
- Starts the application and listens for incoming requests.

---

## **What Happens When You Run This App?**

1. **Startup**: 
   - The application runs on a local server.
   - It sets up middleware to handle requests.

2. **Static Files**:
   - Any requests for files like `/css/site.css` are served directly from the `wwwroot` folder.

3. **Dynamic Pages**:
   - Razor Pages handle requests like `/Index` or `/About`.

4. **HTTPS**:
   - Ensures secure communication by redirecting HTTP requests to HTTPS.

---

This structure is designed to be modular and scalable. As you progress, you'll dive deeper into:
- **Dependency Injection**: Managing services like databases.
- **Middleware**: Customizing request-handling logic.
- **Routing**: Building complex URL patterns.

