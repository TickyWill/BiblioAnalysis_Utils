#!/usr/bin/env python

from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

#requires = open(file_requirements).read().strip().split('\n')
    
# This setup is suitable for "python setup.py develop".

setup(name='BiblioAnalysis_Utils',
      version='1.2.0',
      description='A toolbox for bibliographic analysis',
      long_description=long_description,
      long_description_content_type='text/markdown',
      include_package_data = True,
      license = 'MIT',
      classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Information Analysis :: Visualization',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research'
        ],
      keywords = 'Bibliography, Corpus parsing, Corpus description, Coupling, Co-occurrence, WOS, SCOPUS',
      install_requires = ['matplotlib==3.4.3',
                          'more-itertools==8.10.0',
                          'networkx==2.6.3',
                          'nltk==3.6.5',
                          'openpyxl==3.0.9',
                          'pandas==1.3.3',
                          'python-louvain==0.15',
                          'pyvis==0.1.9',
                          'squarify==0.4.3',
                          'scipy==1.7.1'],
      author= 'BiblioAnalysis team',
      author_email= 'francois.bertin7@wanadoo.fr, amal.chabli@orange.fr',
      url= 'https://github.com/TickyWill/BiblioAnalysis_Utils',
      packages=find_packages(),
      )
