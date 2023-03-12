from django import template
from gym.models import BlogCategory, Blog
from accounts.models import ProfileCoach as Profile

register = template.Library()


@register.simple_tag()
def get_categories():
    return BlogCategory.objects.all()


@register.simple_tag()
def get_popular():
    return Blog.objects.order_by('-visit_count__hits')[:3]


@register.simple_tag()
def get_profile():
    return Profile.objects.all()


@register.simple_tag()
def get_blogs():
    return Blog.objects.all()

