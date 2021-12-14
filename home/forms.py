from django import forms
from .models import Movie

from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML


class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(

                FloatingField('title', autofocus='autofocus'),
                FloatingField('gross'),
            HTML('<button type="submit" class="btn btn-outline-info">Добавить</button>'),
            )
