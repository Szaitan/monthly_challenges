from django.contrib import admin
from challenges.models import Author, Posts, Tag

# Register your models here.

admin.site.register(Author)
admin.site.register(Posts)
admin.site.register(Tag)
