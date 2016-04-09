from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
# Create your views here.

def index(request):
	#template = loader.get_template('sharefilms/index.html')
	context = {'parm': 123456}
	return render(request, 'sharefilms/index.html', context)

def create_dirs():
	pass