from django.contrib import admin

from .models import Post


# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = [ "title",  "timestamp", "updated" ,"content"]
    list_filter = ["updated", "timestamp"]
    list_display_links = ["timestamp"]
    list_editable = ["title"]
    search_fields = ["title", "content"]

    class Meta:
        Model = Post



admin.site.register(Post, PostModelAdmin)
