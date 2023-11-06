from django.db import models

# class Movies(models.Model):
#     title=models.CharField(max_length=200)
#     year=models.IntegerField(max_length=4)
#     time=models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return(f"{self.title} {self.year} {self.time}")
    

class Url(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=20, unique=True)