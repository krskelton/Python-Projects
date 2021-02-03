from django.http import HttpResponse
from django.shortcuts import render
from classApp.models import djangoClasses

def home(request):
    #add djangoclasses objects to add classes to the database
    class1 = djangoClasses(title="English", courseNumber=1001, instructorName="Mrs. Skelton", duration=60)
    class1.save()
    class2 = djangoClasses(title="Biology", courseNumber=1002, instructorName="Mr. Neubauer", duration=60)
    class2.save()
    class3 = djangoClasses(title="Computer Science", courseNumber=1003, instructorName="Mr. Cali", duration=60)
    class3.save()
    data = djangoClasses.objects.all()
    classes = {
        "classes" : data
    }
    #send the classes to the home document to be diplayed
    return render(request, 'home.html', classes)



