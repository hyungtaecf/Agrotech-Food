from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    text = RichTextUploadingField()
    image = models.ImageField()
    publish_date = models.DateField(blank=True, null= True)
    create_date = models.DateField(default = timezone.now)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering= ['-publish_date']
