from core.models import PublishedModel
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(PublishedModel):
    desciption = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Location(PublishedModel):
    def __str__(self):
        return self.title


class Post(PublishedModel):
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
