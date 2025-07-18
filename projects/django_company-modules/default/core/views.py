from django.shortcuts import render
from django.http import JsonResponse
from .db import create_warehouse_tables, create_menu_data

####################################################################################################
import subprocess
from warehouse.models import Shed, Rack, Item
import os

# creates some initial data for the database, so you can see how the application works
#    without having to create a bunch of data yourself. It's a good idea to remove this file from the
#    project before deploying it to a production server.


def dev_build(superuser: dict):
    MANAGE_PY_PATH = os.path.join(os.path.dirname(__file__), "..", "manage.py")
    subprocess.run([MANAGE_PY_PATH, "makemigrations"])
    subprocess.run([MANAGE_PY_PATH, "migrate"])
    subprocess.run(
        [
            MANAGE_PY_PATH,
            "createsuperuser",
            "--firstname",
            superuser.firstname,
            "--lastname",
            superuser.lastname,
            "--email",
            superuser.email,
            "--password",
            superuser.password,
        ]
    )


def dev_fill_tables(request):
    all_data = {}
    message = ""
    # create Data (
    #   register_login{CustomUser, CustomGroup, CustomSubGroup, Menu,
    all_data["register_login"] = create_menu_data()
    #   warehouse{Shed, Rack, Item,},
    all_data["warehouse"] = create_warehouse_tables()
    #   hr{},
    #   reports{}
    #   sales{},
    #   purchases{},
    # )

    for key in all_data:
        message += (
            f"{key} - {len(all_data[key])} objects created\n"
            if len(all_data[key]) > 0
            else f"{key} - No objects created\n"
        )
    status = "success" if not "No objects created" in message else "error"

    return JsonResponse({"status": status, "message": message})


####################################################################################################
# def dev_login(superuser: dict):
#     subprocess.run(
#         [
#             "../manage.py",
#             "login",
#             "--username",
#             superuser.email,
#             "--password",
#             superuser.password,
#         ]
#     )
####################################################################################################
