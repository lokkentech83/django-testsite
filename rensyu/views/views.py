from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse

from ..models import UserList

# Create your views here.
# index
def index(request):

    context = {
        "date" : timezone.now(),
    }
    return render(request, 'rensyu/index.html', context)
    # return HttpResponse("Hello, world. You're at the polls index.")


# 유저관리 페이지
def userlist(request):
    # 유저리스트 가져오기
    user_list = UserList.objects.all()

    # userlistObj = UserList.objects.create(kanzi_name="鈴木 由紀",kana_name="すずき ゆき", age="33", birthdate="1990-05-17", gender="0002", blood_type="0001", mail_address="suzukiyuki@example.ne.jp", tel_num="093-529-8413", mobile_tel_num="080-0844-9365", post_num="834-8774", address="福岡県北九州市小倉北区下富野2-2-304", company_name="株式会社H＆K")
    # print(userlistObj)
    context = {
        "user_list" : user_list
    }
    return render(request, 'rensyu/userlist/userList.html', context)

# 유저관리 상세
def userDetail(request, id):
    
    # 유저관리 테이블의 id로 데이터 취득
    user_data = get_object_or_404(UserList, pk=id)
    

    context = {
        "user_data" : user_data
    }
    return render(request, 'rensyu/userlist/userDetail.html', context)

# 유저관리 상세
def userModify(request, id):
    # 유저 작성 페이지
    context = {
        # "user_list" : user_list
    }
    return render(request, 'rensyu/userlist/userDetail.html', context)

# 유저관리 페이지
def userCreate(request):
    # 유저 작성 페이지
    context = {
        # "user_list" : user_list
    }
    return render(request, 'rensyu/userlist/userCreate.html', context)