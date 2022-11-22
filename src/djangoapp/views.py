from django.http import request
from django.shortcuts import render , redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm , ContactForm
from django.contrib.auth import logout as auth_logout


# Create your views here.

def dashboard(request):
    context = {
        "welcome": "Welcome to your dashboard"
    }
    return render(request, 'djangoapp/dashboard.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'djangoapp/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'djangoapp/register.html', context=context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'djangoapp/edit.html', context=context)

@login_required
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("djangoapp:contact_sent")
      
	form = ContactForm()
	return render(request, "djangoapp/contact.html", {'form':form})
    
@login_required
def contact_sent(request):
    context = {
        "Contact": "Contact Sent"
    }
    return render(request, 'djangoapp/contact_sent.html', context=context)



    