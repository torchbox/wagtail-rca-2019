from django import forms
from django.contrib.auth.forms import UsernameField

from rca.users.models import User


class StudentCreateForm(forms.ModelForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True}), required=True,
    )
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    create_student_page = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}
