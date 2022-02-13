from django.db import models

# Create your models here.


class Terms(models.Model):
    Term_name = models.CharField(max_length=100)
    Term_def = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'terms'

    def __str__(self):
        return self.Term_name