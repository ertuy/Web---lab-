from django import forms
from django.http import Http404
from .models import Article
from django.shortcuts import render,redirect
def create_post(request):
    if not request.user.is_anonymous():
        if request.method == "POST":
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
            }
            if form["text"] and form["title"]:
                Article.objects.create(text=form["text"],
                                       title=form["title"],
                                       author=request.user)
                return redirect('get_article', article_id=article.id)
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'post_edit.html', {})

    else:
        raise Http404