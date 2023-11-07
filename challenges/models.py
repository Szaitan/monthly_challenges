from django.db import models

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    author = models.ForeignKey("Author", on_delete=models.SET_DEFAULT, default="No User")
    date = models.DateField()
    image = models.ImageField(upload_to="post_images/", default="")
    excerpt = models.CharField(max_length=80)
    content = models.CharField(max_length=50)
    tag = models.ManyToManyField("Tag")

    def __str__(self):
        return f"{self.title}"


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    e_mail_address = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.caption}"


