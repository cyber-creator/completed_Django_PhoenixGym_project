from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from gym.models import Blog, BlogCategory
from .check_group_decorator import editors_permissions
from .models import ProfileCoach

# import forms
from accounts.forms import FormRegister, FormProfile, FormUser, BlogEditForm


def account_options(request):
    if request.user.is_authenticated:
        return redirect('account_profile', permanent=True)

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            login_account = authenticate(request, username=user.username, password=password)
        else:
            messages.error(request, 'credentials are incorrect \n or user not exist ')
            return redirect('account_options', permanent=True)

        try:
            user.profile_coach.first_name
        except:
            ProfileCoach.objects.create(user=user, first_name=user.username, email=user.email)

        if login_account and user.profile_coach:
            login(request, login_account)
            return redirect('account_profile', permanent=True)
        else:
            messages.error(request, "Some information doesn't match \n or user not exist")

    return render(request, 'account/account_options.html')


def account_register(request):

    if request.user.is_authenticated:
        return redirect('account_profile', permanent=True)

    if request.method == 'POST':
        form = FormRegister(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            first_name = cd['first_name']
            email = cd['email']
            password = cd['password']
            password2 = cd['password_confirm']

            if User.objects.filter(username=cd['first_name']).exists():
                messages.error(request, 'This username name already in use')
                return redirect('account_register')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'This email already in use please log in or change your password')
                return redirect('account_register')

            if password == password2:
                new_account = User.objects.create_user(first_name=first_name, username=first_name,
                                                       email=email, password=password)
                ProfileCoach.objects.create(user=new_account, first_name=first_name, email=email)
                login(request, new_account)
                return redirect('account_profile')
            else:
                messages.error(request, 'Password does\'t match')
                return redirect('account_register')

    return render(request, 'account/account_register.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect('account_options')


@login_required
@editors_permissions()
def account_profile(request):
    context = {}
    author = ProfileCoach.objects.get(user=request.user)
    profile_blog = Blog.objects.filter(user=request.user).order_by('-date_added')[:15]
    context["author"] = author
    context["profile_blog"] = profile_blog
    paginator = Paginator(profile_blog, per_page=1)
    page_number = request.GET.get('page')

    if request.method == 'POST':

        try:
            profile = ProfileCoach.objects.get(user=request.user)
        except ObjectDoesNotExist:
            profile = None
            user = None

        form_profile = FormProfile(instance=request.user.profile_coach, data=request.POST)
        form_user = FormUser(instance=request.user, data=request.POST)

        if form_profile.is_valid() and form_user.is_valid():
            form_profile_obj = form_profile.save(commit=False)
            if 'avatar' in request.FILES:
                form_profile_obj.avatar = request.FILES['avatar']
            form_profile_obj.save()
            form_user.save()
            context["profile_data"] = form_profile
            return redirect('account_profile')
    else:
        form_profile = FormProfile(instance=request.user.profile_coach)
        form_user = FormUser(instance=request.user)
        context["profile_data"] = form_profile

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context['blog_list'] = page_obj
    return render(request, 'account/account_profile.html', context)


def account_inform(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'account/account_informer.html')


class BlogEdit(UpdateView):
    model = Blog
    template_name = "account/edit-post.html"
    context_object_name = "blog_single"
    form_class = BlogEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        edit_form = BlogEditForm(instance=context["blog_single"])
        context['categories'] = BlogCategory.objects.all()
        context['edit_form'] = edit_form
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        author = self.request.user
        blog = self.get_object()

        if author == blog.user:
            if 'poster' in self.request.FILES:
                instance.poster = self.request.FILES['poster']
            elif self.request.POST.getlist('categories'):
                new_categories = self.request.POST.getlist('categories')
                blog.category.set(new_categories)

        instance.save()

        return redirect(self.request.META['HTTP_REFERER'], permanent=True)


class BlogCreate(CreateView):
    model = Blog
    template_name = "account/edit-post.html"
    form_class = BlogEditForm
    # context_object_name = "blog_single"
    success_url = reverse_lazy("profile_blog_create")
    extra_context = {'categories': BlogCategory.objects.all()}

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.slug = slugify(form.instance.title)
        instance.save()

        if 'poster' in self.request.FILES:
            instance.poster = self.request.FILES['poster']
            instance.save()

        if 'categories' in self.request.POST:
            new_categories = self.request.POST.getlist('categories')
            instance.category.set(new_categories)
            instance.save()

        return redirect("profile_blog_create")

    def form_invalid(self, form):
        print(self.request)
        return super(BlogCreate, self).form_invalid(form)


class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy("account_profile")


