from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from todolist.models import UserData
import todolist.models as e


@csrf_exempt
def addTask(request):
    response = HttpResponse()
    print(request.method)
    if request.method=='POST':
        print(request.body.decode('utf-8'))
        json_body=json.loads(request.body.decode('utf-8'))
        list_of_tasks=json_body['tasks']
        print(list_of_tasks)
        status_of_tasks=json_body['status']
        print(status_of_tasks)
        c=0
        if UserData.objects.filter(user_nam=json_body['username']).count()==0: #Check if a user with the given username exists in the database
            return HttpResponse(json.dumps({'report':'USER_DOES_NOT_EXIST'}))
        else:
            query=UserData.objects.filter(user_nam=json_body['username']) #Query the database to get DB entry with the given username.
            tasks=UserData.objects.values('user_nam') 
            for i in range(len(tasks)):
                if(tasks[i]['user_nam']==json_body['username']):
                    index=i
                    break
            taskfull=UserData.objects.values()
            dictstr=taskfull[index]['taskdata']
            q=json.loads(dictstr)
            for i in range(len(json_body['tasks'])):
                q[json_body[i]]=status_of_tasks[i]
            print(q)
            query.update(taskdata=json.dumps(q))
    response.write('SUccess connection')
    return response

def getTask(request):
    if request.method=='GET':
        jsonbody=json.loads(request.body.decode('utf-8')) # Request body
        getusernames=UserData.objects.values('user_nam')
        index=-1
        for i in range(len(getusernames)):
            if(getusernames[i]['user_nam']==jsonbody['username']):
                index=i
                break
        taskfull=UserData.objects.values()
        if index<0:
            return HttpResponse('NO_DATA')
        else:
            print('4')
            dictstr=taskfull[index]['taskdata']
            return HttpResponse(dictstr)
    


    
    
