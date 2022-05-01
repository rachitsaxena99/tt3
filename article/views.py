from django.shortcuts import render , redirect
from article.models import Tag , Article , RelationArticle, CommentArticle
from django.contrib.auth.models import User

def index(request):
    return render(request , 'homepage.html')


def topics(request):
    tags = Tag.objects.all()
    params = {
        'tags':tags
    }
    return render(request , 'article/topics.html' , params)

def articles(request , pk):
    articles = Article.objects.filter(tags__name__in = [pk])

    params = {
        'name':pk,
        'status': True if len(articles) else False,
        'articles': articles
    }

    return render(request , 'article/index.html' , params )

def article_detail(request , pk):
    article = Article.objects.get(id=pk)
    para  = str(article.content).split('/')
    comments = CommentArticle.objects.filter(article_id =article.id).order_by('-date')

    params  ={
        'article':article,
        'para':para,
        'comments':comments
    }
    return render(request , 'article/article_detail.html' ,params)



def newComment(request , pk):
    try:
        article = Article.objects.get(id=pk)
        user = User.objects.get()
        if request.method=='POST':
            commentText = request.POST.get('commentText')
            if commentText is not None:
                comment = CommentArticle.objects.create(article= article , user = user , reaction=commentText)
                comment.save()
                return redirect('article_detail',pk=article.id)
    except Exception as E:
        raise Exception(str(E))
