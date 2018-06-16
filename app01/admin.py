from django.contrib import admin

# Register your models here.

class AuthorDetailAdmin(admin.ModelAdmin):
    list_display = ('hobby','addr')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','detail')
    filter_horizontal = ('book',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'kucun', 'sold')
    list_editable = ('title', 'price', 'kucun', 'sold')
    list_per_page = 3
    search_fields = ('id', 'title', 'publisher__name')

class PublisherListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'addr')

from app01 import models
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Publisher_list, PublisherListAdmin)
admin.site.register(models.Person)
admin.site.register(models.AuthorDetail, AuthorDetailAdmin)

