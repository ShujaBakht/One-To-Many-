from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = [ 'post_title', 'post_catrgry', 'post_publish_date', 'user']