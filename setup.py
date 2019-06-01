from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='biathlonresults',
      version='0.1',
      description='biathlonresults.com API for Python',
      url='http://github.com/prtkv/biathlonresults',
      author='Ilya Porotikov',
      author_email='ip.tspl@gmail.com',
      license='MIT',
      packages=['biathlonresults'],
      install_requires=['requests'],
      tests_require=['pytest']
      zip_safe=False)
