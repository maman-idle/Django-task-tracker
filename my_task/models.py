from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyCustomUserManager(BaseUserManager):
    #create user
    def create_user(self, email, username, password):
        if not email:
            raise ValueError("User must have an email!")
        if not username:
            raise ValueError("User must have a username!")
        if not password:
            raise ValueError("User must have a password!")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            password = password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    #create superuser
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self.db)     
        return user

class MyCustomUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    # Required fields for custom user model
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    #login using email
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'password']

    objects = MyCustomUserManager()

    def __str__(self) -> str:
        return self.email

class Task(models.Model):

    STATUS = (('FINISH','FINISH'), ('UNFINISH','UNFINISH'),)

    name = models.CharField(max_length=255, blank=False)
    status = models.CharField(max_length=255, choices=STATUS)
    description = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey(MyCustomUser, related_name='task', on_delete=models.CASCADE, null=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name