from django.forms import ModelForm, Textarea
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['blog','user']

        fields = [
            'comment',
        ]

        labels = {
            'comment':'',
        }

        widgets = {
            'comment':Textarea(attrs={'id':"comment", 'class':"form-control", 'name':"comment", 'cols':"45", 'rows':"8", 'aria-required':"true", 'placeholder':"Comment"}),
        }