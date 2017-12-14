from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(name='tilepie',
      version='0.1.3',
      description='multiproc mbtile processing',
      long_description=long_description,
      url='https://github.com/kamicut/tilepie',
      author='Marc Farra',
      author_email='marcfarra@gmail.com',
      license='MIT',
      download_url='https://github.com/kamicut/tilepie/archive/0.1.3.tar.gz',
      packages=['tilepie'],
      install_requires = [
        'landez'
      ],
      zip_safe=False)
