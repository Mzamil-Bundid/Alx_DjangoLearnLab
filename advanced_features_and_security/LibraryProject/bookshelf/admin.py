from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book
# from .forms import CustomUserCreationForm, CustomUserChangeForm

# Custom Admin for CustomUser
class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'email']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff', 'is_active'),
        }),
    )

# Custom Admin for Book
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_year']
    list_filter = ['author']
    search_fields = ['title', 'author']
    # Allow managing permissions in the Book admin
    filter_horizontal = ('permissions',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)