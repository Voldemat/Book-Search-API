from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.



class FavouriteBook(models.Model):
      title = models.CharField(verbose_name = "name", max_length = 200, unique=True)
      
      user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "books")
      
      image = models.CharField(max_length=200, null = True)
      
      author_name = models.CharField(max_length=200, null = True, blank = True)
      
      key = models.CharField(max_length=100, null = True, unique=True)
      
      def __str__(self):
            return self.title
      
      def get_absolute_url(self):
            return reverse("books:detail", kwargs = {"id":self.key})

      def get_delete_url(self):
            return reverse("books:favourite-delete", kwargs={"id":self.key})