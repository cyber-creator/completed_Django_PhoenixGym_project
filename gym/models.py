from datetime import date

from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount

# Create your models here.
from django.urls import reverse


class BlogCategory(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_by_author',
                             blank=True, null=True)
    title = models.CharField("Blog title", max_length=50, unique=True)
    date_added = models.DateField("Blog Added", default=date.today)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.ManyToManyField(BlogCategory, blank=True)
    blog_text = models.TextField("Blog Text")
    special_text = models.TextField("Special Text", max_length=250)
    blog_text_next = models.TextField("Blog Text next", blank=True, null=True)
    poster = models.ImageField("Poster", upload_to="poster/", null=True, default='img/blog/news/news_1.jpg')
    youtube_link = models.URLField(blank=True, null=True)
    visit_count = GenericRelation(HitCount, object_id_field='object_pk')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_blog', args=[self.slug])

    def get_absolute_profile_url(self):
        return reverse('profile_blog_edit', args=[self.slug])


class Contact(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    subscription = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.phone}'
