#!/usr/bin/env python
import os
from setuptools import setup

with open(os.path.join('fio_stats', '__init__.py')) as f:
    for line in f:
        if line.strip().startswith('__version__'):
            version = line.split('=')[1].strip().replace('"', '').replace("'", '')

setup(
    name='fio-stats',
    author='Matthew Perry',
    author_email='perrygeo@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: GIS'
    ],
    description="A Fiona CLI plugin for summary statistics on GeoJSON properties",
    entry_points="""
    [fiona.fio_plugins]
    stats=fio_stats.cli:stats
    """,
    extras_require={
        'dev': ['pytest', 'pytest-cov']
    },
    include_package_data=True,
    install_requires=[
        'tabulate',
        'fiona>=1.6'
    ],
    keywords='Fiona fio GIS plugin',
    license="New BSD",
    packages=['fio_stats'],
    url='https://github.com/perrygeo/fio-stats',
    version=version,
    zip_safe=False
)
