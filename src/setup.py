from setuptools import setup

setup(
    name='yadokari',
    version='0.1.2',
    author='rhoboro',
    author_email='rhoboro@gmail.com',
    maintainer='rhoboro',
    maintainer_email='rhoboro@gmail.com',
    license="MIT",
    py_modules=['yadokari'],
    install_requires=[
        'Click',
        'requests',
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
