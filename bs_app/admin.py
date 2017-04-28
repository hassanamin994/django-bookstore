from django.contrib import admin
from . import models
from django import forms
# Register your models here.

class BookForm(forms.ModelForm):
    def save(self, commit=True):
        print("saving ")
        instance = super(BookForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance
    class Meta:
        model=models.Book
        fields = "__all__"


class BookAdmin(admin.ModelAdmin):

    form = BookForm


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author)
admin.site.register(models.Category)
admin.site.register(models.Profile)
