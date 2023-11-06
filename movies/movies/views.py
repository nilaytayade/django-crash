

# from django.http import HttpResponse
# from django.shortcuts import render
# from .models import Movies
# from django.shortcuts import redirect

from django.shortcuts import render, get_object_or_404, redirect
from .models import Url
import random
import string

# data=Movies.objects.all()

# def movies(request):
#     return render(request,'movies/movies.html',{'movies':data})    
# def login(request):
#     return redirect('https://git-scm.com/download/win')
# def home(request):
#     return HttpResponse("this is home")

def home(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        url = Url(original_url=original_url, short_code=short_code)
        url.save()
        return render(request, 'shortener/home.html', {'short_url': f'{request.build_absolute_uri("/")}{short_code}'})
    return render(request, 'shortener/home.html')

def redirect_to_original(request, short_code):
    url = get_object_or_404(Url, short_code=short_code)
    return redirect(url.original_url)