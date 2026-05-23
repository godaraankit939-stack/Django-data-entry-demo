from django.shortcuts import render
from django.http import JsonResponse
from .models import Student

def form_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        course = request.POST.get('course')

        Student.objects.create(
            name=name,
            phone=phone,
            course=course
        )

        return render(request, 'form.html', {'success': True})

    return render(request, 'form.html')


# API (GET + POST)
def student_api(request):
    if request.method == "GET":
        data = list(Student.objects.values())
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        course = request.POST.get('course')

        student = Student.objects.create(
            name=name,
            phone=phone,
            course=course
        )

        return JsonResponse({"message": "Student added"})
