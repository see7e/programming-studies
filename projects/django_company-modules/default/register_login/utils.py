import time


def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()

        print(f"Function {func.__name__} took {end - start} seconds to run")
        return value

    return wrapper


from functools import wraps
from collections import defaultdict
from django.shortcuts import render
from django.db.models import Q
from .models import Menu, CustomUser


def update_sidenav(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        # print("Updating sidenav menus...")
        # Query for the side menu
        menu_data = (
            Menu.objects
            # .filter(Q(group__in=request.user.groups.all()) | Q(subgroup=request.user.subgroup))
            .filter(group__in=request.user.groups.all())
            .values("id", "menu", "submenu", "url", "icon", "group", "subgroup")
            .distinct()
        )

        # Convert the queryset into a list of dictionaries
        data = list(menu_data)

        # Create a dictionary to store the data grouped by menu
        grouped_data = defaultdict(list)

        # Group items by menu
        for item in data:
            menu = item["menu"]
            grouped_data[menu].append(
                {
                    "id": item["id"],
                    "submenu": item["submenu"],
                    "icon": item["icon"],
                    "url": item["url"],
                    "group": item["group"],
                    "subgroup": item["subgroup"],
                }
            )

        # Convert the dictionary back to a list of dictionaries
        result_list = [
            {"menu": menu, "items": items} for menu, items in grouped_data.items()
        ]

        # Store the data in the session
        request.session["menu_data"] = result_list

        return func(request, *args, **kwargs)

    return wrapper


# TODO: improve saving location
# TODO: replace default django messaging with toast
# import os
# from django.core.files.images import Image
# from django.contrib import messages
# from .models import CustomUser

# def resize_and_save_image(photo, user):
#     """
#     Resize the image and save it to the media directory.
#     """
#     # Define the target size
#     target_size = (300, 300)

#     # Resize the image
#     try:
#         with Image.open(photo) as image:
#             image.thumbnail(target_size)
#             # Define the filename
#             filename = f"{user.id}.{photo.name.rsplit('.', 1)[1].lower()}"
#             # Define the file path
#             file_path = os.path.join('user_photos', filename)
#             # Save the image
#             with open(os.path.join('media', file_path), 'wb+') as destination:
#                 image.save(destination, format='JPEG')
#     except Exception as e:
#         messages.error(request, f'Error resizing image: {str(e)}')
#         return None

#     return file_path
