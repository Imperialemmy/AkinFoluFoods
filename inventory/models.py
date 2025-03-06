from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    pass

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    pass

class Size(models.Model):
    size = models.IntegerField(max_length=10)

    def __str__(self):
        return f'{self.size}kg'
    pass

class Ware(models.Model):
    name = models.CharField(max_length=100, unique=True)
    brand = models.ForeignKey(Brand, related_name='brands', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    size = models.ForeignKey(Size, related_name='sizes', on_delete=models.CASCADE, null=True)
    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update_availability(self):
        if self.stock > 0:
            self.is_available = True
        else:
            self.is_available = False
        self.save()

    def __str__(self):
        return self.name

    pass


class WareWithPromo(models.Model):
    pass




