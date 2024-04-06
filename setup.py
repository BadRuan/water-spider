from setuptools import setup, find_packages

setup(
    name='water_info',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pymysql',
        'yaml'
    ],
)
