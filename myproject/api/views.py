from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

@api_view(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')  

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login/')  # After signup, redirect to login

    @api_view(['GET'])
    def login_view(request):
       return Response({"message": "This is the login page."})

    # if GET request
    return render(request, 'api/signup.html')
