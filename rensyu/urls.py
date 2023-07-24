from django.urls import path

from .views import views
from .views import views_tdColor

# 어플리케이션이 여러개 있을때 해당 어플리케이션을 특정하기 위한 namespace를 지정
app_name = "rensyu"
urlpatterns = [
    # 인덱스 /rensyu/
    path("", views.index, name="index"),

    # 전통색 /rensyu/tdcolor/
    path("tdcolor/", views_tdColor.tdcolor, name="tdcolor"),

    # 유저관리 /rensyu/userlist/
    path("userlist/", views.userList, name="userList"),

    # 유저관리 - 상세정보 /rensyu/userlist/detail/
    path("userlist/detail/<int:id>", views.userDetail, name="userDetail"),

    # 유저관리 - 수정 /rensyu/userlist/modify/1
    path("userlist/modify/<int:id>", views.userModify, name="userModify"),

    # 유저관리 - 수정 /rensyu/userlist/modify/1/upd
    path("userlist/modify/<int:id>/upd", views.updateUserData, name="updateUserData"),

    # 유저관리 - 수정 /rensyu/userlist/create/
    path("userlist/create/", views.userCreate, name="userCreate"),

    # 유저관리 - 삭제 /rensyu/userlist/delete/1
    path("userlist/delete/<int:id>", views.userDelete, name="userDelete"),

    # # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),


    # path("", views.IndexView.as_view(), name="index"),
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
    
]