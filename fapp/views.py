from django.shortcuts import render,redirect

from .forms import MovieForm

from.models import Movie
 

from django.core.files.storage import FileSystemStorage



# Create your views here.


def demo(request):

    movie = Movie.objects.all()
    return render(request,'index.html',{'movie':movie})





def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        year = request.POST['year']
        description = request.POST['desc']
        image = request.FILES['image']


        movies = Movie(Name=name, Year=year, Description=description, image=image)

        movies.save()

        return redirect('fapp:demo')
    return render(request, 'home.html')

#  Name from database , name from above function




def update(request,id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('fapp:demo')
    return render(request, 'edit.html',{'form' : form , 'movie':movie})
    


def delete(request,id):
    if request.method=='POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('fapp:demo')
    return render (request,'delete.html')










