from django.shortcuts import render, HttpResponse

# Create your views here.


def hello_fulano(request, nome):
    return HttpResponse('<h1>Hello World!</h1>'
                        '<br>'
                        '<h2>Olá {}, gostou do Django?'.format(nome))


def hello(request):
    return HttpResponse('<h1 align="center" padding-top="20px">Hello World!</h1>')
