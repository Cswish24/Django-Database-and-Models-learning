from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='', blank=True,
    # editable= False,   needs to be removed for prepopulated fields to work
    null=False, db_index=True) # slug indentifier in search bar add db_index to make searching better
    #arg configurations here also apply to the admin page
    

    def __str__(self):
        return f"{self.title} ({self.rating})"

    # override for alternate href path
    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])


# override save to add slug identifier automatically
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
#no longer need this overridden function to add slug thanks to admin page
    