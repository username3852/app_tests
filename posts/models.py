from django.db import models


class Post(models.Model):  # it inherits the Model class from the models module or package
    text = models.TextField()

    def __str__(self):
        return self.text
