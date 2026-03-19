import os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
django.setup()
from rsvp.models import Guest
obj, created = Guest.objects.get_or_create(name='Ms Farah', slug='ms-farah')
print(f"Guest: {obj.name} (slug={obj.slug}) - {'created' if created else 'exists'}")
