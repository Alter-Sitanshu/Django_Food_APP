from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=120)
    item_desc = models.TextField(max_length=200)
    item_price = models.PositiveIntegerField(blank=False, null=False)
    item_img = models.URLField(blank=True, null=True, default='https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png')
    item_author = models.CharField(max_length=100, null=False, blank=False, editable=False)
    uploaded_on = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.item_name
