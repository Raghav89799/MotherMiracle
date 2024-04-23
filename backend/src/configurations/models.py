from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from rest_framework_simplejwt.tokens import RefreshToken

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=255,null=True,blank=True)
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    mobile_number = models.IntegerField(null=True,blank=True)
    otp_verify = models.IntegerField(null=True,blank=True)
    user_type = models.CharField(max_length=255,choices=(
        ("Student","Student"),
        ("Teacher","Teacher"),
        ("Staff","Staff"),
        ("Principal","Principal"),
        ("Vice Principal","Vice Principal")
    ),null=True,blank=True)
    
    date_of_birth = models.DateField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password",]

    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Student(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True,blank=True)
    grade = models.IntegerField(null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    roll_no = models.IntegerField(null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    adhar_number = models.IntegerField(null=True,blank=True)
    adhar_image = models.ImageField(null=True,blank=True,upload_to='images')

    def __str__(self):
        return self.name
