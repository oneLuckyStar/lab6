# Create your views here.
# -- coding: cp1251 --
from models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
def archive(request):
    try:
        name = request.user.get_full_name()
    except:
        name = ''
    return render(request, 'archive.html', {"posts": Article.objects.all(), "auth": request.user.is_authenticated(),"name": name})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if not request.user.is_anonymous():
        if request.method == "POST":
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
                }
            if form["text"] and form["title"]:
                articles = Article.objects.all()
                for article in articles:
                    if article.title.lower() == form.get('title').lower():
                        form['errors'] = u"Имя повторяется"
                        return render(request, 'create_post.html', {'form': form})
                article = Article.objects.create(text=form["text"],
                                       title=form["title"],
                                       author=request.user)
                return redirect('get_article', article_id=article.id)
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404
    
def create_puser(request):
    if request.user.is_anonymous():
        if request.method == "POST":
            form = {
                'login':request.POST["name"],
                'mail': request.POST["mail"],
                'pas': request.POST["pas"]
                }
            if form["login"] and form["mail"] and form["pas"]:
                users = User.objects.all()
                for user in users:
                    if user.username.lower() == form.get('login').lower():
                        form['errors'] = u"Имя повторяется"
                        return render(request, 'create_user.html', {'form': form})
                user = User.objects.create_user(form.get('login'),form.get('mail'),form.get('pas'))
                user = authenticate(username=form.get('login'), password=form.get('pas'))
                login(request,user)   
                return redirect('get_articles')
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_user.html', {'form': form})
        else:
            return render(request, 'create_user.html', {})
    else:
        raise Http404

def create_auto(request):
    if request.user.is_anonymous():
        if request.method == "POST":
            form = {
                'login': request.POST["login"],
                'pas': request.POST["pas"]
                }
            if form["login"] and form["pas"]:
                user = authenticate(username=form.get('login'), password=form.get('pas'))
                if user is not None:
                    login(request,user)
                    return redirect('get_articles')
                else:
                    form['errors']= u"Неверное имя пользователя или пароль"
                    return render(request, 'auto.html', {'form': form})
        else:
            return render(request, 'auto.html', {})
    else:
        raise Http404
def create_logout(request):
    logout(request)
    return redirect('get_articles')
                
