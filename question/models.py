from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    ICON_CHOICES = (
        ('Arr','Array'),
        ('DP', 'Dynamic Programing'),
        ('STR', 'String'),
        ('LL','Linked List'),
        ("S",'Stack')
    )
    name = models.CharField(max_length=100)
    img = models.ImageField(blank=True, null=True, upload_to='./media/category')
    icon = models.CharField(max_length=3, choices=ICON_CHOICES, blank=True , null=True)
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
    difficulty = models.CharField(max_length=100 , choices=DIFF_CHOICES , default='Easy')
    tags = models.ForeignKey(Category,blank=True , null=True, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    example = models.ManyToManyField('Example' , blank=True , related_name='exampleQuestion')
    companies = models.ManyToManyField(Company, blank=True)

    def __str__(self):
        return self.heading

class Example(models.Model):
    input = models.CharField(max_length=1000)
    output = models.CharField(max_length=1000)
    explaination = models.TextField()
    img = models.ImageField(null=True , blank=True)
    ques = models.ForeignKey(Question , on_delete=models.CASCADE , related_name='ques')

    def __str__(self):
        return str(self.ques.heading)