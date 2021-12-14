from django.db import models

class Movie(models.Model):
    title = models.CharField('Название фильма', max_length=100)
    gross = models.IntegerField('Сборы', help_text='По всему миру, в гривнах.')

    def __str__(self):
        return self.title
