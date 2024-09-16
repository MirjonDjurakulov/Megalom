"""
WSGI config for djangoProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

import sys

activate_this = os.path.expanduser('~/site/venv/bin/activate_this.py')

exec(open(activate_this).read(), {'__file__': activate_this})

sys.path.insert(1, os.path.expanduser('~/site/public_html/'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings.production')

application = get_wsgi_application()
