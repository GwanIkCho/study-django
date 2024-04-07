from django.db import models

from member.models import Member
from model.models import Period


class Image(Period):
    STATUS_CHOICES = [
        (0, '정지'),
        (1, '활동중')
    ]

    image_members = models.ForeignKey(Member ,null=False, blank=False , on_delete=models.PROTECT)
    image_url = models.CharField(null=False, blank=False, default='/images/', max_length=100)
    image_title = models.CharField(null=False, blank=False, max_length=100)
    image_status = models.BooleanField(null=False, blank=False,default=False,choices=STATUS_CHOICES)

    class Meta:
        db_table = 'tbl_image'