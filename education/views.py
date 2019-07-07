from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import BotDialog
from .models import Connections
from .models import Courses
from .models import Schools
from .models import Chatbot_User

def QueryToDict(query):
    response = dict()
    response['id'] = query['id']
    response['dialog'] = query['dialog']
    return response

def index(request):
    return render(request, 'index.html')

def form(request):
    return render(request, 'form.html')

def form_add_user(request):
    name = request.GET;
    print(name)
    return JsonResponse({'status': '4'})


def get_dialog(request, id):
    # if (id == 7):
    #    name = request.GET.get("back", "WHO?")
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
    return JsonResponse(response)

def get_all_dialogs(request):
    return JsonResponse(dialogs)

def add_dialog(request):
    return render(request, 'addD.html')

def chatbot(request):
    return render(request, 'chat_bot.html')

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

def result(request):
    return render(request, 'result.html')

def card_detail(request, path):
    search = Courses.objects.filter(page_title__icontains=path).values()
    sear = search[0]
    ids = sear['school']
    sear['school'] = Schools.objects.filter(id = ids).values()[0]['name']
    return render(request, 'cart_detail.html', context = sear)
