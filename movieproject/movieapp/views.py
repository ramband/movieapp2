from django.shortcuts import render
from movieapp.models import movie
from movieapp import forms


# Create your views here.
def home(request):
	return render(request,'movieapp/abc.html')


def seelist(request):
	x=movie.objects.all()
	my_dict={'x':x}
	return render(request,'movieapp/seelist.html',context=my_dict)

def xyz(request):
	x=forms.movieform()
	print(request.method)
	if request.method=="POST":
		x=forms.movieform(request.POST)
		if x.is_valid():
			x.save(commit=True)
		return render(request,'movieapp/home2.html')
		
	return render(request,'movieapp/home.html',{'x': x})

def aboutus(request):
	return render(request,'movieapp/aboutus.html')