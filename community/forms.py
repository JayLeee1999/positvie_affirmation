from django.forms import ModelForm
from community.models import Article

class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['nickname', 'emotion', 'affirmation']

