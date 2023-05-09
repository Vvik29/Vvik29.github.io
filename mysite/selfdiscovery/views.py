from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCreatForm, UpdateProfileForm, FeedbackForm, UserInfoForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Feedback, Post, Message
from django.contrib.auth.decorators import user_passes_test
from django.views import View
from django.db.models import Q



def main(request):
    return render(request, 'selfdiscovery/main.html')

def contacts(request):

    form = FeedbackForm(request.POST)
    context = {'form': form, }
    return render(request, 'selfdiscovery/contacts.html', context)

@login_required
def cabinet(request):

    user = request.user
    if request.method == 'POST':
        info = UserInfoForm(request.POST, instance=user)
        if info.is_valid():
            return redirect('cabinet')
    else:
        info = UserInfoForm(instance=user)


    if request.method == 'POST':
        passw = PasswordChangeForm(request.user, request.POST)
        if passw.is_valid():
            user = passw.save()
            update_session_auth_hash(request, user)
            return redirect('cabinet')
    else:
        passw = PasswordChangeForm(request.user)



    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('cabinet')
    else:
        form = UpdateProfileForm(instance=request.user)



    context = {'form': form, 'passw': passw, 'info': info, }
    return render(request, 'selfdiscovery/cabinet.html', context)


def contact_success(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('cabinet')
    else:
        form = FeedbackForm()
    # return render(request, 'selfdiscovery/feedback.html', {'form': form})
    return render(request, 'selfdiscovery/contact_success.html')



def registration_view(request):
    if request.method == 'POST':
        form = UserCreatForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = UserCreatForm()
    return render(request, 'selfdiscovery/registration.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        #form = CustomAuthenticationForm(data=request.POST)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        #form = CustomAuthenticationForm()
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})




def user_logout(request):
    logout(request)
    return redirect('main')


def view_feedback(request):
    feedbacks = Feedback.objects.all()
    #feedbacks = Feedback.objects.filter(user=request.user)
    return render(request, 'selfdiscovery/view_feedback.html', {'feedbacks': feedbacks})


@login_required
def view_feedback_my(request):
    feedbacks = Feedback.objects.filter(user=request.user)
    return render(request, 'selfdiscovery/view_feedback_my.html', {'feedbacks': feedbacks})


def admin_only(function):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url='/admin/login/',
        redirect_field_name=None
    )
    return actual_decorator(function)


# @admin_only
def post_list(request):
    if Post.objects.exists():
        posts = Post.objects.order_by('-created_at')
        return render(request, 'selfdiscovery/post_list.html', {'posts': posts})
    else:
        message = "no posts!"
        return render(request, 'selfdiscovery/post_list.html', {'message': message})



def post(request, id=None):
    posts = get_object_or_404 (Post, pk=id)
    context = {"post": posts}
    return render(request, 'selfdiscovery/post_one.html', context)




class AdminContactView(View):
    template_name = "selfdiscovery/contact_success.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        admin_message = Message(name=name, phone=phone, email=email, subject=subject, message=message)
        admin_message.save()
        return render(request, self.template_name, {'success': True})



def search(request):
    query = request.POST.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) | Q (title__icontains=query))
    context = {"post": posts}

    return render(request, 'selfdiscovery/post_list.html', context)

