from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'homepage.html')
    #return HttpResponse("frgtr")
def count(request):
    fulltext = request.GET['mainarea']
    arr=fulltext.split(' ')
    wdict={}
    for word in arr:
        if word in wdict:
            wdict[word]+=1
        else:
            wdict[word]=1
    sortw=sorted(wdict.items(),key=operator.itemgetter(1),reverse=True)   
    return render(request,'count.html',{'res':len(arr),'sortedwords':sortw,'text':fulltext})
def aboutus(request):
    return render(request,'aboutus.html')