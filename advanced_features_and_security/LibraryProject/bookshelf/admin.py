from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book
# from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    # Use custom forms for user creation and editing
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = CustomUser

    # Fields to display in the admin list view
    list_display = ['username', 'email', 'date_of_birth', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'email']

    # Fields to display/edit in the user detail view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields for creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff', 'is_active'),
        }),
    )

# Register the CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)

# Register the Book model
admin.site.register(Book)