from django.contrib import admin
from .models import Question, Choice


class ChoiceInline (admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields=["pub_date", "question_text"]

    # list_display = ["question_text", "pub_date"]
    list_display = ["question_text", "pub_date", "was_published_recently"]

    fieldsets = [
        (None, {"fields" : ["question_text"]}),
        # ( title , fields)
        ("Date information", {"fields" : ["pub_date"], "classes" : ["collapse"]})
    ]
    inlines = [ChoiceInline]

    # 해당 칼럼에대한 필터기능
    list_filter = ["pub_date"]

    

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)