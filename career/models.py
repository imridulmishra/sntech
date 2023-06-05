from django.db import models
from django.utils import timezone
# Create your models here.
class JobPost(models.Model):
    location=models.CharField(max_length=100)
    jobfunction = models.CharField(max_length=50)
    role = models.CharField(max_length=20)
    skills=models.CharField(max_length=200)
    experience=models.CharField(max_length=30)
    discription=models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True,blank=True)
    last_date = models.DateField(null=True, blank=True,)
    vacancies = models.IntegerField(default=1)
    CHOICES = (
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Intern', 'Intern'),
    )

    category = models.CharField(max_length=10, choices=CHOICES,default='Full-Time')
    qualification = models.CharField(max_length=100,default='Bachelor of technology')