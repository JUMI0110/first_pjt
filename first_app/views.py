from django.shortcuts import render
from faker import Faker
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


def username(request, name): # urls.py에서 정의한 변수 이름을 두번째 인자
    context = {
        'name': name,
    }
    return render(request, 'username.html', context)


def cube(request, number):
    result = number ** 3

    context = {
        'result': result
    }
    return render(request, 'cube.html', context)


def posts(request):
    fake = Faker()

    fake_posts = []
    for i in range(100):
        fake_posts.append(fake.text())

    context = {
        'fake_posts': fake_posts,
    }
    return render(request, 'posts.html', context)

# ping.html에서 사용자의 데이터 받아오기
def ping(request):
    return render(request, 'ping.html')

def pong(request):
    # raise 강제로 오류를 실행 -> 페이지 정보확인
    # request.GET['title'] key값으로 접근
    title = request.GET.get('title') # dictionary의 get메소드로 접근(안정적)
    content = request.GET.get('content')

    context = {
        'title': title,
        'content': content,
    }
    return render(request, 'pong.html', context)