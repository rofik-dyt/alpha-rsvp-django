from django.db import models


class Guest(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    RSVP_CHOICES = [
        ('pending', 'Pending'),
        ('attending', 'Attending'),
        ('declined', 'Declined'),
    ]
    rsvp_status = models.CharField(
        max_length=20, choices=RSVP_CHOICES, default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
