from django.db import models


class user(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    # to save the data
    def register(self):
        self.save()

    @staticmethod
    def get_user_by_email(email):
        try:
            return user.objects.get(email=email)
        except user.DoesNotExist:
            return False

    def isExists(self):
        return user.objects.filter(email=self.email).exists()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

