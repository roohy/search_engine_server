from django.shortcuts import render
from django.shortcuts import Http404
from django.shortcuts import HttpResponse
from crawler.tools import crawler,indexJson,search
from django.views.decorators.csrf import csrf_protect
from json import dumps,loads
# Create your views here.

@csrf_protect
def indexPage(request):
    context = {}
    return render(request, 'indexePage.html', context)

@csrf_protect
def searchPage(request):
    context = {}
    return render(request, 'searchPage.html', context)

@csrf_protect
def searchIt(request):
    if request.method != 'POST':
        raise Http404
    searchTerm = request.POST['searchTerm']
    result = search(searchTerm)
    result = dumps(result)
    print("result",result)
    return HttpResponse(result, content_type='application/json')

@csrf_protect
def indexIt(request):
    if request.method != 'POST':
        raise Http404
    url = request.POST['url']
    count = request.POST['count']
    count = int(count)
    print("crawling on pages count " , count, " starting form page: ",url )
    crawler(url , count)
    indexJson()
    return HttpResponse("haha")

