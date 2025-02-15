from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class Author(models.Model, AbstractUser):
    author = models.OneToOneField(User, on_delete=models.CASCADE)


# def update_rating(self):


polite = 'Po'
sport = 'So'
education = 'Ed'
show = 'Sh'
economy = 'Ec'
culture = 'Cu'
music = 'Mu'
category = [(polite, 'Политика'),
            (sport, 'Спорт'),
            (education, 'Образование'),
            (show, 'Шоу-бизнес'),
            (economy, 'Экономика'),
            (culture, 'Культура'),
            (music, 'Музыка')]


class Category(models.Model):
    name = models.CharField(max_length=2, choices=category, unique=True)


news = 'N'
article = 'A'
type_of_post = [(news, 'Новости'),
                (article, 'Статья')]


class Post(models.Model):
    heading = models.CharField(max_length=255)
    text_post = models.TextField()
    rating_post = models.IntegerField(default=0)
    time_in = models.DateTimeField(auto_now_add=True)
    type_post = models.CharField(choices=type_of_post, max_length=1)
    auth = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', through='PostCategory')

    def like(self, rating_post):
        self.rating_post += 1
        rating_post.save()
        return self.rating_post

    def dislike(self, rating_post):
        self.rating_post -= 1
        rating_post.save()
        return self.rating_post

    def preview(self):
        return self.text_post[0:125] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Comment(models.Model):
    text_comment = models.TextField()
    time_write = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)
    com_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    com_auth = models.ForeignKey('Author', on_delete=models.CASCADE)

    def like(self, rating_comment):
        self.rating_comment += 1
        rating_comment.save()
        return self.rating_comment

    def dislike(self, rating_comment):
        self.rating_comment -= 1
        rating_comment.save()
        return self.rating_comment

# Create your models here.
