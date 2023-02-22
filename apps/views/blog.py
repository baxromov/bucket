from django.shortcuts import render


def index(request):
    context = {
        "url":"Asd"
    }
    return render(request, 'pages/blog/index.html', context=context)
