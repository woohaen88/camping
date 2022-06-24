from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("이메일이 존재합니다.")
        return email
    
    
class SigninForm(forms.ModelForm):
    password = forms.CharField(label = "비밀번호", 
                               help_text="비밀번호를 입력하세요",
                               max_length=15, 
                               widget=forms.TextInput(
                                   attrs = {"type" : "password",
                                            "placeholder" : "비밀번호를 입력하세요~~" })
                              )
    class Meta:
        model = User
        fields = ("email", "password")