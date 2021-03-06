from django.contrib.auth.forms import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class registerForm(forms.Form):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput,label='New Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            # Row(
            #     Column('first_name', css_class='form-group col-md-6 mb-0'),
            #     Column('last_name', css_class='form-group col-md-6 mb-0'),
            #     css_class='form-row'
            # ),
            'username',
            Row(
                Column('password1', css_class='small form-group col-md-6 mb-0'),
                Column('password2', css_class='small form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Register')
        )
