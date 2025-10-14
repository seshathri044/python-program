# # dbapp1/models.py
# from django.db import models

# class UserData(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)

#     class Meta:
#         app_label = 'dbapp1'  # Explicitly declare the app label

#     def __str__(self):
#         return self.name
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username