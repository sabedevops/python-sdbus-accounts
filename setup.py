from __future__ import annotations
from setuptools import setup


with open('./README.md') as f:
    long_description = f.read()

setup(
    name='sdbus-accounts',
    description=('python-sdbus binds for freedesktop.org AccountsService'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.0',
    url='https://github.com/sabedevops/python-sdbus-accounts',
    author='sabedevops',
    author_email='sabedevops@gmail.com',
    license='LGPL-2.1-or-later',
    keywords='accounts dbus linux freedesktop',
    project_urls={
        'Documentation': 'https://github.com/sabedevops/python-sdbus-accounts/blob/master/README.md',
        'Source': 'https://github.com/sabedevops/python-sdbus-accounts/',
        'Tracker': 'https://github.com/sabedevops/python-sdbus-accounts/issues/',
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        (
            'License :: OSI Approved :: '
            'GNU Lesser General Public License v2 or later (LGPLv2+)'
        ),
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=[
        'sdbus_async.accounts'
    ],
    package_data={
        'sdbus_async.accounts': [
            'py.typed',
        ]
    },
    python_requires='>=3.7',
    install_requires=[
        'sdbus>=0.8rc2',
    ],
)
