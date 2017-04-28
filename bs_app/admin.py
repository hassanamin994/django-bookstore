from django.contrib import admin
from . import models
from django import forms
# Register your models here.

class BookForm(forms.ModelForm):
    def save(self, commit=True):
        print("saving ")
        instance = super(BookForm, self).save(commit=False)


        instance.save()
        notification_category_body = "A new book was added in " + instance.category.name
        notification_category = models.Notification.objects.create(body=notification_category_body)
        for profile in instance.category.profile_set.all():
            profile.notifications.add(notification_category)
        # print('the count is ' + str(instance.authors.all().count()))
        # for author in instance.authors.all():
        #     notification_author_body = author.name + " Has published a new book"
        #     notification_author = models.Notification.objects.create(body=notification_author_body)
        #     for profile in author.profile_set.all():
        #         profile.notifications.add(notification_author)
        #         profile.notifications.save()
        # return instance
    class Meta:
        model=models.Book
        fields = "__all__"


class BookAdmin(admin.ModelAdmin):

    form = BookForm


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author)
admin.site.register(models.Category)
admin.site.register(models.Profile)
