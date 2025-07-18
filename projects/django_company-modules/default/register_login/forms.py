from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, ButtonHolder, HTML, Div, Submit

from .models import CustomUser, CustomGroup


class MultiSelectionGroupForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        label="CustomUsers",
        queryset=CustomUser.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("users", False),
    )

    class Meta:
        model = CustomGroup
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["users"].initial = self.instance.user_set.all()

    def save_m2m(self):
        self.instance.user_set.set(self.cleaned_data["users"])

    def save(self, *args, **kwargs):
        instance = super().save()
        self.save_m2m()
        return instance


class BaseCustomUserForm(forms.ModelForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label="Remember me", required=False)

    class Meta:
        model = CustomUser
        fields = "__all__"

    def __init__(self, *args, action=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        if action:
            self.helper.form_action = action


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label="Remember me", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "register_login:login"
        self.helper.layout = Layout(
            "email",
            "password",
            "remember_me",
            Submit("submit", "Login", css_class="btn btn-primary btn-block mx-4 my-2"),
        )


class RegisterForm(BaseCustomUserForm):
    password_confirm = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput
    )

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, action="register_login:register", **kwargs)
        self.helper.layout = Layout(
            Row(
                Column("first_name", css_class="form-group col-md-6 mb-0"),
                Column("last_name", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            "email",
            "password",
            "password_confirm",
            Div(
                Submit(
                    "submit", "Create Account", css_class="btn btn-primary btn-block"
                ),
                css_class="d-grid",
            ),
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")


class UpdateCustomUserForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(
        label="Groups",
        queryset=CustomGroup.objects.none(),
        widget=forms.SelectMultiple(attrs={"class": "selectmultiple form-select"}),
    )

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "subgroup"]
        edit_fields = ["first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Check if form is in edit mode
        btns = self.set_edit_mode(
            True if "initial" in kwargs and "edit" in kwargs["initial"] else False
        )

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column("first_name", css_class="form-group col-md-6 mb-0"),
                Column("last_name", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            "email",
            Row(
                Column("groups", css_class="form-group col-md-6 mb-0"),
                Column("subgroup", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            ButtonHolder(*btns, css_class="submit-row"),
        )

        # Update queryset for groups field to display only CustomUser registered groups
        self.fields["groups"].queryset = self.instance.groups.all()

    def set_edit_mode(self, mode):
        if mode:
            for field in self.fields:
                if field in self.Meta.edit_fields:
                    self.fields[field].disabled = False
                    self.fields[field].readonly = False
                else:
                    self.fields[field].disabled = True
                    self.fields[field].readonly = True
            return (
                HTML(
                    '<a href="{% url "register_login:profile" %}" class="btn btn-outline-danger me-2">Cancel</a>'
                ),
                Submit("submit", "Save", css_class="btn btn-success"),
            )
        else:
            for field in self.fields:
                self.fields[field].disabled = True
                self.fields[field].readonly = True
            return (
                HTML(
                    '<a href="{% url "register_login:profile_edit" %}" class="btn btn-primary">Edit</a>'
                ),
            )

    def save(self, commit=True):
        # Override save method to handle saving in both edit and create mode
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
