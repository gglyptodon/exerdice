"""store form-related classes"""
from django.conf import settings
from django import forms


from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from .models import ExerciseDefinition
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab
from crispy_forms.layout import Submit, Fieldset, MultiField, Div

class ExerciseForm(forms.ModelForm):
    choices = ExerciseDefinition.objects.all() #todo !!! save this on upload
    helper = FormHelper()
    helper.add_input(Submit('submit','Submit'))
    helper.layout = Layout(
         Fieldset(
             'exercise_name',
         ),
    )
    class Meta:
        model = ExerciseDefinition
        fields = ('name',)

####

class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)


class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
        }
    new_password1 = forms.CharField(label=("New password"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("New password confirmation"),
                                    widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                    )
        return password2