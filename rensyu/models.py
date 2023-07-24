from django.db import models

# python manage.py makemigrations을 통해 이 변경사항에 대한 마이그레이션을 만드세요.
# python manage.py migrate 명령을 통해 변경사항을 데이터베이스에 적용하세요.


"""
한국의 전통색
"""
# 전통색 관리 테이블
class TranditionalColor(models.Model):
    color_name = models.CharField(max_length=50
                                  , help_text="색깔 이름")
    category_code = models.CharField(max_length=4
                                     ,help_text="카테고리 코드")
    rgb_code = models.CharField(max_length=6
                                , help_text="rgb 코드")
    r_num = models.IntegerField(help_text="r값")
    g_num = models.IntegerField(help_text="g값")
    b_num = models.IntegerField(help_text="b값")
    cymk_code = models.CharField(max_length=15
                                 , help_text="cymk 코드")

    def __str__(self) -> str:
        return self.color_name + " : " + self.rgb_code
    def getCategoryName(self) :
        # 카테고리명 관리테이블의 카테고리코드와 일치하는 카테고리명칭 반환
        return TranditionalColorCategory.objects.get(pk = self.category_code).category_name

# 전통색의 카테고리명 관리 테이블
class TranditionalColorCategory(models.Model):
    category_code = models.CharField(primary_key=True, max_length=4) # 카테고리 코드 ex) 0001
    category_name = models.CharField(max_length=50) # 카테고리 명칭 ex) 무채색계(無彩色界)

    def __str__(self) -> str:
        return self.category_name



"""
유저관리 CRUD 테스트
"""

# 性別
CODE_GENDER = 2
# 血液型
CODE_BLOOD_TYPE = 3

# コードリスト
class CodeList(models.Model):
    code = models.CharField(max_length=4, unique=True) # 코드 ex) 0001
    code_name = models.CharField(max_length=100) # 코드명칭 ex) 성별
    code_description = models.CharField(max_length=1000) # 코드관련 설명 ex) 성별 관리용 코드, 남/여/기타등으로 데이터를 관리.

    def __str__(self) -> str:
        return self.code_name
    

# コード管理
# 장고 모델에서는 single-column primary key만을 지원하므로 unique제약조건을 이용하여 복수칼럼에 대한 제약을 걸 수 밖에 없다고 한다.
class CodeManage(models.Model): 
    code_subcode = models.CharField(max_length=4) # 코드 ex) (0001)0001
    code_subname = models.CharField(max_length=100) # 코드 ex) (0001)0001 男
    codelist = models.ForeignKey(CodeList, on_delete=models.CASCADE)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['code', 'code_subcode'], name='CodeManage_constraints_1'
    #         )
    #         # models.ForeignKey("rensyu.CodeList", verbose_name=("code"), on_delete=models.CASCADE)
    #     ]

# ユーザーリスト
class UserList(models.Model):
    kanzi_name = models.CharField(max_length=50) #이름(한자)
    kana_name = models.CharField(max_length=60) #이름(카나)
    age = models.IntegerField() # 연령
    birthdate = models.DateField() # 생일
    gender = models.CharField(max_length=4) # 관리코드 0001
    blood_type = models.CharField(max_length=4) # 관리코드 0002
    mail_address = models.CharField(max_length=100)
    tel_num = models.CharField(max_length=15)
    mobile_tel_num = models.CharField(max_length=15)
    post_num = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    company_name = models.CharField(max_length=50)

    # TODO update_date 추가하기
    # TODO create_date 추가하기 default가 date.now()

    def gender_text(self) :
        # 성별의 명칭 취득하기처리
        return CodeList.objects.get(pk=CODE_GENDER).codemanage_set.get(code_subcode=self.gender).code_subname
    
    def blood_type_text(self) :
        # 성별의 명칭 취득하기처리
        return CodeList.objects.get(pk=CODE_BLOOD_TYPE).codemanage_set.get(code_subcode=self.gender).code_subname
