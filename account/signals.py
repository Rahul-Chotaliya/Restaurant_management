from django.db.models.signals import Signal
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Menu,Like ,LikeR

# Define the signal
post_created = Signal()


# @receiver(post_save, sender=Menu)
# def send_post_created_signal(sender, instance, created, **kwargs):
#     if created:
#         post_created.send(sender=sender, instance=instance)
      
@receiver(post_save, sender=LikeR)
def update_post_likes(sender, instance, created, **kwargs):
    if created:
        print(instance.resturant.likes,'kookokokookokokooooookokookoooovhgjcfccchgffcgjg')
        resturant = instance.resturant
        resturant.likes = resturant.resturant.count()
        resturant.save()

@receiver(post_save, sender=Like)
def update_post_likes(sender, instance, created, **kwargs):
    if created:
        print(instance,'kookkokoooookokokokoko')
        menu = instance.menu
        menu.likes = menu.like_set.count()
        menu.save()
  