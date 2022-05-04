from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(blank=True, null=True, upload_to='./media/category')
    def __str__(self):
        return self.name



class Company(models.Model):
    name =models.CharField(max_length=100)
    def __str__(self):
        return self.name




class Question(models.Model):
    DIFF_CHOICES = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )
    heading = models.CharField(max_length=200)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    difficulty = models.CharField(max_length=100 , choices=DIFF_CHOICES )
    tags = models.ForeignKey(Category,blank=True , null=True, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    # example = models.
    companies = models.ManyToManyField(Company, blank=True)

    def __str__(self):
        return self.heading