from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser


#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, name, tc, password=None, password2=None):
      """
      Creates and saves a User with the given email, name, tc and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          name=name,
          tc=tc,
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, name, tc, password=None):
      """
      Creates and saves a superuser with the given email, name, tc and password.
      """
      user = self.create_user(
          email,
          password=password,
          name=name,
          tc=tc,
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

#  Custom User Model
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    save_menu = models.CharField(max_length=255,blank=True,null=True,unique=True)
    
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin




class Menu(models.Model):
    menu_name = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    price = models.CharField(max_length=255)
    # save_menu= models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True)
    def __str__(self) -> str:
        return self.menu_name

class Like(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Like for '{self.menu.menu_name} '"    


class Resturants(models.Model):
    resturant_name= models.CharField(max_length=200 )
    likes= models.IntegerField(default=0)
    is_admin=models.BooleanField(default=False)
    menus = models.ManyToManyField(Menu)
    def __str__(self) -> str:
        return self.resturant_name

    
class LikeR(models.Model):
    resturant = models.ForeignKey(Resturants,on_delete=models.CASCADE,related_name='resturant')
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Like for '{self.resturant.resturant_name}'"

class SaveMenu(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    resturant_name = models.ManyToManyField(Resturants)
    menu_name = models.ManyToManyField(Menu)
    
    def __str__(self) -> str:
        return f'{self.user_id.name},   {self.resturant_name},   {self.menu_name}'