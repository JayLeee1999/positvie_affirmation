from django.shortcuts import redirect, render

# Create your views here.
# def positive(request):
#     return render (request , 'positive.html',)

from django.shortcuts import render
from community.forms import Form
from community.models import Article

def positive(request):
    # print("aaa")
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        emotion = request.POST.get('emotion')
        affirmation = request.POST.get('affirmation')
        print(nickname, emotion, affirmation)
        
        try:

            # 모델 클래스를 통해 저장
            article = Article(nickname=nickname, emotion=emotion, affirmation=affirmation)
            print(article)
            article.save()  # 모델 객체를 저장
            print("저장 성공")
            return redirect('/')
        except Exception as e:
            print("에러 상태 : ", e)
    else:
        form = Form()
    article_list = Article.objects.all()
    return render(request, 'positive.html', {'article_list': article_list})
 


# def positive(request):
#     # print("aaa")
#     if request.method == 'POST':
#         form = Form(request.POST)
#         print("폼 데이터:", form.data)  # 👉 입력된 데이터 확인
#         if form.is_valid():
#             article = form.save(commit=False)  # 👉 DB 저장 전 객체 생성
#             article.save()  # 👉 직접 저장 시도
#             return redirect('/')
#     else:
#         form = Form()
#     return render(request, 'positive.html', {'form':form})


