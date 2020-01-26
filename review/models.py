from django.db import models


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.CharField(max_length=1000)
 
    def __unicode__(self):
        return self.user_name
