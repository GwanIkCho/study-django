from datetime import timezone, datetime

from django.test import TestCase
from random import randint
from image.models import Image
from member.models import Member

class ImageTest(TestCase):
    pass
    # members = Member.objects.all()
    # images = []
    # for i in range(100):
    #     image = Image(
    #         image_title=f'image_file{i+1}',
    #         image_members=members[randint(0, len(members)-1)]
    #     )
    #     images.append(image)
    # Image.objects.bulk_create(images)

    # image_puery = Image.objects.filter(created_date__gte=datetime(2024, 2, 21, 16),image_members_id=3).values('image_title')
    # for image in image_puery:
    #     print(image)