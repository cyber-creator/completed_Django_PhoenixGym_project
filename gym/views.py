from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView, ListView, FormView
from hitcount.views import HitCountDetailView

from .forms import ContactForm, SubscribeForm
from .models import *
from accounts.models import ProfileCoach as Profile


class SubscriptionFormMixin:

    def post(self, request, **kwargs):
        form = SubscribeForm(request.POST)
        if form.is_valid():
            clean_d = form.cleaned_data
            if Contact.objects.filter(email=clean_d['email']).exists():
                messages.error(request, 'This email already subscribed')
                return redirect(request.META['HTTP_REFERER'], permanent=True)

            form.save()
            return redirect(request.META['HTTP_REFERER'], permanent=True)


class PhoenixHomePage(TemplateView):  # need all_blogs
    template_name = "index.html"

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'], permanent=True)


class BlogByCategory(SubscriptionFormMixin, ListView):   # need all_blogs
    model = Blog
    template_name = "blog_list.html"
    context_object_name = "blog_list"
    paginate_by = 1
    ordering = ["-date_added"]

    def get_queryset(self):
        return Blog.objects.filter(category__slug=self.kwargs['slug']).order_by('-date_added')


class BlogList(SubscriptionFormMixin, ListView):   # need all_blogs
    model = Blog
    template_name = "blog_list.html"
    context_object_name = "blog_list"
    ordering = ["-date_added"]

    paginate_by = 1


class AuthorsBlog(SubscriptionFormMixin, ListView):   # need all_blogs
    model = Blog
    template_name = "blog_list.html"
    context_object_name = "blog_list"
    ordering = ["-date_added"]

    def get_queryset(self, **kwargs):
        q_set = super().get_queryset()
        author = Profile.objects.get(first_name=self.kwargs['name'])
        return q_set.filter(user=author.user).order_by('-date_added')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Profile.objects.get(first_name=self.kwargs['name'])
        context['author'] = author
        return context

    paginate_by = 1


class SingleBlog(SubscriptionFormMixin, HitCountDetailView, DetailView):
    model = Blog
    template_name = "blog-single.html"
    context_object_name = "blog_single"
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogs_you_may_like = Blog.objects.exclude(id=kwargs['object'].id).filter(category__in=kwargs['object'].
                                                                                 category.all()).distinct()[0:2]
        context['may_like'] = blogs_you_may_like
        return context


class BlogSearch(SubscriptionFormMixin, ListView):
    template_name = "blog_list.html"
    context_object_name = "blog_list"
    paginate_by = 1

    def get_queryset(self):
        return Blog.objects.filter(title__icontains=self.request.GET.get("search_query")).order_by('-date_added')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["search_query"] = f'search_query={self.request.GET.get("search_query")}&'
        return context
