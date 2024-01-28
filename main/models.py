from django.db import models
from django.utils.safestring import mark_safe


class Subject(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Home(models.Model):
    name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55, blank=True, null=True)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name


class About(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='media/about', blank=True, null=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=55)
    email = models.EmailField()
    phone = models.CharField(max_length=55)
    complete_projects = models.IntegerField(default=0)


class Partners(models.Model):
    image = models.ImageField(upload_to='media/partners',)






