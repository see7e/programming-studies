from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, HTML
from crispy_forms.bootstrap import Div
from .models import Task


class BaseTaskForm(forms.ModelForm):
    # task object (
    #     name, description, user, type, status, start_date, due_date, created_at, created_by,
    #     updated_at, updated_by
    # )
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "start_date": forms.widgets.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "yyyy-mm-dd (DOB)",
                    "class": "form-control",
                }
            ),
            "due_date": forms.widgets.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "yyyy-mm-dd (DOB)",
                    "class": "form-control",
                }
            ),
        }

    def __init__(self, *args, user=None, type=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["type"].initial = type
        self.fields["status"].initial = "pending"
        self.fields["created_by"].initial = user
        self.fields["updated_by"].initial = user

        self.helper = FormHelper(self)
        self.helper.form_method = "post"
        self.helper.form_class = "modal-content"
        self.helper.layout = self.build()

    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=False, *args, **kwargs)
        instance.created_by.save()  # Save the related CustomUser instance
        instance.updated_by.save()  # Save the related CustomUser instance
        if commit:
            instance.save()
        return instance

    # def build(self):
    #     return Layout(
    #         Div(
    #             "name",
    #             "description",
    #             "start_date",
    #             "due_date",
    #             ButtonHolder(
    #                 HTML(
    #                     '<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>'
    #                 ),
    #                 HTML(
    #                     '<button type="submit" class="btn btn-primary ms-3">Create</button>'
    #                 ),
    #             ),
    #             css_class="modal-body",
    #         )
    #     )
