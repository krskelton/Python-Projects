from django.db import models

# Create your models here.

title_options = [
    ('Mrs.', 'Mrs.'),
    ('Mr.', 'Mr.'),
    ('Dr.', 'Dr.'),
]

class Profile(models.Model):
    title = models.CharField(max_length=60, default="", choices=title_options)
    firstName = models.CharField(max_length=60, default="", blank=True)
    lastName = models.CharField(max_length=60, default="", blank=True)
    email = models.CharField(max_length=255, default="", blank=True)
    username = models.CharField(max_length=255)

    objects = models.Manager()

    def __str__(self):
        return self.firstName