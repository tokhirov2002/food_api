from django.db import models


class Comments(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    full_name = models.CharField(max_length=255)
    images = models.ImageField(upload_to='comment_images/')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Foods(models.Model):
    name = models.CharField(max_length=255)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    images = models.ImageField(upload_to='foods_images/')
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class BookTable(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    phone = models.IntegerField()
    person = models.IntegerField()

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name