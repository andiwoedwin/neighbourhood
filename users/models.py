from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from neighbourhood.models import Neighbourhood


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250, default="My city my town", blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    location = models.CharField(max_length=50, blank=True, null=True)
    neighborhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE, blank=True, null=True)


    def save_profile(self):
        self.save()


    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)





