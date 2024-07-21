from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from django.views import View

from Users.models import user


class Login(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        users = user.get_user_by_email(email)
        error_message = None

        if users:
            if check_password(password, users.password):
                request.session['user_id'] = users.id
                return redirect('index')
            else:
                error_message = 'Invalid email or password!'
        else:
            error_message = 'Invalid email or password!'

        return render(request, self.template_name, {'error': error_message})
    

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        users = user(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(users)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            users.password = make_password(users.password)
            users.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, users):
        error_message = None
        if not users.first_name:
            error_message = "Please enter your First Name!"
        elif len(users.first_name) < 3:
            error_message = 'First Name must be 3 characters or more'
        elif not users.last_name:
            error_message = 'Please enter your Last Name'
        elif len(users.last_name) < 3:
            error_message = 'Last Name must be 3 characters or more'
        elif not users.phone:
            error_message = 'Enter your Phone Number'
        elif len(users.phone) < 10:
            error_message = 'Phone Number must be 10 characters long'
        elif len(users.password) < 5:
            error_message = 'Password must be 5 characters long'
        elif len(users.email) < 5:
            error_message = 'Email must be 5 characters long'
        elif users.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message






