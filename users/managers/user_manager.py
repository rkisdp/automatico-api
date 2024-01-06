from django.contrib.auth.models import BaseUserManager

from security.email import send_verification_code


class UserManager(BaseUserManager):
    def create_user(self, **kwargs):
        password = kwargs.pop("password")
        user = self.model(**kwargs)
        user.email = self.normalize_email(user.email)
        user.set_password(password)
        user.save(using=self._db)
        self.send_welcome_email(user)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        username_field = f"{self.model.USERNAME_FIELD}__iexact"
        return self.get(**{username_field: username})

    def normalize_email(self, email):
        return email.lower()

    def send_welcome_email(self, user):
        send_verification_code(
            user=user,
            code_type="AAC",
            email_template="welcome",
            email_subject="Bienvenido",
        )
