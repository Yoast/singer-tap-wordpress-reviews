"""Setup."""
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='tap-wordpress-reviews',
    version='0.1.0',
    description='Singer.io tap for extracting data form WordPress Reviews',
    author='Yoast',
    url='https://github.com/Yoast/singer-tap-wordpress-reviews',
    classifiers=['Programming Language :: Python :: 3 :: Only'],
    py_modules=['tap_wordpress_reviews'],
    install_requires=[
        'beautifulsoup4~=4.9.3',
        'httpx[http2]~=0.17.1',
        'singer-python~=5.12.0',
    ],
    entry_points="""
        [console_scripts]
        tap-wordpress-reviews=tap_wordpress_reviews:main
    """,
    packages=find_packages(),
    package_data={
        'tap_wordpress_reviews': [
            'schemas/*.json',
        ],
    },
    include_package_data=True,
)
