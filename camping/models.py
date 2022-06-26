from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.processors import Thumbnail


class Post(models.Model):
    title = models.CharField(max_length=20)
    review = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    
    class CampingKindChoice(models.TextChoices):
        CAR = 'C', _('차박')
        AUTO = 'A', _('오토캠핑')
        OUTFILED = 'O', _('노지')
        
    kind_of_camping = models.CharField(
        max_length=1,
        choices=CampingKindChoice.choices,
        default="N",
    )
    visited_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ("-updated_at",)

    def __str__(self):
        return self.title


    class QuietChoice(models.TextChoices):
        HIGH = 'High', _('시끄러움')
        LOW = 'Low', _('조용조용')
        MIDDLE = 'Middle', _('중간쯔음?')
        
    quiet = models.CharField(
        max_length=6,
        choices=QuietChoice.choices,
    )

    class SiteParking(models.TextChoices):
        CAN = 'CAN', _('가능')
        CANNOT = 'CANNOT', _('불가능')
        DONTKNOW = 'DONTKNOW', _('모름')
        
    site_parking = models.CharField(
        max_length=8,
        choices=SiteParking.choices,
    )

    class GroundChoice(models.TextChoices):
        CAN = 'CAN', _('가능')
        CANNOT = 'CANNOT', _('불가능')
        DONTKNOW = 'DONTKNOW', _('모름')
        
    ground = models.CharField(
        max_length=8,
        choices=GroundChoice.choices,
    )    

    class AnimalChoice(models.TextChoices):
        CAN = 'CAN', _('가능')
        CANNOT = 'CANNOT', _('불가능')
        DONTKNOW = 'DONTKNOW', _('모름')
        
    animal = models.CharField(
        max_length=8,
        choices=AnimalChoice.choices,
    )    

    class CampFireChoice(models.TextChoices):
        CAN = 'CAN', _('가능')
        CANNOT = 'CANNOT', _('불가능')
        DONTKNOW = 'DONTKNOW', _('모름')
        
    camp_fire = models.CharField(
        max_length=8,
        choices=CampFireChoice.choices,
    )

    class CampViewChoice(models.TextChoices):
        FOREST = 'FOREST', _('숲쀼~~')
        OCEAN = 'OCEAN', _('오션뷰')
        RIVER = 'RIVER', _('계곡뷰~~~!!')        
        SHIT = 'SHIT', _('똥망')
        OTHERS = 'OTHERS', _('기타')
        
    camp_view = models.CharField(
        max_length=6,
        choices=CampViewChoice.choices,
    )

class Photos(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, related_name="images")
    # image = ProcessedImageField(
	# 	upload_to = 'camping/image/%Y/%M/%d',
	# 	processors = [Thumbnail(100, 100)], # 처리할 작업 목룍
	# 	format = 'JPEG',					# 최종 저장 포맷
	# 	options = {'quality': 60})  
    image = models.ImageField(upload_to="camping/images/%Y/%m/%d", blank=True)
    class Meta:
        verbose_name_plural = "Photo"

    
