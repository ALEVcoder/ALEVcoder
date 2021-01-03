from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['Ism']
        message = request.POST['Xabar']
        email = request.POST['Pochta']
        title = email
        msg = 'Sizga '+name+'dan yangi xabar keldi'+'\nEmail: '+email+'\nXabari: '+message

        print(name, message, email)
        
        send_mail(
            name,
            msg,
            email,
            ['alevcoder1@gmail.com', 'kompbook22@gmail.com'],
            fail_silently=False,
        )

        print('Xabar ketti')
    return render(request, 'index.html')