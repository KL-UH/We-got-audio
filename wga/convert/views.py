from email import message
# from pickle import FALSE
from django.shortcuts import render
from .models import urlConvert
import sys
# from django.contrib import messages
from django.http import HttpResponse
import subprocess
from subprocess import run, PIPE

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
    


        
    return subprocess.run(['python', 'C:\\Users\\Kripzen\\Desktop\\convo\\main.py', url], shell=False, timeout=1800)
    # return render(request,'home.html')


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