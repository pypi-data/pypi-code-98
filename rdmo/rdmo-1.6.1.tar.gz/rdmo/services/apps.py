from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ServicesConfig(AppConfig):
    name = 'rdmo.services'
    verbose_name = _('Services')
