from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from blog.models import Article
from django.core.paginator import Paginator

def hello_world(request):
    return HttpResponse("Hello World12321312312312")

def article_content(request):
    article = Article.objects.all()[0]
    return_str = 'ID:{},标题:{}，副标题:{},内容：{},日期:{}'.format(
        article.article_id,
        article.title,
        article.brief_content,
        article.content,
        article.publish_date
    )
    return HttpResponse(return_str)

def get_index_page(request):
    next_page = 0
    previous_page = 0
    # 传参
    current_page = request.GET.get('page')
    if current_page:
        current_page = int(current_page)
    else:
        current_page = 1
    # print('page param:', page)
    all_article = Article.objects.all()
    # 分页
    paginator = Paginator(all_article, 5)
    # 共多少页
    page_num = paginator.num_pages
    print('page_num param:', paginator.num_pages)
    page_article_list = paginator.page(current_page)
    # 上一页
    if page_article_list.has_previous():
        previous_page = current_page - 1
    else:
        previous_page = page_num
    # 下一页
    if page_article_list.has_next():
        next_page = current_page + 1
    else:
        next_page = 1
    # 最近10篇文章
    top10_article_list = Article.objects.order_by('-publish_date')[:10]

    return render(request, 'blog/index.html',
                  {
                      "article_list": page_article_list,
                      "page_num": range(1, page_num + 1),
                      "current_page": current_page,
                      "previous_page": previous_page,
                      "next_page": next_page,
                      "top10_article_list": top10_article_list
                  }
                  )

def get_detail_page(request, article_id):
    article_list = Article.objects.all()
    current_article = None
    previous_article = None
    next_article = None
    previous_index = 0
    next_index = 0
    for index, article in enumerate(article_list):
        if article.article_id == article_id:
            current_article = article
            if index == 0:
                previous_index = len(article_list) - 1
                next_index = index + 1
            elif index == len(article_list) - 1:
                previous_index = index - 1
                next_index = 0
            else:
                previous_index = index - 1
                next_index = index + 1
            previous_article = article_list[previous_index]
            next_article = article_list[next_index]
            break;

    current_article.content = current_article.content.split('\n')
    return render(request, 'blog/detail.html',
                  {
                      "current_article": current_article,
                      "previous_article": previous_article,
                      "next_article": next_article
                  }
                  )