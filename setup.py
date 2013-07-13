# coding: utf-8
from distutils.core import setup

setup(name='pcaxis',
      version='0.1',
      description='PC Axis (.px) dataset parser',
      author=u'Gašper Žejn'.encode('utf-8'),
      author_email='zejn@owca.info',
      url='http://www.zejn.net/labs/',
      py_modules=['pcaxis'],
      install_requires=['pyparsing>=1.5.2'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
     )


