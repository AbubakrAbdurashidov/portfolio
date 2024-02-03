from django.db import models


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
    website = models.URLField(blank=True)
    CV = models.FileField(blank=True, null=True, upload_to='media/about')


class Partner(models.Model):
    image = models.ImageField(upload_to='media/partners', blank=True, null=True)
    link = models.URLField(blank=True)


class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    university_name = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)

    def __str__(self):
        return self.university_name


class TopSkill(models.Model):
    title = models.CharField(max_length=255)
    percent = models.IntegerField()
    last_week = models.IntegerField()
    last_month = models.IntegerField()

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=255)
    percent = models.IntegerField()

    def __str__(self):
        return self.title


class Experience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    company_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name


class Award(models.Model):
    date = models.DateField()
    description = models.TextField()
    where_get_award = models.CharField(max_length=255)
    award_name = models.CharField(max_length=255)

    def __str__(self):
        return self.award_name


class Service(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/services', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='media/projects', blank=True, null=True)


    def __str__(self):
        return self.title


class Counter(models.Model):
    awards = models.IntegerField(default=0)
    complete_projects = models.IntegerField(default=0)
    happy_customers = models.IntegerField(default=0)
    cups_of_coffee = models.IntegerField(default=0)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)









