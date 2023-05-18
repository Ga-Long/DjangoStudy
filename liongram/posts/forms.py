from django import forms

from django.core.exceptions import ValidationError
from .models import Post

# class PostBaseForm(forms.Form):
#     image = forms.ImageField()
#     content = forms.CharField(widget=forms.Textarea)


# models 에 있는 Post 모델이 알아서 들어감
class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__' # field는 전체 필드 
        

class PostCreateForm(PostBaseForm): # base에서 image, content만 
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']
    
    def clean_content(self):
        data = self.cleaned_data['content']
        if "비속어" == data:
            raise ValidationError("'비속어는 사용하실 수 없습니다.")
        
        return data
        
class PostUpdateForm(PostBaseForm): # base에서 image, content만 
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']


class PostDetailForm(PostBaseForm): # base에서 image, content만 
    pass