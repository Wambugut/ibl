from django.shortcuts import render
def get_context_data():
 return{
  'data':'some data'
 }
def index(request):
 template= 'webapp/index.html'
 return render (request, template, {})
