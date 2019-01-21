from django.db import models


class Idea(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=300)
    text = models.TextField(verbose_name='Описание')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '%i' % self.id


