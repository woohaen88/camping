from secrets import choice
from turtle import title
from django import forms
from django.contrib.auth import get_user_model
from .models import Post, Photos


class PostForm(forms.ModelForm): 
    title = forms.CharField(label="캠핑장이름", 
                                 widget=forms.TextInput(
                                     attrs = {
                                         "type" : " text"
                                     }
                                 )) 

    visited_at = forms.CharField(label="언제 갔니?", 
                                 widget=forms.TextInput(
                                     attrs = {
                                         "type" : "date"
                                     }
                                 )) 
    

    kind_of_camping = forms.CharField(label="캠핑종류", 
                                 widget=forms.Select(
                                     choices=Post.CampingKindChoice.choices,
                                 )) 
    quiet = forms.CharField(label="캠퍼는 조용하니?", 
                                 widget=forms.Select(
                                     choices=Post.QuietChoice.choices,
                                 )) 
    site_parking = forms.CharField(label="사이트에 주차 가능?", 
                                 widget=forms.Select(
                                     choices=Post.SiteParking.choices,
                                 )) 
    ground = forms.CharField(label="접지여부", 
                                 widget=forms.Select(
                                     choices=Post.GroundChoice.choices,
                                 )) 
    animal = forms.CharField(label="반려동물 가능?", 
                                 widget=forms.Select(
                                     choices=Post.AnimalChoice.choices,
                                 )) 
    camp_fire = forms.CharField(label="불멍이 가능한가?", 
                                    widget=forms.Select(
                                     choices=Post.CampFireChoice.choices,
                                 )) 

    camp_view = forms.CharField(label="뷰는 어떠한가?", 
                                 widget=forms.Select(
                                    choices=Post.CampViewChoice.choices,
                                 )) 

    class Meta:
        model = Post
        fields = (
            "title",
            "review",
            "kind_of_camping",
            "quiet",
            "site_parking",
            "ground",
            "visited_at",
            "animal",
            "camp_fire",
            "camp_view",
        )
