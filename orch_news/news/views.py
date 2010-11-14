from django.http import HttpResponse
from django.shortcuts import render_to_response
from news.models import News
import datetime

def all_news(request):
	nows = datetime.datetime.now()
	news_show = News.objects.order_by('-order')
	return render_to_response('news.html', {'news_show':news_show, 'nows':nows})