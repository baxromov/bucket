from apps.models import Department


def departments(request):
    data = {
        "departments": Department.objects.all()
    }
    return data
