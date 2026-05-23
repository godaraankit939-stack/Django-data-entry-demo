from django.shortcuts import render
from .models import Student

def form_view(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        course = request.POST['course']

        Student.objects.create(name=name, phone=phone, course=course)

    return render(request, 'form.html')
