#!/usr/bin/env python
import setuptools

setuptools.setup(
    name='pygments-style-rub',
    version='0.1',
    description='Ruhr-Uni Bochum Corporate Design colors for Pygments',
    license='BSD',
    author='Jan Holthuis',
    author_email='jan.holthuis@ruhr-uni-bochum.de',
    url='https://github.com/Holzhaus/pygments-style-rub',
    packages=['pygments_style_rub'],
    install_requires=['pygments >= 1.4'],
    entry_points={
        'pygments.styles': [
            'rub = pygments_style_rub:RubStyle',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
