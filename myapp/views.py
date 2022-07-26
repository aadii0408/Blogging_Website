from django.shortcuts import render, redirect
from .models import Student, Blog

def loadhtml(request):
    return render(request, "hello.html")


def signup(request):
    if request.session.has_key('is_login'):
        return redirect('/home')
    return render(request, "insert.html")


def datasave(request):
    if request.POST:
        sid = request.POST['sId']
        sname = request.POST['sName']
        semail = request.POST['sEmail']
        spassword = request.POST['sPassword']
        obj = Student(sId=sid, sName=sname, sEmail=semail, sPassword=spassword)
        obj.save()
    return redirect('/login')


def login(request):
    if request.session.has_key('is_login'):
        return redirect('/home')
    if request.POST:
        semail = request.POST['sEmail']
        spassword = request.POST['sPassword']
        count = Student.objects.filter(sEmail=semail, sPassword=spassword).count()
        if count > 0:
            request.session['is_login'] = True
            request.session['user_id'] = Student.objects.values('id').filter(sEmail=semail, sPassword=spassword)[0][
                'id']
            return redirect('/home')
        else:
            return redirect('/#')
    return render(request, "login.html")


def home(request):
    data = Blog.objects.all
    return render(request, "home.html", {"data": data})


def aboutus(request):
    return render(request, "aboutus.html")


def company(request):
    return render(request, "company.html")


def logout(request):
    del request.session['is_login']
    return redirect('/login')


def createPost(requset):
    if requset.POST:
        uid = requset.POST['user_id']
        pname = requset.POST['publisherName']
        ptitle = requset.POST['title']
        pdetail = requset.POST['postDetail']
        img = requset.FILES['img']
        obj = Blog(publisherName=pname, title=ptitle, postDetail=pdetail, image=img)
        obj.user_id_id = uid
        obj.save()
        return redirect('/home')
    return render(requset, "createPost.html")