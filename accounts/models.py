from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profession = (
        ('student','student'),
        ('teacher','teacher'),
        ('other','other'),
    )
    user = models.OneToOneField(User , related_name='profile' , on_delete=models.CASCADE)
    profession = models.CharField(max_length=100 , default='other')

    def __str__(self):
        return self.user.name

