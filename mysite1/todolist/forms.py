from django import forms
from todolist.models import Diary, Comment

class DiaryForm(forms.ModelForm):
    class Meta:
        model=Diary
        fields=['subject', 'content']

        labels={
            'subject':'제목',
            'content':'내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']
        labels={
            'content':'답변내용',
        }
