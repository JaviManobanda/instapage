from django.contrib import admin
from users.models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
# Register your models here.
# ? admin.site.register(Profile) //forma rapida de agregar el perfiol creado


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    # ? se coloca el orden que se quiere ver de las columnas
    list_display = ('pk', 'user', 'phone_number',
                    'website', 'pictureUser')
    # ? al dar clic en los items 'pk','user', 'phone_number'. LLevan al detalle del usuario
    list_display_links = ('pk', 'user')
    # ? Para que sean campos editables en el admin
    list_editable = ('phone_number', 'website', 'pictureUser')
    # ? Campo de busqueda donde se determina los campos a buscar,
    #! Para referenciar a los items de usuario colocar __ (doble quion bajo)
    search_fields = ('user__email', 'user__first_name',
                     'user__last_name')
    # ? Crea filtros para la búsqueda
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')

    # ? Se coloca los campos en secciones
    fieldsets = (
        ('Profile', {
            "fields": (('user', 'pictureUser'), ),
        }),
        ('Extra Info', {
            "fields": (('website', 'phone_number'), 'biography')
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),)
        })
    )

    # ! Para que sean campos de solo lectura
    readonly_fields = ('created', 'modified')


class ProfileInline(admin.StackedInline):
    #! Crear una clase con el perfil que se quiere agregar
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    #! Crea una clase UserAdmin que contendra al perfil que hemos creado
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_active', 'is_staff')


# * Se vuelve a registrar el UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
