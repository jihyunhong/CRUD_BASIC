from django.shortcuts import render, HttpResponse

# Create your views here.


def post_list(reuqest):
    return HttpResponse('글 리스트')
