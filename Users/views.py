from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import logout
from django.views import View  

def index(request):
    context = {
        'login_url': reverse('login')  
    }
    return render(request, 'index.html', context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login') 
