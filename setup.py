from setuptools import setup, find_packages

setup(
    name='water_info',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pymysql',
        'yaml'
    ],
)
