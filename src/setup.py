from setuptools import setup

setup(
    name='yadokari',
    version='0.1.3',
    author='rhoboro',
    author_email='rhoboro@gmail.com',
    maintainer='rhoboro',
    maintainer_email='rhoboro@gmail.com',
    license="MIT",
    py_modules=['yadokari'],
    description='yadokari.py is a command line tool for yadokari reservation system.',
    install_requires=[
        'Click<7.0',
        'requests<3.0',
    ],
    entry_points='''
        [console_scripts]
        yadokari=yadokari:cmd
    ''',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
)
