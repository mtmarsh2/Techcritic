from django.db import models
PROF_STATUS = 1
AVG_STATUS = 2
    
STATUS_CHOICES = (
    (PROF_STATUS, 'Prof'),
    (AVG_STATUS, 'Avg'),
)

class Scrapped_Comment(models.Model):
    PROF_STATUS = 1
    AVG_STATUS = 2
    
    STATUS_CHOICES = (
        (PROF_STATUS, 'Prof'),
        (AVG_STATUS, 'Avg'),
    )
    source_url = models.URLField()
    source_name = models.CharField()
    text = models.CharField()
    #date = date_of_post
    author_type = models.IntegerField(choices=STATUS_CHOICES)

class Comment(models.Model):
    source_url = models.URLField()
    source_name = models.CharField()
    text = models.CharField()
    product = models.ForeignKey(Product)
    #date = date_of_post
    author_type = models.IntegerField(choices=STATUS_CHOICES)

    def __unicode__(self):
        return str(self.source_url)

class Product(models.model):
    product_name = models.CharField()
