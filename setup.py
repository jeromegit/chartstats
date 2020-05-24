#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Jerome Provensal",
    author_email='jerome@provensal.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="CLI utility to easy parse files, compute stats, and chart results",
    entry_points={
        'console_scripts': [
            'chartstats=chartstats.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='chartstats',
    name='chartstats',
    packages=find_packages(include=['chartstats', 'chartstats.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jeromegit/chartstats',
    version='0.1.0',
    zip_safe=False,
)
