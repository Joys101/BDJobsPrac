from django.db import models

class book(models.Model):
    title = models.CharField(max_length=120)
    publisher = models.CharField(max_length=120)
    age = models.IntegerField()
    page_count = models.IntegerField()
    publish_date = models.DateField()
    book_type = models.CharField(max_length=120)

    def __str__(self):
        return self.title