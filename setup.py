from setuptools import setup

setup(name='resman',
      version='0.1',
      description='Resource manager',
      url='http://github.com/pswart/resman',
      author='Paul Swart',
      author_email='paul.oorkant@gmail.com',
      license='LGPL-3.0',
      packages=['resman'],
      zip_safe=False,
      setup_requires=[
          # dependency for `python setup.py test`
          'pytest-runner',
          # dependencies for `python setup.py build_sphinx`
          'sphinx',
          'recommonmark',
          ])
