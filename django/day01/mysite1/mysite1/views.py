from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render
def page_view(request,d):
    html='这是第%s页'%d
    return HttpResponse(html)
def person_view(request,name,age):
    html='名字：%s,年龄：%s'%(name,age)
    return HttpResponse(html)
def birthday_view(request,year,month):
    html='生日是：%s年%s月'%(year,month)
    print(request.path_info)
    print(request.method)
    if request.method=='GET':
        pass
    print(request.GET)   #类字典对象
    return HttpResponse(html)
def index_view(request):
    # html='跳转到相对地址'
    return render(request,'index.html')
def sports_index(request):
    return render(request,'music.html')
def music_index(request):
    return render(request,'music_index')

def login_view(request):
    # html='重定向'
    return HttpResponseRedirect('/index')
def add_view(request):
    if request.method=='GET':
        return render(request,'addd.html')
    elif request.method=='POST':
        x=request.POST.get('x')
        if not x:
            return HttpResponse('please give me a number')
        x=int(x)
        y=request.POST.get('y')
        if not y:
            return HttpResponse('please give me a number')
        y=int(y)
        op=request.POST.get('op')
        result=0
        if op=="add":
            result=x+y
        elif op=='sub':
            result=x-y
        elif op=='mul':
            result=x*y
        elif op=='div':
            result=x/y
        return render(request,'addd.html',locals())
def test_if_view(request):
    va1=3
    dic={'va1':va1}
    return render(request,'test_if.html',dic)
def test_for(request):
    lst=['北京','上海','济南','asjdhfGTT']
    return render(request,'test_for.html',locals())
def shebao(request):
    if request.method=='GET':
        return render(request,'shebao.html')
    elif request.method=='POST':
        base=request.POST.get('base')
        if not base:
            return HttpResponse('please give me a number')
        base=int(base)
        new_base=max(min(base,23188),3082)
        is_city=request.POST.get('is_city')
        yl_gr=new_base*0.08
        yl_dw=new_base*0.19
        if is_city==1:
            sy_gr=new_base*0.002
        else:
            sy_gr=new_base*0
        return render(request,'shebao.html',locals())

def test_static(request):
    return render(request,'test_static.html')