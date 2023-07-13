import datetime

from django.db import models
from django.utils import timezone

from django.contrib import admin


# python manage.py makemigrations을 통해 이 변경사항에 대한 마이그레이션을 만드세요.
# python manage.py migrate 명령을 통해 변경사항을 데이터베이스에 적용하세요.
# 변경사항은 migrations에 이력처럼 넘버링되어 남는다.
# Create your models here.
class Question (models.Model) :
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    

    # 자바로 치면 toString에 해당하는 메소드
    def __str__(self) -> str:
        return self.question_text
    
    # decorator 어노테이션 느낌으로 해당 함수에 admin관련 내용들을 추가 가능하다.
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    # 신규로 메소드를 추가해서 해당 레코드에 대한 판단
    def was_published_recently(self) :
        # #4의 테스트를 통한 버그수정
        now = timezone.now()
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice (models.Model) :
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text