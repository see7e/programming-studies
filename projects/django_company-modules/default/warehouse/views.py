from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from core.utils import response_trigger
from register_login.models import CustomUser
from .models import Item, OutboundRequest
from .forms import OrderForm


@login_required
def index(request):
    item_list = Item.objects.all()
    context = {"item_list": item_list}
    return render(request, "inventory.html", context)


@login_required
def orders(request):
    order_list = OutboundRequest.objects.all()
    print(len(order_list))
    context = {"order_list": order_list}
    return render(request, "orders.html", context)


@login_required
def list_orders(request):
    # return
    order_list = OutboundRequest.objects.all()
    print(len(order_list))
    context = {"order_list": order_list}
    return render(request, "order_list.html", context)


@login_required
def new_order(request):
    user = get_object_or_404(CustomUser, pk=request.user.id)
    if request.method == "POST":
        form = OrderForm(request.POST, user=user)
        if form.is_valid():
            with transaction.atomic():
                task_instance = form.save()
                request_created, errors = form.set_outbound_request(task_instance)
                if not request_created:
                    raise ValueError(errors)
            return response_trigger(200, hx_triggers={"orderListChanged": None})
        else:
            print(form.has_error)
            print(form.errors)
            # print(form.non_field_errors)
    form = OrderForm(user=user)
    return render(request, "order_form.html", {"form": form})
