from django.shortcuts import render


def about(request):
    context = {'current_view': 'about'}
    template = 'pages/about.html'
    return render(request, template, context)


def rules(request):
    context = {'current_view': 'rules'}
    template = 'pages/rules.html'
    return render(request, template, context)
