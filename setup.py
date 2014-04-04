#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    install_requires=['spreads', 'RPi.GPIO'],
    name='spreadsplug_rpipushbuttontrigger',
    provides=['spreadsplug_rpipushbuttontrigger'],
    version='1.0',
    author='Matti Kariluoma',
    author_email='matti@kariluo.ma',
    description='Spreads (http://github.com/DIYBookScanner/spreads http://spreads.readthedocs.org) plugin',
    license='public domain',
    classifiers=['Environment :: Console',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX',
        'Topic :: Multimedia :: Graphics :: Capture',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion'],
    keywords='spreads spreadsplugin',
    packages=['spreadsplug_rpipushbuttontrigger'],
    entry_points={u'spreadsplug.hooks': [u'RPiPushButtonTrigger = spreadsplug_rpipushbuttontrigger.RPiPushButtonTrigger:RPiPushButtonTrigger']},
  )
