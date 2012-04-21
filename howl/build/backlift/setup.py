import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup

setup(name='backlift',
      version='0.1.4',
      description='Backlift Command Line Interface',
      author='Cole Krumbholz',
      author_email='cole@backlift.com',
      py_modules=['backlift'],
      install_requires=['requests>=0.10.8', 'PyYAML>=3.10'],
      scripts=['backlift']
     )
