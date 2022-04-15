from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)




class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.SET, null=True)

    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        return self.full_name()




class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.SET, null=True)#related_name="books" changes Author object books query from book_set to books
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='', blank=True,
    # editable= False,   needs to be removed for prepopulated fields to work
    null=False, db_index=True) # slug indentifier in search bar add db_index to make searching better
    #arg configurations here also apply to the admin page
    published_countries = models.ManyToManyField(Country)

    def __str__(self):
        return f"{self.title} {self.rating}"

    # override for alternate href path
    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])


# override save to add slug identifier automatically
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
#no longer need this overridden function to add slug thanks to admin page
    