from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse

from ..models import TranditionalColor

# 전통색
def tdcolor(request):
    # 컬러 전부 가져오기
    color_list = TranditionalColor.objects.all().order_by("id") 
    context = {
        "date" : timezone.now(),
        "color_list" : color_list
    }
    return render(request, 'rensyu/tranditionalColor.html', context)