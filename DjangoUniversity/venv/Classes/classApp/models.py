from django.db import models

# djangoClasses model with a title, courseNumber, instructorName, and duration
class djangoClasses(models.Model):
    title = models.CharField(max_length=250)
    courseNumber = models.IntegerField()
    instructorName = models.CharField(max_length=250)
    duration = models.DecimalField(max_digits=10000, decimal_places=2, default=0.00)

    #model manager
    objects = models.Manager()

    #returns the title in the admin menu
    def __str__(self):
        return self.title