from django.http import HttpResponse
from django.shortcuts import render
def index(request):
   # params={'name':'ayush','place':'kanpur' }

    return render(request,'index.html')
def analyze(request):
    removepunc=request.POST.get('removepunc', 'off')
    uppercase =request.POST.get('uppercase', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover =request.POST.get('extraspaceremover', 'off')

    djtext=request.POST.get('text', 'off')
    if (removepunc == 'on'):
        puclist = '''`~!@#$%^&*()-_=+[]\{}|;':",./<>?'''
        analyzed = ''
        for i in djtext:
            if i not in puclist:
                analyzed = analyzed + i

        params = {'purpose': 'removed punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (uppercase == 'on'):
        analyzed = ''
        for i in djtext:
            analyzed = analyzed + i.upper()

        params = {'purpose': 'uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == 'on'):
        analyzed = ''
        for index, i in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==' '):
                analyzed = analyzed + i
        params = {'purpose': 'extraspaceremover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == 'on'):
        analyzed = ''
        for i in djtext:
            if  (i != "\n" and i != "\r"):
                analyzed = analyzed + i

        params = {'purpose': 'newlineremover', 'analyzed_text': analyzed}





    return render(request, 'analyze.html', params)

    if(extraspaceremover != 'on' and newlineremover != 'on' and uppercase != 'on' and removepunc != 'on'):
       return HttpResponse('error')













#def removepunc(request):
  #  return HttpResponse("<h1>capitalize</h1>")
#def newline(request):
 #   return HttpResponse("<h1>newline</h1>")
#def spaceremover(request):
 #   return HttpResponse("spaceremover<a href='/'>back</a> ")
#def charcount(request):
 #   return HttpResponse("<h1>charcount</h1>")