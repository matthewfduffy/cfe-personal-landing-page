from django import forms

class LandingPageForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    email2 = forms.EmailField(label='Confirm Email')

    # Validation Methods
    def clean(self):
        data = self.cleaned_data
        # email = self.cleaned_data.get("email")
        email = data.get("email")
        email2 = data.get("email2")
        if email2 != email:
            self.add_error('email', 'Emails do not match.')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email.endswith('aol.com'):
            self.add_error('email', 'You cannot use AOL domains.')
            # raise forms.ValidationError("You are really old!")
        return email