import os
from setuptools import setup


def git_version():
    return os.system('git rev-parse HEAD')


setup(
    name="octue_app_wind_resource",
    version=git_version(),
    py_modules=['app'],
    entry_points='''
    [console_scripts]
    octue-app=app:octue_app
    ''',
)
