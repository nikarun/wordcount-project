from django.http import HttpResponse as hr
from django.shortcuts import render
import operator
def Home(request):
    return render(request, 'home.html')
def count(request):
    fulltext = request.GET["fulltext"]
    count = fulltext.split()
    dict={}
    for i in count:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
   # dict=sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{"fulltext":fulltext,"count":len(count),"dict":dict.items()})
def arun_bio(request):
    return render(request,"bio.html")