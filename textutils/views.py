from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def about(request):
    return HttpResponse("About Page")

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    if removepunc== 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        
        params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")





# def capitalizefirst(request):
#     return HttpResponse('capfirst')


# def newlinerremove(request):
#     return HttpResponse('newlinerremove')

# def spaceremover(request):
#     return HttpResponse("spaceremover <a href ='/'> back </a>")


# def charcount(request):
#     return HttpResponse('charcount')