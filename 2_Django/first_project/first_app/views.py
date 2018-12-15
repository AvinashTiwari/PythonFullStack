from django.shortcuts import render

# Create your views here.
def index(request):
    mydict = {'insert_content': "Hello I am from first app "}
    return render(request, 'first_app/index.html', context=mydict)
