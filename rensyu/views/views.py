from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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
def userList(request):
    # 유저리스트 가져오기
    user_list = UserList.objects.all()

    # userlistObj = UserList.objects.create(kanzi_name="鈴木 由紀",kana_name="すずき ゆき", age="33", birthdate="1990-05-17", gender="0002", blood_type="0001", mail_address="suzukiyuki@example.ne.jp", tel_num="093-529-8413", mobile_tel_num="080-0844-9365", post_num="834-8774", address="福岡県北九州市小倉北区下富野2-2-304", company_name="株式会社H＆K")
    # print(userlistObj)
    context = {
        "user_list" : user_list
    }
    return render(request, 'rensyu/userlist/list.html', context)

# 유저관리 상세
def userDetail(request, id):
    
    # 유저관리 테이블의 id로 데이터 취득
    user_data = get_object_or_404(UserList, pk=id)
    
    context = {
        "user_data" : user_data
    }
    return render(request, 'rensyu/userlist/detail.html', context)

# 유저관리 상세
def userModify(request, id):
    # 유저관리 테이블의 id로 데이터 취득
    user_data = get_object_or_404(UserList, pk=id)
    
    # 수정용 화면으로
    context = {
        "user_data" : user_data
    }
    return render(request, 'rensyu/userlist/modify.html', context)


# 수정내용 등록
def updateUserData(request, id) :
    # 유저관리 테이블의 id로 데이터 취득
    user_data = get_object_or_404(UserList, pk=id)

    # TODO validate

    # 입력된 데이터로 변경
    user_data.kanzi_name = request.POST["kanzi_name"]


    # TODO updated_date 수정하기
    user_data.save()

    # detail 페이지로 이동하기
    return HttpResponseRedirect(reverse("rensyu:userDetail", args=(user_data.id,)))

# 유저관리 데이터 생성하기
def userCreate(request):
    # 유저 작성 페이지
    context = {
        # "user_list" : user_list
    }
    return render(request, 'rensyu/userlist/create.html', context)

# 유저관리 데이터 삭제
def userDelete(request, id):
    # 데이터 조회
    user_data = get_object_or_404(UserList, pk=id)
    print(user_data)

    # 해당데이터 삭제하기
    user_data.delete()

    return HttpResponseRedirect(reverse("rensyu:userList")) # "/polls/3/results/"
