from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to = 'images/')
    pub_date = models.DateTimeField()
    body = models.TextField()
    title = models.CharField(max_length = 255)

    def __str__(self):              #shows title of blog in database instead of blog object
        return self.title

    def summary(self):              #doesn't show whole blog, first 100 characters
        return self.body[:100]

    def pub_date_pretty(self):      #makes date pretty, look up strftime references
        return self.pub_date.strftime( '%b %e %Y' )
