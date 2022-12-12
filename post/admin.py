from django.contrib import admin

from post.models import Post, Image, HashTag
# Register your models here.
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(HashTag)