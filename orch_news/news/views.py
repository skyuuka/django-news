from django.http import HttpResponse
from django.shortcuts import render_to_response

def all_news(request):
	return HttpResponse("All News here")