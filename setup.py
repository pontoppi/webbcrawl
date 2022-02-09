from setuptools import setup

setup(name='webbcrawl',
      version=1.0,
      description='Retrieve information about JWST data files from folder',
      author='Klaus Pontoppidan (STScI)',
      author_email='pontoppi@stsci.edu',
      url='http://jwst.stsci.edu/',
      download_url = '',
      packages=['webbcrawl'],
      install_requires=['pandas>=1.3.5'],
      entry_points = {'console_scripts': ['webbcrawl=webbcrawl.cli:main']}
      )
