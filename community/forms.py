from django import forms
from community.models import Post, Answer

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content']
        label = {
            'subject' : '제목',
            'content' : '내용'
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        label = {
            'content' : '내용'
        }