from django import forms
from .models import Library
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

class LibraryWriteForm(forms.ModelForm):
    title = forms.CharField(
        lebel = '글 제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '게시글 제목'
            }
        ),
        required=True,
    )


    contets = SummernoteTextField()
    field_order = [
        'title',
        'contents'
    ]

    class Meta:
        model = Library
        fields = [
            'title',
            'contents'
        ]

        
        widgets = {
            'contents' : SummernoteWidget()
        }
        
        def clean(self):
            cleaned_data = super().clean()

            title = cleaned_data.get('title', '')
            contents = cleaned_data.get('contents', '')
            
            if title == '':
                self.add_error('title', '글 제목을 입력하세요.')
            elif contents == '':
                self.add_error('contents', '글 내용을 입력하세요.')
            else:
                self.title = title
                self.contents = contents
