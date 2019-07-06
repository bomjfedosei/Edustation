from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import BotDialog
from .models import Connections
from .models import Courses
from .models import Schools


def QueryToDict(query):
    response = dict()
    response['id'] = query['id']
    response['dialog'] = query['dialog']
    return response

def index(request):
    return render(request, 'index.html')

def get_dialog(request, id):
    dialog = Connections.objects.filter(firstfrase = id).values()
    response = dict()
    for i in range(len(dialog)):
        bd = BotDialog.objects.filter(id = dialog[i]['secondfrase']).values()
        if (bd[0]['owner'] == True):
            bot = dict()
            bot['id'] = bd[0]['id']
            bot['dialog'] = bd[0]['dialog']
            response['bot'] = bot
        else:
            bot = dict()
            bot['id'] = bd[0]['id']
            bot['dialog'] = bd[0]['dialog']
            response[str(i)] = bot
            print(response)
    return JsonResponse(response)

def get_all_dialogs(request):
    return JsonResponse(dialogs)

def add_dialog(request):
    return render(request, 'addD.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def search(request, searchstring):
    search = Courses.objects.filter(title__icontains=searchstring).values()
    sear = dict()
    for i in range(len(search)):
        sear[str(i)] = search[i]
        ids = search[i]['school']
        school = Schools.objects.filter(id = ids).values()[0]['name']
        search[i]['school'] = school
        if (i == 2):
            break
    return JsonResponse(sear)
