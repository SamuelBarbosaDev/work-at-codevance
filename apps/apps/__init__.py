__version__ = "0.1.0"
__version_info__ = tuple(
    int(num) if num.isdigit() else num
    for num in __version__.replace("-", ".", 1).split(".")
)

# django_celery/__init__.py

from apps.celery import app as celery_app


__all__ = ("celery_app",)