import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

# Create your tests here.

# 테스트 할 때는, 많이 할 수록 좋습니다.¶
# 우리의 테스트가 통제 불능으로 성장하고있는 것처럼 보일 수 있습니다. 이 속도라면 곧 우리의 어플리케이션에서 보다 우리의 테스트의 코드가 더 많아질 것이고, 나머지 코드의 우아한 간결함과 비교했을 때, 반복하는 것은 미학적입니다.
# @see https://docs.djangoproject.com/ko/4.2/topics/testing/

# Model에 대한 테스트 클래스
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self) :
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        self.assertIs(future_question.was_published_recently(), False)

    # recently에 해당하지 않는경우
    def test_1(self) :
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_2(self) :
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
    
def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

# ▽▽▽indexTest.py 로 이동
# class QuestionIndexViewTests(TestCase):
    
#     # 데이터 없는 케이스
#     # def test_no_question(self):
#     #     response = self.client.get(reverse("polls:index"))
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertContains(response, "No polls are available.") # 메시지가 표시되는것을 확인
#     #     self.assertQuerysetEqual(response.context["latest_question_list"], [])
#     def test_no_questions(self):
#         """
#         If no questions exist, an appropriate message is displayed.
#         """
#         response = self.client.get(reverse("polls:index"))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "No polls are available.")
#         self.assertQuerySetEqual(response.context["latest_question_list"], [])

#     # def test_past_question(self):
        
#     #     question = create_question("Past question", days=-30)
#     #     response = self.client.get(reverse("polls:index"))
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertNotContains(response, "No polls are available.") # 메시지가 표시되지 않는것을 확인
#     #     self.assertQuerysetEqual(response.context["latest_question_list"], [question])
#     def test_past_question(self):
#         """
#         Questions with a pub_date in the past are displayed on the
#         index page.
#         """
#         question = create_question(question_text="Past question.", days=-30)
#         response = self.client.get(reverse("polls:index"))
#         self.assertQuerySetEqual(
#             response.context["latest_question_list"],
#             [question],
#         )

#     def test_future_question(self):
#         """
#         Questions with a pub_date in the future aren't displayed on
#         the index page.
#         """
#         create_question(question_text="Future question.", days=30)
#         response = self.client.get(reverse("polls:index"))
#         self.assertContains(response, "No polls are available.")
#         self.assertQuerySetEqual(response.context["latest_question_list"], [])

#     def test_future_question_and_past_question(self):
#         """
#         Even if both past and future questions exist, only past questions
#         are displayed.
#         """
#         question = create_question(question_text="Past question.", days=-30)
#         create_question(question_text="Future question.", days=30)
#         response = self.client.get(reverse("polls:index"))
#         self.assertQuerySetEqual(
#             response.context["latest_question_list"],
#             [question],
#         )

#     def test_two_past_questions(self):
#         """
#         The questions index page may display multiple questions.
#         """
#         question1 = create_question(question_text="Past question 1.", days=-30)
#         question2 = create_question(question_text="Past question 2.", days=-5)
#         response = self.client.get(reverse("polls:index"))
#         self.assertQuerySetEqual(
#             response.context["latest_question_list"],
#             [question2, question1],
#         )
# △△△indexTest.py 로 이동
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)