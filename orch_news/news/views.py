from django.http import HttpResponse
from django.shortcuts import render_to_response
from news.models import News

def all_news(request):
	news_show = News.objects.all()
	return render_to_response('news.html', {'news_show':news_show})