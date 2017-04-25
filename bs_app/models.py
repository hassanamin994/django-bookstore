from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name

class Author(models.Model):

    name = models.CharField(max_length=100,null=False)
    bio = models.TextField()
    def __str__(self):
        return self.name

class Book(models.Model):

    title = models.CharField(max_length=100,null=False)
    description = models.TextField(null=False)
    authors = models.ManyToManyField('Author')
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE )
    authors = models.ManyToManyField('Author')
    categories = models.ManyToManyField('Category')
    books = models.ManyToManyField('Book',through='Rate')

    def __str__(self):
        return self.user.email

#Synchronizing User model with Profile model
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Rate(models.Model):

    profile = models.ForeignKey(Profile,on_delete=models.CASCADE )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    STATES = [('read','Read'),('wish','Wish'),('none','None')]
    state = models.CharField(max_length=10,choices=STATES)
    RATES = [(1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"),(6,"6"),(7,"7"),(8,"8"),(9,"9"),(10,"10")]
    rate = models.CharField(max_length=2,choices=RATES)

    def __str__(self):
        return self.rate
