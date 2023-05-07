from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    price = models.FloatField(null=False)
    image = models.ImageField(null=True)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=256)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
