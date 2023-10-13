from se2.search import search as se2_search
from django.shortcuts import render

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
