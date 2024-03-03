---
title: Python - Django
tags: studies, programação
use: Documentation
languages: Python
dependences: Django
---

<details> <summary>Table of Contents 🔖</summary>

- [Django](#django)
  - [The root folders](#the-root-folders)
  - [Django configurations (`setup/`)](#django-configurations-setup)
    - [`settings.py`](#settingspy)
    - [`urls.py`](#urlspy)
    - [`asgi.py` and `wsgi.py`](#asgipy-and-wsgipy)
  - [Application (`app_name/`)](#application-app_name)
    - [App `apps.py`](#app-appspy)
    - [App `urls.py`](#app-urlspy)
    - [App `views.py`](#app-viewspy)
    - [App `models.py`](#app-modelspy)
    - [App `admin.py`](#app-adminpy)
    - [App `forms.py`](#app-formspy)
  - [Templates (`templates/`)](#templates-templates)
    - [Base layout (`base.html`)](#base-layout-basehtml)
    - [Child layout (`child.html`)](#child-layout-childhtml)
    - [Custom tags/filters (`templatetags/`)](#custom-tagsfilters-templatetags)
  - [Tests](#tests)

</details>

---

# Django

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It is a free and open-source framework, which follows the model-template-views architectural pattern. Django's primary goal is to ease the creation of complex, database-driven websites.


## The root folders

In the projects which I've worked on, the file structure is usually like this:

```
project_name/
    manage.py
    templates/...
    static/...
    media/...
    utils/...
    setup/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    app_name/
        templates/...
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
    ...
```


## Django configurations (`setup/`)

### `settings.py`

This file is the main configuration file for the Django project. It contains the settings for the project, such as the database configuration, the installed apps, the middleware, the static and media files, the internationalization, the authentication, the logging, and so on.

> [!INFO]
> For the full list of settings and their values, see https://docs.djangoproject.com/en/4.2/ref/settings/

```python
# Django Application definitions

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    # ...,
]

INSTALLED_APPS = [
    # django modules
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party modules
    'debug_toolbar',
    'crispy_forms',
    'crispy_bootstrap5',
    'widget_tweaks',

    # internal modules
    # ...
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

ROOT_URLCONF = 'setup.urls'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'setup.wsgi.application'
```

For the static files it will depend on how we build the url calls in the templates we can point the to a single direction, using `python manage.py collectstatic` to join all the statics in a single folder before the deployment.

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/' # or staticfiles
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # or staticfiles
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"), # or staticfiles
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

In most cases we used PostgreSQL as the database provider, so the database settings are usually like this:

```python
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'name',
        'USER': 'user@domain.com',
        'PASSWORD': 'pass',
        'HOST': 'hostIP',
        'PORT': 'port',
        # 'CONN_MAX_AGE': 600, # optional
    },
}

# PostgreSQL URI-style connection string
DATABASE_URL = 'postgresql://uri'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
```
For authentication, had some experience with LDAP Auth because of the company's policy, due to the usage of the Active Directory.

```python
import ldap
from django_auth_ldap.config import LDAPSearch

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model for LDAP authentication
AUTH_USER_MODEL = 'app_auth.CustomUser'

# Settings for LDAP authentication
AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_SERVER_URI = 'ldap://10.0.0.4:389'
AUTH_LDAP_BIND_DN = 'CN=cn_name,OU=ou_name,DC=dc_name'
AUTH_LDAP_BIND_PASSWORD = 'pass'
AUTH_LDAP_USER_SEARCH = LDAPSearch('DC=dc_name,', ldap.SCOPE_SUBTREE, '(mail=%(user)s)') # to search the users

# Set up the basic group parameters
AUTHENTICATION_BACKENDS = [
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
]
```

In case of Language settings there's no mistry, just some default settings for the date and time formats, and the range of years for the date pickers.

```python
from datetime import datetime

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DATE_FORMAT = 'd/m/Y'

DATE_INPUT_FORMATS = [
    '%Y-%m-%d',  # Default format
    '%d/%m/%Y',  # Portuguese format
]

CURRENT_DAY = datetime.now().day
DAY_DEFAULT = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]


CURRENT_MONTH = datetime.now().month
MONTHS_DEFAULT = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June":6, "July": 7, "August": 8, "September": 9,
    "October": 10, "November": 11, "December": 12
}

CURRENT_YEAR = datetime.now().year
YEAR_RANGE = range(2015, CURRENT_YEAR)
```

### `urls.py`

The `urls.py` file is `pretty simple, it contains the URL patterns for the project, in order that the requests are directed to the correct urls files of each app.

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls), # default django admin pages
    path('', include('app_auth.urls')), # root route
    path('app/', include('app_name.urls', namespace='app')),
]
```

The `urlpatterns` lists the routes directing to the admin pages, the root route, and the apps routes. Generally, we use root route to lead to the login page, this ensures that the user is always authenticated before accessing the applications. 

This list can be handled with conditional statements, for example, if the context where the applocation is running is development, the `debug_toolbar` (a third party module that I'll talk about later) is included in the urlpatterns.

```python
# Add debug toolbar to urlpatterns
if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    # Show debug toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

    # Add media files to urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
```

### `asgi.py` and `wsgi.py`

These files are used to deploy the application in a server. The `asgi.py` file is used for asynchronous servers, and the `wsgi.py` file is used for synchronous servers. By default, the files looks like this:

```python
import os

from django.core.asgi import get_asgi_application # or get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

application = get_asgi_application() # or get_wsgi_application
```


## Application (`app_name/`)

In this there are some files that usually appear in the applications (such as: `admin.py`, `apps.py`, `models.py`, `tests.py`, `views.py` and `urls.py`), but we can create any other file following the purpose and the logic of the application.

### App `apps.py`

This file is used to configure the application, and it's used to define the name of the application. By default, the file looks like this:

```python
from django.apps import AppConfig


class AppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_name'
```


### App `urls.py`

This follows the same logic as the `urls.py` file in the `setup/` folder, but it contains the URL patterns for the app. So there's some differences in the way the routes are handled.
Usually we'll have more routes in here as much as the number of the views in the app or the number of the requests received through the templates. For example, if we have a CRUD application, we'll have 5 routes: one for the index, one for the create, one for the update, one for the delete and one for the detail.

```python
from django.urls import path

from . import views

app_name = 'app_name'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('detail/<int:pk>/', views.detail, name='detail'),
]
```

Some points to give notice:

- The `app_name` is used to create a namespace for the app, so we can use the `{% url 'app_name:index' %}` in the templates to call the index route. This improves the readability and the maintainability of the code.
- In the string patterns we see `<int:pk>`, this is a way to pass a parameter (through the URL) to the view. In this case, the `pk` is the primary key of the object that we want to manipulate (it's a convention) and the `int` is the type of the parameter (in this case, an integer). We can use other types, such as `str`, `slug`, `uuid` and so on.
    - `slug` is a string that contains only letters, numbers, underscores or hyphens, and it's used to create a URL that is more friendly to the search engines.
    - `uuid` is a string that contains 32 characters, and it's used to create a URL that is unique and hard to guess.


### App `views.py`

The views are the functions that handle the requests and return the responses. They are the core of the application, and they are responsible for the logic of the application. The views are the bridge between the templates and the models, and they are the ones that make the application work.
Usually, the views are divided into two types: the **class-based** views and the **function-based** views. The **class-based** views are used when we have a lot of logic to handle, and the **function-based** views are used when we have a simple logic to handle.

```python
def create(request, day=CURRENT_DAY, month=CURRENT_MONTH, year=CURRENT_YEAR):
    if day is None or month is None or year is None:
        return custom_error_response(400)

    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            context = 'create' # could be a query to the database

            valid, msg = validate_info(context, form.cleaned_data)
            if not valid:
                return custom_error_response(400, msg)
            
            form.save()
            return custom_success_response(201, f"Added in {form.cleaned_data['date']}")
        else:
            return custom_error_response(400, form.errors)

    # if not sending a POST request, create a new form
    date = datetime(year, month, day).strftime('%Y-%m-%d')
    form = CreateForm(initial={'employee': request.user.id, 'date': date, 'status': "pending"})
    
    return render(request, 'form.html', {'form': form, 'date': date})
```

A not so positive point about using **function-based** views is that we have to handle the requests and the responses manually, and this can lead to a lot of code repetition. So generally I add some decorators or even some helper functions to handle the requests and the responses. Appart from that there's also some points worth to mention:

- this example uses other parameters in the function signature, compared to the one listed in the urls examples, because I wanted the first one to be more generic and the second one to be more specific.
- the `CreateForm` is an instance of a form class, defined in the `forms.py` file, and it's used to handle the data that comes from the request.
- talking about the helper functions:
    - the `validate_info` is a helper function that I created to validate the data that comes from the form, and it returns a boolean and a message.
    - the `custom_error_response` and the `custom_success_response` are helper functions that I created to handle the responses, and they return a response with a status code and a message. This is entirely optional, but I like to use HTMX triggers and events, and this "toast" is based on that:

        ```python
        def custom_error_response(status_code: int, msg: str = None, **hx_triggers) -> HttpResponse:
            if msg:
                message = f"[ERROR|{status_code}] {msg}"
            else:
                message = f"[ERROR|{status_code}]"

            hx_triggers.update({
                "showMessage": message
            })

            return HttpResponse(
                status=status_code,
                headers={'HX-Trigger': json.dumps(hx_triggers)}
            )


        def custom_success_response(status_code: int, msg: str, instance=None, dates=None, **hx_triggers) -> HttpResponse:
            if instance and dates or instance:
                message = f"[CREATED|{status_code}] {msg}"
            else:
                message = f"[ACCEPTED|{status_code}] {msg}"

            hx_triggers.update({
                "showMessage": message
            })

            return HttpResponse(
                status=status_code,
                headers={'HX-Trigger': json.dumps(hx_triggers)}
            )
        ```

        An interesting feature of these funtions is that we have the default events emmited but we can add how many as we want.
        We still need some JS code to display the message in the front-end, but still uses some HTMX:

        ```javascript
        ;(function () {
            const toastElement = document.getElementById("toast")
            const toastBody = document.getElementById("toast-body")
            const toast = new bootstrap.Toast(toastElement, { delay: 3000 })

            htmx.on("showMessage", (e) => {
                statusCode = e.detail.value.split(" ")[0].split("|")[1]

                if (statusCode.startsWith("2") || statusCode.startsWith("3")) {
                toastElement.classList.remove("bg-danger-subtle", "bg-warning-subtle")
                toastElement.classList.add("bg-success-subtle") // green
                } else if (statusCode.startsWith("4") || statusCode.startsWith("5")) {
                toastElement.classList.remove("bg-success-subtle", "bg-warning-subtle")
                toastElement.classList.add("bg-danger-subtle") // red 
                } else {
                toastElement.classList.remove("bg-success-subtle", "bg-danger-subtle")
                toastElement.classList.add("bg-warning-subtle") // yellow
                }
                toastBody.innerText = e.detail.value
                toast.show()
            })
        })()
        ```

        And the HTML code:

        ```html
        <!-- Empty toast to show the message -->
        <div class="toast-container position-fixed top-0 end-0 p-3">
            <div id="toast" class="toast align-items-center text-white border-0" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="d-flex">
                    <div id="toast-body" class="toast-body"></div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        </div>
        ```

The example of `create` function uses the `django.shortcuts.render` to load the template in the delivery of the request, but other possibility is to pair the call of the route (in a GET or POST) with a HTMX trigger, and return a JSON response with the data that we want to display in the front-end. This is a good practice when we want to avoid the page reload, and it's a good practice when we want to use the HTMX library.

```python
def update_obj_data(request, *args, **kwargs) -> JsonResponse:
    select_model_field = kwargs.get('select_model_field')
    obj_list = list(Object.objects.filter(field_a=select_model_field).values()) # can exclude based on some condition too

    return JsonResponse({'obj_data': obj_list})
```

> This where used as a call point to HTMX request to deliver the data in a select chain input in the front-end. I'll talk about this in the `templates` section.


### App `models.py`

This is one of the most important files in the application, because it contains the models of the application. The models are the classes that represent the database tables, and they are the ones that make the application persistent (the ones that make possible to store the data in the database). I'll use as example the `CustomUser` model, that I used as example to handle the LDAP authentication.

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    supervisor = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='supervised')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name}-{self.last_name}-{self.email}"
```

In this example, we have a class that inherits from (django's) `AbstractUser` class, and we have some fields that are specific to the application.
But why use the `AbstractUser` and not the `User` class? Because the first one  is a class that contains the basic fields that we need to create a user, and it's a class that we can customize. The `User` class is a class that contains the basic fields that we need to create a user, but it's a class that we can't customize. So, if we want to create a user with some specific fields, we have to create a class that inherits from the `AbstractUser` class.

Following this principle we can add as many fields as we want, and we can create as many models as we want. The fields can be of different types, such as `CharField`, `IntegerField`, `BooleanField`, `DateField`, `DateTimeField`, `ForeignKey`, `ManyToManyField`, and so on. We can also add some methods to the class, and we can override some methods of the class.

> [!INFO]
> The `ForeignKey` is used to create a relationship between two tables (a parent table and a child), and the `ManyToManyField` is used to create a relationship between many tables. The `ForeignKey` is used to create a one-to-many relationship, and the `ManyToManyField` is used to create a many-to-many relationship.

Talking about **Methods**, one that we already saw is the `__str__` method, that is used to return a string representation of the object. This is a good practice to use, because it makes the object more readable in the admin pages, and it makes the object more readable in the templates. Also, when filtering (querying) the objects, the `__str__` method is used to return the string representation of the object.


### App `admin.py`

This file is used to register the models in the admin pages, and it's used to customize the admin pages.

```python
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'last_login')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    actions = ['update_users_from_ldap_action']

    def update_users_from_ldap_action(self, request, queryset):
        update_users_from_ldap()
        self.message_user(request, "Users updated successfully.")

    update_users_from_ldap_action.short_description = "Update users from LDAP"
admin.site.register(CustomUser, CustomUserAdmin)
```

In this example, we have a class that inherits from (django's) `UserAdmin` class, and we have some fields that are specific to the application. We can add as many fields as we want, and we can create as many classes as we want. The fields can be of different types, such as `list_display`, `search_fields`, `readonly_fields`, `actions`, and so on. We can also add some methods to the class, and we can override some methods of the class.

We can also modify or create a custom admin page over the default ones, for example, to add some custom actions (as I did in the example above calling `update_users_from_ldap` function). We can modify the forms for editing the objects, in this example we've added a field to add the users in a group (by the group form), reversing the default behavior of admin (adding the users in a group by the user form):

```python
admin.site.unregister(Group) # Unregister the original Group admin.
class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    filter_horizontal = ['permissions',] # Filter permissions horizontal as well.
admin.site.register(Group, GroupAdmin)
```

But for doing this we need the `GroupAdminForm` from the `forms.py`.

> [!NOTE]
> I didn't had the time yet to create a custom admin page, but I'm planning to do it in the future. I think that it's a good practice to use, because it makes the admin pages more readable, and it makes the admin pages more usable.


### App `forms.py`

This file is used to create the forms of the application, and it's used to handle the data that comes from the request. The forms are the classes that represent the HTML forms, and they are the ones that make the application interactive. The forms are the bridge between the views and the templates, and they are the ones that make the application dynamic.

Continuing with the example of the Group admin page:

```python
# Create ModelForm based on the Group model.
class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []
    
    users = forms.ModelMultipleChoiceField(
        label=('Users'),
        queryset=CustomUser.objects.all(), 
        required=False,
        widget=FilteredSelectMultiple('users', False),
    )
    
    
    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()
    
    
    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])
    
    
    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance
```

In this case the purpose was only to add in the default form the `users` field. And the methods used (`__init__`, `save_m2m` and `save`) are used to handle the data that comes from the request, and they are the ones that make the form dynamic.

- The `__init__` method is used to initialize the form, and it's used to populate the form with the data that comes from the request.
- The `save` method saves the information by calling the `save_m2m` method, and returns the `instance` of the object.
- The `save_m2m` method defines the many-to-many relationship between the `Group` and the `CustomUser` models, setting the users in the group.

Others possibilities for the forms involves what we are used to see, in this case we have a form to create specific object:

```python
class SpecificBaseForm(forms.ModelForm):
    class Meta:
        model = SpecificModel
        fields = '__all__'

    # Some definitions

    REQUIRED_FIELDS = [
        # ...
    ]

    READ_ONLY_FIELDS = [
        # ...
    ]

    # The fields of the form
    date_field = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }),
    )

    select_model_field = forms.ModelChoiceField(
        queryset=OtherModel.objects.exclude(field='value'),
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }),
    )

    comment_field = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter comment',
                'class': 'form-control',
            }),
    )

    state_field = forms.ChoiceField(
        choices=SpecificModel.STATE,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'default': 'IN_PROGRESS'
            }),
    )

    # The methods of the form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_class = 'modal-content'
        self.helper.layout = self.get_layout()

        self.set_required_fields()
        self.set_readonly_fields()

    def get_layout(self): # acts like the builder
        return Layout(
            Div(
                *self.get_fields(),
                css_class='mt-3',
            ),
            ButtonHolder(
                HTML(
                    """
                    <div class="modal-footer">
                        {% if form.instance.pk %}
                            <button type="button" class="btn btn-danger" hx-post="{% url 'worktime:remove' pk=form.instance.pk %}">Remove</button>
                            <span class="flex-grow-1"></span>
                        {% endif %}
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                        <button type="submit" class="btn btn-primary">Save</button>
                    </div>
                    """
                ),
            ),
        )

    def get_fields(self):
        return [
            'date_field',
            'select_model_field',
            HTML( # this field behavior is handled by HTMX and related to the JsonResponse of update_obj_data() in views
                """
                <div id="div_id_select_object_field" class="mb-3">
                    <label for="{{ form.select_object_field.id_for_label }}" class="form-label">Modal Object field</label>
                    <select name="select_object_field" class="form-select" required id="id_select_object_field"
                        {% if "some_context" in form_context %}disabled{% endif %}
                    >
                        <div class="menu" id="select_object_field-data-box">
                        {% if instance %}
                            <option value="{{ instance.select_object_field.id }}" selected>{{ instance.select_object_field }}</option>
                        {% else %}
                            <option value="" selected>---------</option>
                        {% endif %}
                        </div>
                    </select>
                    <div class="invalid-feedback">{{ form.select_object_field.errors|first }}</div>
                </div>
                """
            ),
            'comment_field',
            'state_field',
        ]

    def set_required_fields(self):
        for field_name, field in self.fields.items():
            field.required = True if field_name in self.REQUIRED_FIELDS else False

    def set_readonly_fields(self):
        for field_name, field in self.fields.items():
            field.widget.attrs['readonly'] = True if field_name in self.READ_ONLY_FIELDS else False
```

By heritance, we can create variations of the base form, for example is the form is accessed by some administrator, we can alter the form but keeping the same base:

```python
class SpecificAdminForm(BaseWorkTimeForm):
    multiple_date_selctor = forms.CharField(
        label='Date Range',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['team'].queryset = CustomUser.objects.filter(supervisor=self.user.id)

    def get_layout(self):
        layout = super().get_layout()
        multiple_date_selctor_html = """
                    <div id="dateSelectorDiv" style="display:none" class="my-4">
                        <div id="multiDateSelector"></div>
                        <div class="mt-3">
                            <div id="applySelection" class="btn btn-primary btn-sm">Apply Selection</div>
                            <div id="clearSelection" class="btn btn-secondary btn-sm">Clear Selection</div>
                        </div>
                    </div>
                """

        # Add the date_html to the layout
        layout.fields.insert(
            0, # index of field placement in the layout
            Div(
                HTML(multiple_date_selctor_html),
                'multiple_date_selctor' # field name
            )
        )
        return layout

    def get_fields(self):
        return super().get_fields()

    def update_field_attribures(self):
        super().set_readonly_fields()
        super().set_required_fields()

        # Can override the fields attributes
        self.fields['select_model_field'].required = True

        # Can override the fields widgets attributes
        self.fields['date_field'].widget = forms.HiddenInput()
        self.fields['comment_field'].widget = forms.HiddenInput()
        self.fields['state_field'].widget = forms.HiddenInput()
```

As always, there's some points to give notice:

- In the `SpecificAdminForm` we have a new field, the `multiple_date_selctor`, and we have a new method, the `update_field_attribures`, that is used to update the fields attributes based on the parent `set_readonly_fields` and `set_required_fields` methods, called by the `super()` method (that calls the parent class).
- The `get_layout` method this time is used to call for the main fields (from the parent class) in the form and add the `multiple_date_selctor` which is a custom HTML to handle the date range selection.


## Templates (`templates/`)

In this case we can have the templates used by the project root as base layouts and the ones used by the apps as extensions of theese layouts. The templates are normal htmlx files that could inport javascript and css code, but in the Django there's an addition named `Django Template Language`, an incrementation of Jinja2, that allows us to use some logic and some variables in the templates.


### Base layout (`base.html`)

Depending on the usage we usually have a base layout that is used by the root of the project, and it's used to create the structure of the pages. This is a simple example of a base layout:

> In this case comes the decision to whether use the static files in the `static/` or the ones collected in the `staticfiles/` folder. Other option is to use a CDN to import the files. In this case I'm using a combination of the static folder and the CDN.

In first place, as said before, is to load the static information and to save time I usually work with Bootstrap and Fontawesome, so I load the static files and the CDN for the icons. The `header_links` and `header_scripts` are used to add some custom links and scripts in the header of the page.

```html
{% load static %}

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#712cf9">
    <link rel="icon" type="image/icon" href="{% static 'images/logo.ico' %}">
    
    <title>MyApp - {% block title %}{% endblock %}</title>

    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-..." crossorigin="anonymous">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.2/font/bootstrap-icons.css" rel="stylesheet"
        integrity="sha384-..." crossorigin="anonymous">
    <link href="https://cdn.jsdelivr.net/npm/@docsearch/css@3" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="{% static 'css/styles.css' %}" rel="stylesheet">
    {% block header_links %}{% endblock %}
    
    <!--- Fontawesome -->
    <script src="https://kit.fontawesome.com/d45e7e578e.js" crossorigin="anonymous"></script>

    {% block header_scripts %}{% endblock %}
</head>
```


For the body, and in this example we use a traditional division of the page in header with a navbar header, a sidebar with the menus and the main section with the content of the page, where the child layouts will be included. The `theme.html` is used to handle the color mode of the page, and the `toast` is used to show the messages in the front-end.

```html
<body class="vh-100">

{% include "theme.html" %}

<!-- NAVBAR HEADER -->
<header class="navbar sticky-top bg-dark flex-md-nowrap p-3 shadow" data-bs-theme="dark">
    <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
        <a href="/home" class="d-flex align-items-center mb- mb-lg-0  text-white text-decoration-none">
            <img type="image/png" src="{% static 'images/logo.png' %}" alt="Logo" height="50">
        </a>
    </div>
    <div class="d-flex flex-wrap align-items-center justify-content-end justify-content-lg-start">
        <div class="dropdown me-4">
            <a href="#" class="d-flex align-items-center text-white text-decoration-none dropdown-toggle"
               data-bs-toggle="dropdown" aria-expanded="false">
               
                {% if request.user.photo %}
                <img src="{{ request.user.photo.url }}" alt="User Photo" width="25" height="25"
                    class="rounded-circle me-2" style="object-fit: cover;">
                
                {% else %}
                <img src="{% static 'images/default.jpg' %}" alt="User Photo" width="25" height="25"
                    class="rounded-circle me-2" style="object-fit: cover;">
                {% endif %}

                <strong>{{ request.user.name }}</strong>
            </a>
            <ul class="dropdown-menu dropdown-menu-dark text-small shadow">
                <li><a class="dropdown-item" href="/profile/">Profile</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="/logout/">Logout</a></li>
            </ul>
        </div>
    </div>
</header>

<!-- toast example to show the message -->

<!-- MAIN SECTION -->
<main class="container-fluid" style="height: 90vh;">
    <div class="row">

        <!-- SIDEBAR MENUS -->
        <div class="col-2 p-3 position-fixed vh-100 shadow text-bg">
            <ul class="list-unstyled ps-0">
                <li>
                    <button class="btn btn-toggle d-inline-flex align-items-center rounded border-0 collapsed">
                        <a href="/" class="link-body-emphasis d-inline-flex text-decoration-none rounded">Home Page</a>
                    </button>
                </li>
                {% for menu_item in request.session.user_menu %}
                    {% with menu_id=menu_item.menu|lower|slugify %}
                    <li class="mb-1">
                        <button class="btn btn-toggle d-inline-flex align-items-center rounded border-0 collapsed"
                                data-bs-toggle="collapse" data-bs-target="#{{ menu_id }}" aria-expanded="false">
                            {{ menu_item.menu }}
                        </button>
                        <div class="collapse" id="{{ menu_id }}">
                            <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                {% for submenu_item in menu_item.submenus %}
                                <li>
                                    <a href="/{{ submenu_item.url }}"
                                    class="link-body-emphasis d-inline-flex text-decoration-none rounded">
                                        {{ submenu_item.submenu }}
                                    </a>
                                </li>
                                {% endfor %}
                            </ul>
                        </div>
                    </li>
                    {% endwith %}
                {% endfor %}
            </ul>
        </div>
        <!-- /SIDEBAR MENUS -->

        <!-- Childs -->
        <section class="ms-sm-auto col-10 px-md-4 overflow-auto" style="height: 90vh;">
            {% block main_section %}{% endblock %}
        </section>
        <!-- /Childs -->
    </div>
</main>
<!-- /MAIN SECTION -->
```

Other important element to give notice is that in the sidebar, the menus are created based on the user session, and the `menu_item` and `submenu_item` are objects that are created based on the user permissions. This is a good practice to use, because it makes the menus more dynamic, and it makes the menus more usable.

For the footer we have the scripts that are used to handle the behavior of the page, and the `footer_scripts` is used to add some custom scripts in the footer of the page.

```html
<footer>
    <script src="{% static 'js/theme.js' %}"></script>
    
    <!-- Bootstrap -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <!-- jQuery / jQuery UI -->
    <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
    <link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
    <!-- HTMX -->
    <script src="https://unpkg.com/htmx.org@1.9.10/dist/htmx.js"></script>
    <script type="text/javascript" src="{% static 'js/toast.js' %}"></script>

    {% block footer_scripts %}{% endblock %}
</footer>
</body>
</html>
```


### Child layout (`child.html`)

This file could be located in any app folder, and it's used to extend the base layout. The child layout is used to create the content of the pages, and it's used to create the structure of the pages. This is a simple example of a child layout:

```html
{% extends "base.html" %}

{% load static %}
{% load crispy_forms_tags %}

{% block title %}Child Page{% endblock %}

{% block header_links %}{% endblock %}
{% block header_scripts %}{% endblock %}

{% block main_section %}
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">
                <h1 class="mt-4">Child Page</h1>
                <p class="lead">This is a child page.</p>
            </div>
        </div>
    </div>
{% endblock %}

{% block footer_scripts %}{% endblock %}
```

> [!INFO]
> We can also directly call a child by the `{% include "other_child.html" %}` in any portion of the page, this helps to avoid code repetition and to keep the code more organized.

### Custom tags/filters (`templatetags/`)

Django has some [built-in](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/) tags and filters, some of them were used in the past examples such as conditionals (`if`, `else`, `endif`), loops (`for`, `endfor`), or related to django forms (`csrf_token`), or to handle the files and paths (`include`, `load`, `static`, `url`). But we can create our own tags and filters to handle some specific logic in the templates.

For example, we can create a custom tag to handle the color mode of the page, and we can create a custom tag to handle the messages in the front-end. This is a simple example of a custom tag:

```python
from django import template

register = template.Library()

@register.filter(name='get_theme') # if tag, use @register.tag
def get_theme(request):
    if request.session.get('theme') == 'dark':
        return 'dark'
    return 'light'
```
The difference between a tag and a filter is that the tag is used to create a block of code, and the filter is used to create a function that returns a value. In this case, the `get_theme` filter is used to return the value of the theme, and it's used to create a block of code that changes the color mode of the page.

To use a custom filter in the templates, we have to load the custom filter in the template, and we have to call the custom filter in the template. This is a simple example of how to use the custom filter:

```html
{% load get_theme %}
{{ request|get_theme }}
```

To use the custom tag in the templates, we have to load the custom tag in the template, and we have to call the custom tag in the template. This is a simple example of how to use the custom tag:

```html
{% load get_theme %}
{% get_theme request %}
```

> [!INFO]
> The custom filter functions can only accept up to one argument, and the argument can be any type of data (string, integer, float, boolean, list, dictionary, and so on). Can return any type of data (string, integer, float, boolean, list, dictionary, and so on).


## Tests

The tests are used to test the application, and they are used to ensure that the application works as expected. The tests are the classes that represent the test cases, and they are the ones that make the application reliable. The tests are the bridge between the development and the production, and they are the ones that make the application stable.

To implement some tests there's some classes and methods that we can use, such as:

- `TestCase`: a class that contains the test cases, and it's used to create the test cases.
- `setUp`: a method that is used to set up the test cases, and it's used to create the test cases.
- `tearDown`: a method that is used to tear down the test cases, and it's used to destroy the test cases.
- `assertEqual`: a method that is used to compare the expected result with the actual result, and it's used to test the application.
- `assertNotEqual`: a method that is used to compare the expected result with the actual result, and it's used to test the application.
- `assertIn`: a method that is used to compare the expected result with the actual result, and it's used to test the application.
- `assertNotIn`: a method that is used to compare the expected result with the actual result, and it's used to test the application.

This is a simple example of a test case:

```python
from django.test import TestCase

class TestCustomUserCreation(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email = 'test@mail.com',
            first_name = 'User',
            last_name = 'Test',
            is_active = True,
            supervisor = None,
        )
    
    def test_user_creation(self):
        self.assertEqual(self.user.email, '
        self.assertEqual(self.user.first_name, 'User')
        self.assertEqual(self.user.last_name, 'Test')
        self.assertEqual(self.user.is_active, True)
        self.assertEqual(self.user.supervisor, None)
```