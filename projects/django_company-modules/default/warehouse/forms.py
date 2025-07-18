import hashlib
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, HTML
from crispy_forms.bootstrap import Div
from django_select2 import forms as s2forms
from core.forms import BaseTaskForm
from .models import Item, OutboundRequest


# class ItemWidget(s2forms.ModelSelect2Widget):
#     search_fields = [
#         "code__icontains",
#         "name__icontains",
#         "description__icontains",
#     ]

# class AddressWidget(forms.TextInput):
#     template_name = 'widgets/address_input.html'

#     class Media:
#         css = {
#             'all': ('path/to/your/css/address-autocomplete.css',)
#         }
#         js = ('https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places', 'path/to/your/js/address-autocomplete.js')

#     def get_context(self, name, value, attrs):
#         context = super().get_context(name, value, attrs)
#         context['widget']['api_key'] = 'YOUR_API_KEY'  # Pass your Google Maps API key to the template
#         return context

#######################


class OrderForm(BaseTaskForm):
    # outboundrequest object (license_plate, products(Item), task, destination_code)
    license_plate = forms.CharField(max_length=100)
    products = forms.ModelMultipleChoiceField(
        queryset=Item.objects.all(),
        widget=forms.SelectMultiple,
        # widget=ItemWidget,
        # help_text="Select from the available products to be shipped.",
    )
    # address = forms.CharField(widget=AddressWidget(attrs={'id': 'address-input'}))
    address = forms.CharField(widget=forms.TextInput(attrs={"id": "address-input"}))

    def __init__(self, *args, user, **kwargs):
        super().__init__(*args, user=user, type="shipping", **kwargs)
        self._set_hidden_fields()

    def build(self):
        # TODO: inherit from the BaseTaskForm build method, so don't have to repeat the fields
        # NOTE: avoiding adding the fields from the base form created a problem withe the form
        #       validation and the form submission. The fields were not being added to the form

        # Additional fields you want to include
        additional_fields = [
            "license_plate",
            "products",
            "address",
        ]
        new_fields_order = [
            "name",
            "description",
            *additional_fields,
            "start_date",
            "due_date",
            "type",
            "status",
            "created_by",
            "updated_by",  # hidden fields from the base form
        ]

        return Layout(
            Div(
                *new_fields_order,
                ButtonHolder(
                    HTML(
                        '<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>'
                    ),
                    HTML(
                        '<button type="submit" class="btn btn-primary ms-3">Create</button>'
                    ),
                ),
                css_class="modal-body",
            )
        )

    def generate_destination_code(self):
        # receive the destination and create a hash code
        destination = self.cleaned_data.get("address")
        hash_object = hashlib.sha3_256(destination.encode())
        destination_code = hash_object.hexdigest()
        return destination_code

    def set_outbound_request(self, task_instance):
        # set the outbound request with the information of the form
        ## fields: license_plate, products, task, destination_code
        outbound_request = OutboundRequest(
            license_plate=self.cleaned_data.get("license_plate"),
            task=task_instance,
            destination_code=self.generate_destination_code(),
        )
        try:
            outbound_request.save()
            return True, None
        except Exception as e:
            return False, e

    def _set_hidden_fields(self):
        hidden_fields = ["type", "status", "created_by", "updated_by"]
        for field in hidden_fields:
            self.fields[field].widget = forms.HiddenInput()
