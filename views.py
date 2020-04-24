
from .models import Article
from django.shortcuts import render,redirect
from django.http import Http404
def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request,'article.html',{"post": post})
    except Article.DoesNotExist:
        raise Http404

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})
def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
            }
            if form["text"] and form["title"]:
                Article.objects.create(text=form["text"],
                                       title=form["title"],
                                       author=request.user)
                return redirect('get_article', article_id=article_id)
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'post_edit.html', {'form': form})
        else:
            return render(request, 'post_edit.html', {})

    else:
        raise Http404