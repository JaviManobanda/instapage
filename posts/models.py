from django.db import models


class User(models.Model):
    """ modelos del usuario """
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.CharField(max_length=100, blank=True)

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} : {self.email}'
