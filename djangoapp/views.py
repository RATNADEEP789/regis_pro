from django.shortcuts import render, redirect
from .models import registab  # Adjust this import based on your actual models module
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        dateofbirth = request.POST['dateofbirth']
        gender = request.POST['gender']
        mobile_number = request.POST['mobile_number']
        email_id = request.POST['email_id']
        home_town = request.POST['home_town'] 
        username = request.POST['Username']
        password = request.POST['password']
        
        # if registab.objects.filter(email_id=email_id).exists():
        #     messages.error(request, "Email already registered.")
        #     return redirect('register')
        # if registab.objects.filter(Username=username).exists():
        #     messages.error(request, "Username already taken.")
        #     return redirect('register')
        
        user = registab(
            full_name=full_name,
            dateofbirth=dateofbirth,
            gender=gender,
            mobile_number=mobile_number,
            email_id=email_id,
            home_town=home_town,
            Username=username,
            password=password
        )
        user.save()
        
        messages.success(request, "Registration successful!")
        return redirect('register')  # Redirect back to the registration page

    return render(request, 'home.html')
