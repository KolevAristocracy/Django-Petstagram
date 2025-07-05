from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from petstagram.accounts.forms import AppUserCreationForm, AppUserChangeForm
from petstagram.accounts.models import Profile

UserModel = get_user_model()

# Register your models here.
@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    list_display = ("email", "is_active", "is_staff")
    form = AppUserChangeForm
    add_form = AppUserCreationForm
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "usable_password", "password1", "password2"),
            },
        ),
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...