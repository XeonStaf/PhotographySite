from django import forms

from photoshoots.models import Review
from django_starfield import Stars
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.bootstrap import InlineCheckboxes


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('what_liked', 'what_disliked', 'post_photo_in_social', 'rate_mood', 'rate_photo')
        widgets = {
            'rate_mood': Stars,
            'rate_photo': Stars,

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'what_liked',
            'what_disliked',
            Row(
                Column('post_photo_in_social', css_class=''),
                Column('rate_mood', css_class='form-group mb-3'),
                Column('rate_photo', css_class='form-group mb-3'),
                css_class='form-row'
            ),
            Submit('sumbit', 'Отправить', css_class="btn btn-all btn-next", style="position: relative; left: 25%")
        )


