from setuptools import setup

setup(
    name='yadokari',
    version='0.1',
    py_modules=['yadokari'],
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        yadokari=yadokari:cmd
    ''',
)
