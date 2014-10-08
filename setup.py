"""Setup.py setups the package for use"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'twutils, a module to help speed up development of tools '
                   'written in python for tribalwars, the browser game. ',
    'author': 'John Penland',
    'url': '',
    'download_url': '',
    'author_email': 'johnp90380@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'requests-2.3.0', 'xmlutils', 'xmltodict'],
    'packages': ['twutils'],
    'scripts': [],
    'v_name': 'twutils',
    'license': ''
}