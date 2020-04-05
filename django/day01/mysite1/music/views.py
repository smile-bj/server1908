from django.shortcuts import render,HttpResponse
from . import Book

# Create your views here.
def index(request):
    return render(request,'music/index.html')


def add_book(request):
    if request.method=='GET':
        return render(request,'music/add_book.html')
    elif request.method=='POST':
        title=request.POST.get('title')
        if not title:
            error = 'Please give me title'
            return render(request, 'bookstore/add_book.html', locals())

        pub = request.POST.get('pub')
        price = request.POST.get('price')
        m_price = request.POST.get('m_price')
        try:
            Book.objects.create(title=title,pub=pub,price=price,maket_price=m_price)
        except Exception as e:
            print(e)
            return render(request,'bookstore/add_book.html',locals())
        return render(request,'bookstore/add_book.html')
    return HttpResponse('sorry---you can not enter ')