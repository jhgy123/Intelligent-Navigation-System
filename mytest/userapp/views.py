from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from userapp.models import User


def login_user(request):
    if request.method == "GET": #get请求处理
        data = {}
        return render(request, 'login.html', context=data)
    elif request.method == "POST": #post请求处理
        uid = request.POST.get('username')
        upaw = request.POST.get('password')
        users = User.objects.filter(u_id=uid)
        if users.exists():  #用户存在
            user = users.first()
            print(upaw,user.u_password)
            if str(upaw)==str(user.u_password):  #密码正确
                if not user.is_delete: #用户未被删除
                    username = user.u_name
                    request.session['username'] = username
                    #test
                    data = {
                        "test": "登陆成功，跳转主页面",
                    }
                    return render(request, 'test.html', context=data)
                    # return redirect(reverse("user:home"))
                else:#用户被删除
                    data = {
                        "test": "账号状态异常提示,请联系管理员处理后再登录",
                    }
                    return render(request, 'test.html', context=data)
                    # return render(request, 'notice.html', acontext=data)
            else: #密码错确
                data = {
                    "test": "密码错确",
                }
                return render(request, 'test.html', context=data)
        else:#用户不存在处理
            data = {
                "test": "用户不存在",
            }
            return render(request, 'test.html', context=data)
        # return render(request, 'login_error_s.html')