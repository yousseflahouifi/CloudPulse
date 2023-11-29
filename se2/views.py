from se2.search import search as se2_search
from django.shortcuts import render
import subprocess
from django.http import HttpResponse


def search(request):
    q = request.GET.get('q')
    s = request.GET.get('s')

    if q :
        if s and s.isdigit() :
            results = se2_search(q,s=s)
        else:
            results = se2_search(q)
    else : 
        results=''
    if results :
        return render(request,'se2/search.html',{'data':results,'count':results.count()})
    else:
        return render(request,'se2/search.html')


def scan(request):
    q = request.GET.get('q')
    if q :
        port_range = '80,81,83,90,88,8000,8080,8443,9443,9090,4443,7443,444,10250,6443,8888,8081,443,10000,9200,554,264,84'
        
        # Use a single subprocess.run call with a pipe and shell=True
        command = f'nmap -p {port_range} --open {q} | grep open'
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
        result_with_line_breaks = result.stdout.replace('\n', '<br>')

        return HttpResponse(result_with_line_breaks)

