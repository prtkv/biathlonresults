from setuptools import setup
from biathlonresults import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='biathlonresults',
      version=__version__,
      description='biathlonresults.com API for Python',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/prtkv/biathlonresults',
      author='Ilya Porotikov',
      author_email='ip.tspl@gmail.com',
      license='MIT',
      packages=['biathlonresults'],
      install_requires=['requests'],
      tests_require=['pytest'])
