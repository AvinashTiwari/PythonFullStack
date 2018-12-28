from django.shortcuts import render
from appTwo.models import User
# Create your views here.

def index(request):
    return render(request, 'app_two/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(reqest, 'app_two/user.html', context=user_dict)
