from django import forms
from django.contrib.auth import get_user_model
from .models import Post


class PostForm(forms.ModelForm):
    visited_at = forms.CharField(label="언제 갔니?", 
                                 widget=forms.TextInput(
                                     attrs = {
                                         "type" : "date"
                                     }
                                 ))   
    
    
    class Meta:
        model = Post
        fields = (
            "title",
            "review",
            "kind_of_camping",
            "visited_at",
        )

# class Post(models.Model):
#     title = models.CharField(max_length=20)
#     review = models.TextField()
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    
#     class CampingKindChoice(models.TextChoices):
#         CAR = 'C', _('차박')
#         AUTO = 'A', _('오토캠핑')
#         OUTFILED = 'O', _('노지')
        
#     kind_of_camping = models.CharField(
#         max_length=1,
#         choices=CampingKindChoice.choices,
#         default="N",
#     )
#     visited_at = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)