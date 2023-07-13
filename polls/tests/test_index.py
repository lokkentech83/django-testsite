import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from polls.models import Question

# 테스트 파일 분리시에는 prefix test_를 붙여 파일을 분리한다.
# python manage.py test polls/tests로 해당폴더의 테스트 실행
# @see https://stackoverflow.com/a/20932450

def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    
    # 데이터 없는 케이스
    # def test_no_question(self):
    #     response = self.client.get(reverse("polls:index"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "No polls are available.") # 메시지가 표시되는것을 확인
    #     self.assertQuerysetEqual(response.context["latest_question_list"], [])
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    # def test_past_question(self):
        
    #     question = create_question("Past question", days=-30)
    #     response = self.client.get(reverse("polls:index"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertNotContains(response, "No polls are available.") # 메시지가 표시되지 않는것을 확인
    #     self.assertQuerysetEqual(response.context["latest_question_list"], [question])
    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )