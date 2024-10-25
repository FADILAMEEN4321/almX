"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
# from pathlib import Path

from django.core.asgi import get_asgi_application


# This allows easy placement of apps within the interior
# almx directory.
# BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
# sys.path.append(str(BASE_DIR / "almx"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.django.base')

application = get_asgi_application()
