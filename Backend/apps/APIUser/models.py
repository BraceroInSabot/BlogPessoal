from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class AbsUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, name, password=None, **extra_fields): 
        """
        Create and save a User with the given username, email, name, and password.
        
        Args:
            first_name (str): User name
            last_name (str): User last name
            email (str): User e-mail
            password (str): User password. Defaults to None.
            **extra_fields: Additional fields for the user model.
        
        Raises:
            ValueError: If the email is not provided.
        
        Returns:
            User: The created user instance.
        """       
        if not email:
            raise ValueError('O Email é um campo obrigatório')
        
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user    
    
class AbsUser(AbstractUser, PermissionsMixin):
    username = None
    date_joined = None
    
    user_id = models.AutoField(
        primary_key=True, 
        editable=False, 
        unique=True, 
        db_index=True, 
        db_column='PK_user')
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=False,
        db_index=True,
        db_column='first_name_user')
    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=False,
        db_index=True,
        db_column='last_name_user')
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        db_column='email_user')
    password = models.CharField(
        max_length=128, 
        db_column='password_user')
    is_active = models.BooleanField(
        default=True,
        db_column='is_active_user')
    is_superuser = models.BooleanField(
        default=False,
        db_column='is_superuser_user')
    last_login = models.DateTimeField(
        default=None,
        null=True,
        blank=True,
        db_column='last_login_user')
    date_joined_user = models.DateTimeField(
        auto_now=True,
        db_column='date_joined_user')
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'User'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        