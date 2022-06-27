
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations: True
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password=None, **kwargs):
        """
        Create and save a User with the given email and password.
        """
        if(not email):
           raise ValueError("No Email Provided!")

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        # import pdb;pdb.set_trace()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)


        if(kwargs.get('is_staff') is not True):
           raise ValueError("Super User must be a staff in order to be in!")

        if(kwargs.get('is_superuser') is not True):
           raise ValueError("User must be a SuperUser!")

        if(kwargs.get('is_active') is not True):
           raise ValueError("Super User must be active!")
        
        return self.create_user(email, password, **kwargs)