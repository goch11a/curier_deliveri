from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserMeneger(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('the imail must be write')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def crete_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_super", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("superuser must have staff status")
        if extra_fields.get("is_super") is not True:
            raise ValueError("superuser must have is_superuser status")
        return self.create_user(email, password, **extra_fields)

class CustomeUser(AbstractBaseUser):
    ROLE_CHOICE = (
        ("customer","Customer"),
        ("curier","Curier"),
        ("admin","admin"),
    )
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_super = models.BooleanField(default=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICE, default="admin")

    objects = CustomUserMeneger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role']

    def __str__(self):
        return self.email

class Parcel(models.Model):
    STATUS_CHOICE = (
        ("pending","Pending"),
        ("in_trabsit","In_trabsit"),
        ("deliveried","Deliveried"),
    )    


    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICE, default="pending")
    sender = models.ForeignKey(CustomeUser, on_delete=models.CASCADE, related_name="user")
    receiver = models.CharField(max_length=50)    
    receiver_adress = models.TextField()
    curier = models.ForeignKey(CustomeUser, related_name="curier", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateTimeField()


class DelveryProof(models.Model):
    parcel = models.OneToOneField(Parcel, related_name="parcel", on_delete=models.CASCADE)
    image = models.URLField(max_length=200)


