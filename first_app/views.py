from django.shortcuts import render
import random 
# Create your views here.
# django -> 함수 첫번째 인자는 항상 request
# render html문서 완성시켜서 결과물 출력

def index(request):
    return render(request, 'index.html')
    

def root(request): # 정적 웹
    return render(request, 'root.html')


def hello(request): # 동적 웹
    username = 'joo'
    
    context = {
        'username': username,

    }
    return render(request, 'hello.html', context)

def lunch(request):
    menus = ['김밥', '라면', '돈까스']

    pick = random.choice(menus) #choice 랜덤한 한 개 

    context = {
        'pick': pick
    }
    return render(request, 'lunch.html', context)


def lotto(request):
    lotto = random.sample(range(1, 46), 6)

    context = {
        'lotto': lotto
    }
    return render(request, 'lotto.html', context)