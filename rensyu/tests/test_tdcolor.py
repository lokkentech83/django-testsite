from django.test import TestCase
from django.urls import reverse

# 테스트를 위해 모델 import
from rensyu.models import TranditionalColor


# 테스트 파일 분리시에는 prefix test_를 붙여 파일을 분리한다.
# python manage.py test rensyu/tests 로 해당폴더의 테스트 실행
# @see https://stackoverflow.com/a/20932450

def insert_data_traditionalColor(color_name, category_code, rgb_code, r_num, g_num, b_num, cymk_code):
    # tdcolor = TranditionalColor(color_name=color_name, category_code=category_code, rgb_code=rgb_code, r_num=r_num, g_num=g_num, b_num=b_num, cymk_code=cymk_code)
    # return tdcolor.save()
    return TranditionalColor.objects.create(color_name=color_name, category_code=category_code, rgb_code=rgb_code, r_num=r_num, g_num=g_num, b_num=b_num, cymk_code=cymk_code)



class tdColorTests(TestCase):
    
    # DB의 해당테이블의 데이터를 가지고 가는것을 확인.
    # 1. 데이터 없음.
    def test1(self):

        response = self.client.get(reverse("rensyu:tdcolor"))

        # http상태코드 확인
        self.assertEqual(response.status_code, 200)
        # 템플릿html의 헤더 확인
        self.assertContains(response, "한국의 전통색상")

        # 테스트시에는 가상의 DB환경을 만들어 테스트가 실행되므로 DB가 비어있는 상태를 가정함.
        # 데이터 insert없을시
        self.assertQuerysetEqual(response.context["color_list"], [])

    def test2(self):
        # 테스트데이터 작성
        testData = insert_data_traditionalColor("테스트색","0001","111111",1,2,3,"111111")

        response = self.client.get(reverse("rensyu:tdcolor"))

        # 데이터 insert시
        self.assertQuerysetEqual(response.context["color_list"], [testData])
        
    
