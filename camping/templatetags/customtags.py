from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='kind_of_camping')
def kind_of_camping(value):
    if value == "C":
        return mark_safe("차박")
    elif value == "A":
        return mark_safe("오토캠핑")
    elif value == "O":
        return mark_safe("노지")
    else:
        return mark_safe("지정되지 않음")

@register.filter(name='quiet_choice')
def quiet_choice(value):
    if value == "High":
        return mark_safe("매우 조용")
    elif value == "Low":
        return mark_safe("시끌시끌 와르르 왕창")
    elif value == "Middle":
        return mark_safe("중간정도?")


@register.filter(name='site_parking')
def site_parking(value):
    if value == "CAN":
        return mark_safe("사이트 주차 가능")
    elif value == "CANNOT":
        return mark_safe("사이트 주차 불가능!!")
    elif value == "DONTKNOW":
        return mark_safe("모르겠어용")


@register.filter(name='ground_choice')
def ground_choice(value):
    if value == "CAN":
        return mark_safe("접지")
    elif value == "CANNOT":
        return mark_safe("접지 아님")
    elif value == "DONTKNOW":
        return mark_safe("모름")

@register.filter(name='animal_choice')
def animal_choice(value):
    if value == "CAN":
        return mark_safe("가능")
    elif value == "CANNOT":
        return mark_safe("불가능")
    elif value == "DONTKNOW":
        return mark_safe("모름")

@register.filter(name='camp_fire_choice')
def camp_fire_choice(value):
    if value == "CAN":
        return mark_safe("가능")
    elif value == "CANNOT":
        return mark_safe("불가능")
    elif value == "DONTKNOW":
        return mark_safe("모름")


@register.filter(name='camp_view_choice')
def camp_view_choice(value):
    if value == "FOREST":
        return mark_safe("숲쀼~")
    elif value == "OCEAN":
        return mark_safe("오션뷰")
    elif value == "RIVER":
        return mark_safe("계곡")
    elif value == "SHIT":
        return mark_safe("똥뷰")
    elif value == "OTHERS":
        return mark_safe("기타")