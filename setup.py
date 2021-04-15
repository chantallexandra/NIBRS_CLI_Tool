from setuptools import setup
setup(
    name='main',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'nibrs_parse=main:run'
        ]
    }
)