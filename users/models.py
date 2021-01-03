from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # cascade: if user is deleted, delete the profile
    # bio = models.TextField(help_text='Enter About Yourself')
    # location = models.CharField(max_length=50, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)