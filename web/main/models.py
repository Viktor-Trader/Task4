from django.db import models


class Users(models.Model):
    index = models.CharField('Index', max_length=100)
    name = models.CharField('Name', max_length=50)
    mail = models.TextField('E-mail')
    registration_date = models.CharField('Reg. date', max_length=50)
    status = models.TextField('Status')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'