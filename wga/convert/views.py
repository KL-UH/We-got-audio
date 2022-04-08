from email import message
from re import template
# from pickle import FALSE
from django.shortcuts import render
from .models import urlConvert
import sys
# from django.contrib import messages
from django.http import HttpResponse
import subprocess
from subprocess import run, PIPE
from django.core.files.storage import FileSystemStorage

def home(request):
    if(request.method == "POST"):
        if(request.POST.get('link')):
            saveurl = urlConvert()
            saveurl.link = request.POST.get('link')
            saveurl.save()
            message.success(request,"Saved Succesfully")
            return render(request,"home.html")
    else:
        return render(request,"home.html")

def file(request):
    return render(request,"file.html")

def url_convert(request):
    print("Working")
    
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")



def convertor(request):
    url = request.POST.get('urlConvert')

    # out = run([sys.executable,'.\\convo.py',url],shell=False,stdout=PIPE)
    # C:\\Users\\Kripzen\\Desktop\\convo\\main.py
    print(url)

    convostr = str(url)
    out = run([sys.executable,'C:\\Users\\Kripzen\Desktop\\We-got-audio\\Convert_codes\\urlConvertor.py',str(convostr)],shell=False,stdout=PIPE)
    print(out)


    return render(request,'home.html')


'''

def convertor(request):

    if request.method == 'POST': # If the form has been submitted...
        form = urlConvert(request.POST) # A form bound to the POST data # All validation rules pass
        print(form)


        # convot(form.cleaned_data)

        

    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")








       if(request.method == "POST"):
        if(request.POST.get('link')):
            saveurl = urlConvert()
            saveurl.link = request.POST.get('link')
            todo = saveurl.save()
            print(todo)
            message.success(request,"Saved Succesfully")


    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")


    '''

def test(request):
    inp = request.POST.get('urlConvert')
    
    out = run([sys.executable,'C:\\Users\\Kripzen\\Desktop\\convo\\main.py',inp],shell=False,stdout=PIPE)
    print(out)

    return render(request,'home.html',{'data1':out})


def files(request):
    vdo = request.FILES['myfile']
    fs=FileSystemStorage()
    filename = fs.save(vdo.name,vdo)
    print(filename)
    # Image path
    fileurl = fs.open(filename)
    print(fileurl)

    templateurl = fs.url(filename) # URL of media in django
    # print(templateurl)

    vdo = run([sys.executable,'C:\\Users\\Kripzen\\Desktop\\We-got-audio\\Convert_codes\\fileConvertor.py',str(fileurl),str(filename)],shell=False,stdout=PIPE)
    print(vdo.stdout)

    return render(request,'file.html')