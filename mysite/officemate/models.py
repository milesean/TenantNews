from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    post_body = models.TextField(max_length=6000)
    comment_count = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return 'Post: {}'.format(self.post_id)


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    add_date = models.DateTimeField('date added')
    comment_body = models.TextField(max_length=1000)
    reply_count = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)


class Reply(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    add_date = models.DateTimeField('date added')
    reply_body = models.TextField(max_length=1000)

