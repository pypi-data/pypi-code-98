# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['apis_core',
 'apis_core.apis_entities',
 'apis_core.apis_entities.api_mappings',
 'apis_core.apis_entities.management.commands',
 'apis_core.apis_entities.migrations',
 'apis_core.apis_entities.templatetags',
 'apis_core.apis_labels',
 'apis_core.apis_labels.migrations',
 'apis_core.apis_metainfo',
 'apis_core.apis_metainfo.migrations',
 'apis_core.apis_relations',
 'apis_core.apis_relations.migrations',
 'apis_core.apis_relations.templatetags',
 'apis_core.apis_tei',
 'apis_core.apis_tei.management.commands',
 'apis_core.apis_vis',
 'apis_core.apis_vocabularies',
 'apis_core.apis_vocabularies.management.commands',
 'apis_core.apis_vocabularies.migrations',
 'apis_core.context_processors',
 'apis_core.default_settings',
 'apis_core.helper_functions',
 'browsing',
 'browsing.management.commands',
 'browsing.migrations',
 'browsing.templatetags',
 'infos',
 'infos.migrations',
 'infos.templatetags']

package_data = \
{'': ['*'],
 'apis_core': ['.vscode/*',
               'templates/apis_templates/*',
               'templates/apis_templates/autocomplete/*',
               'templates/apis_templates/registration/*'],
 'apis_core.apis_entities': ['fixtures/*',
                             'static/apis_entities/libraries/*',
                             'templates/apis_entities/*',
                             'templates/apis_entities/detail_views/*'],
 'apis_core.apis_labels': ['templates/apis_labels/*'],
 'apis_core.apis_metainfo': ['templates/apis_metainfo/*'],
 'apis_core.apis_relations': ['templates/apis_relations/*'],
 'apis_core.apis_tei': ['templates/apis_tei/*'],
 'apis_core.apis_vis': ['templates/apis_vis/*'],
 'browsing': ['templates/browsing/*', 'templates/browsing/tags/*'],
 'infos': ['templates/infos/*']}

install_requires = \
['Django>=3.1.8,<3.2.0',
 'PyYAML>=5.3.1,<6.0.0',
 'SPARQLWrapper>=1.8.5,<2.0.0',
 'convertdate>=2.3.0,<3.0.0',
 'dj-database-url>=0.5.0,<0.6.0',
 'django-admin-csvexport>=1.9,<2.0',
 'django-autocomplete-light>=3.8.1,<4.0.0',
 'django-cors-headers>=3.5.0,<4.0.0',
 'django-crispy-forms>=1.10.0,<2.0.0',
 'django-crum>=0.7.9,<0.8.0',
 'django-filter>=2.4.0,<3.0.0',
 'django-gm2m>=1.1.1,<2.0.0',
 'django-guardian>=2.3.0,<3.0.0',
 'django-leaflet>=0.27.1,<0.28.0',
 'django-model-utils>=4.1.1,<5.0.0',
 'django-reversion>=3.0.8,<4.0.0',
 'django-summernote>=0.8.11,<0.9.0',
 'django-tables2>=2.3.3,<3.0.0',
 'djangorestframework-csv>=2.1.0,<3.0.0',
 'djangorestframework-jsonschema>=0.1.1,<0.2.0',
 'djangorestframework-xml>=2.0.0,<3.0.0',
 'djangorestframework>=3.12.2,<4.0.0',
 'drf-spectacular==0.11.1',
 'jmespath>=0.10.0,<0.11.0',
 'jsonschema>=3.2.0,<4.0.0',
 'lxml>=4.6.2,<5.0.0',
 'mysqlclient>=2.0.3,<3.0.0',
 'pandas>=0.25.3,<0.26.0',
 'rdflib>=5.0.0,<6.0.0',
 'regex>=2020.11.13,<2021.0.0',
 'requests>=2.25.0,<3.0.0',
 'sentry-sdk>=0.19.5,<0.20.0',
 'tablib>=3.0.0,<4.0.0',
 'unicodecsv>=0.14.1,<0.15.0']

setup_kwargs = {
    'name': 'apis-core',
    'version': '0.16.35',
    'description': 'Base package for the APIS framework',
    'long_description': None,
    'author': 'Matthias Schlögl',
    'author_email': 'matthias.schloegl@oeaw.ac.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<3.9',
}


setup(**setup_kwargs)
