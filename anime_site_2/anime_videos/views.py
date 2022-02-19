from django.shortcuts import render,redirect
from .models import AnimeDB
from django.core.paginator import Paginator


def main_view(request):
    anime_base = AnimeDB.objects.order_by('?')
    animes = []
    paginator = Paginator(anime_base, 20)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    for anime in page.object_list:
        anime.genres = [r for r in anime.genres.split(', ') if r != '']
        animes.append(anime)
    return render(request, 'main.html', {'title':'SITE_NAME', 'animes':animes, 'page':page})


def video_view(request, id):
    base = AnimeDB.objects.get(id=id)
    genres = [r for r in base.genres.split(', ') if r != '']
    url = ''
    for i in base.url.split(', '):
        if i != '' and 'serial' in i:
            url = i
    return render(request, 'video.html', {'title':base.title, 'anime':base, 'url':url, 'genres':genres})


def genre_view(request, genre):
    base = AnimeDB.objects.filter(genres__contains=genre)
    animes = []
    paginator = Paginator(base, 20)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    for anime in page.object_list:
        anime.genres = [r for r in anime.genres.split(', ') if r != '']
        animes.append(anime)
    return render(request, 'main.html', {'title': genre, 'animes': animes, 'page': page})


def feedback_view(request):
    return render(request, 'feedback.html', {'title':'Обратная связь'})


def custom_handler404(request, exception):
    return render(request, '404.html')


def custom_handler500(request):
    return render(request, '500.html')

def top100_view(request):
    base = AnimeDB.objects.order_by('-likes')[:100]
    animes = []
    paginator = Paginator(base, 20)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    for anime in page.object_list:
        anime.genres = [r for r in anime.genres.split(', ') if r != '']
        animes.append(anime)
    return render(request, 'main.html', {'title': "Топ 100 аниме", 'animes': animes, 'page': page})