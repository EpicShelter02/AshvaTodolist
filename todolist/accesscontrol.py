from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from todolist.models import UserData
import todolist.models as e

@csrf_exempt
def sign_up(request):
    if request.method=='POST':
        jsonbody=json.loads(request.body.decode('utf-8')) #  Request body
        q = e.UserData(user_nam=jsonbody['username'],pass_wd=jsonbody['password'],taskdata={})
        q.save()
        print(json.dumps({'report':'SIGNUP_SUCCESS'}))
        return HttpResponse(json.dumps({'report':'SIGNUP_SUCCESS'}))
@csrf_exempt
def sign_in(request):
    if request.method=='POST':
        d=json.loads(request.body.decode('utf-8')) # Request body
        tasks=UserData.objects.values('user_nam')
        exist=False
        for i in range(len(tasks)):
            if(tasks[i]['user_nam']==d['username']):
                exist=True
                break
            else:
                exist=False
        if exist:
            return HttpResponse(json.dumps({'report':'SIGNIN_SUCCESS'}))
        else:
            return HttpResponse(json.dumps({'report':'SIGNIN_FAILED'}))