from django.shortcuts import render

from apps.models import Department


def index(request):
    departments = Department.objects.all()
    context = {
        'departments': departments
    }
    return render(request, 'pages/main.html', context=context)

