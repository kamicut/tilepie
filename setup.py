from setuptools import setup
from codecs import open
from os import path

long_description='''
tilepie 
=======

Simple ``.mbtiles`` processor for python. Built with the `QA Tiles <https://osmlab.github.io/osm-qa-tiles/>`_ in mind.
Based on the map/reduce/end structure in `@mapbox/tilereduce <https://github.com/mapbox/tile-reduce>`_.

Acknowledgements & pevious work
--------------------------------
- `mapbox/tilereduce <https://github.com/mapbox/tile-reduce>`_
- `jwass/tile-reduce-py: <https://github.com/jwass/tile-reduce-py/>`_
- `makinacorpus/landez: <https://github.com/makinacorpus/landez/>`_
'''

setup(name='tilepie',
      version='0.2',
      description='multiproc mbtile processing',
      long_description=long_description,
      url='https://github.com/kamicut/tilepie',
      author='Marc Farra',
      author_email='marcfarra@gmail.com',
      license='MIT',
      packages=['tilepie'],
      install_requires = [],
      zip_safe=False)
