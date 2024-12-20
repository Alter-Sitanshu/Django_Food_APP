from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to="profile_pictures")
    location = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self) -> str:
        return self.user.username