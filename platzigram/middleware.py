from django.shortcuts import redirect
from django.urls import reverse  # ? Permite obtener url apartir del nombre
from users.models import Profile


class ProfileCompletionMiddleware:
    """ Ensure that the new user create profile
    to use the application
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            # ? en el caso de que no tenga el usuario un perfil se crea uno
            try:
                profile = request.user.profile
            except:
                profile = Profile.objects.create(user=request.user)
                profile.save()
            if not request.user.is_staff:
                if not profile.pictureUser or not profile.biography:
                    # ? verifica que el path sea diferente a update_profile y logout
                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                        return redirect('update_profile')

        response = self.get_response(request)
        return response
