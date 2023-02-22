from django.shortcuts import render


def index(request):
    context = {
        "a": 1
    }
    return render(request, 'pages/main.html', context=context)
