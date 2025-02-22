from django.contrib import admin
from .models import Movie, Director, Review
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'stars', 'movie')
    list_filter = ('stars', 'movie')
    search_fields = ('text',)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["id", "username", "email", "is_active", "confirmation_code"]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("confirmation_code",)}),
    )

