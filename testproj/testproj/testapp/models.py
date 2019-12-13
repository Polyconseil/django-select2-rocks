from django.db import models


class Beach(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class SelectedBeach(models.Model):
    json_beach = models.ForeignKey(
        Beach,
        blank=True,
        null=True,
        related_name='json',
        on_delete=models.CASCADE,
    )
    rest_framework_beach = models.ForeignKey(
        Beach,
        blank=True,
        null=True,
        related_name='rest',
        on_delete=models.CASCADE,
    )
