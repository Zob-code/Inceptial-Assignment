try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'Advance User Input',
    'author' : 'My Name',
    'url' : 'URL  to get it at',
    'download_url' : 'Where to download it',
    'author_email' : 'My email',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['Ex48'],
    'scripts' : [],
    'name' : 'projectname'
}

setup(**config)
