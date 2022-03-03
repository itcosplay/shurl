from django.forms import ModelForm, TextInput

from short_link.models import Link


class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['url']

        widgets = {
            'url': TextInput(attrs={
                'placeholder': 'What url to shuuurl?'
            })
        }