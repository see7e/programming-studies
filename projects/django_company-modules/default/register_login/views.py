from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import CustomUser
from .forms import LoginForm, RegisterForm, UpdateCustomUserForm
from .utils import update_sidenav


@login_required
@update_sidenav
def index(request):
    # For now, the index has the same content as the dashboard
    return render(request, "dashboard.html")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            # Create a new user
            user = CustomUser.objects.create_user(
                username=email, email=email, password=password
            )

            # Log the user in
            login(request, user)

            # Render the index page
            return redirect("register_login:home")
    else:
        form = RegisterForm()

    return render(request, "register_login.html", {"form": form, "register": True})


def usr_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a specific page after successful login
                return redirect("register_login:home")
            else:
                # Authentication failed
                error_message = "Invalid email or password."
                print(error_message)
                context = {"form": form, "error_message": error_message}
                return render(request, "register_login.html", context)
    else:
        form = LoginForm()

    return render(request, "register_login.html", {"form": form})


def usr_logout(request):
    # Log the user out
    logout(request)

    # Redirect to the login page
    return redirect("register_login:login")


@login_required
def usr_profile(request):
    """Renders the profile page if the user is logged in. Otherwise, redirects them to the login page."""
    user = request.user
    if request.method == "POST":
        return redirect("register_login:profile_edit")
    else:
        form = UpdateCustomUserForm(instance=user)
        context = {"user": user, "form": form}
        return render(request, "profile.html", context)


@login_required
def usr_profile_edit(request):
    """Renders the profile edit page for the logged-in user."""
    user = request.user
    if request.method == "POST":
        form = UpdateCustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("register_login:profile")
    else:
        form = UpdateCustomUserForm(instance=user, initial={"edit": True})
        context = {"user": user, "form": form}
        return render(request, "profile.html", context)


# TODO: replace django messaging with the toast
# TODO: add photo visualization in the templates
# @login_required
# def handle_uploaded_photo(request):
#     """
#     Handle the uploaded photo.
#     """
#     # Get request info
#     photo = request.FILES.get('photo')
#     user = request.user

#     # Check if a file was selected
#     if photo:
#         # Check if the file extension is valid
#         if '.' in photo.name and photo.name.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}:
#             # Resize and save the image
#             file_path = resize_and_save_image(photo, user)
#             if file_path:
#                 # Update the path in the database
#                 user.photo = file_path
#                 user.save()
#                 messages.success(request, 'Photo added successfully')
#             else:
#                 return redirect(request.path)
#         else:
#             messages.error(request, 'Invalid file extension')
#             return redirect(request.path)
#     else:
#         messages.error(request, 'No file selected')
#         return redirect(request.path)
