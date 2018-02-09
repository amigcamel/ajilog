"""Setup."""
from setuptools import setup, find_packages

external_modules = [
    'colorlog==3.1.0',
]

if __name__ == '__main__':
    setup(
        name='ajilog',
        version='0.0.3',
        packages=find_packages(),
        install_requires=external_modules,
        description='Wrapper for colorlog for better use.',
        author='Aji Liu',
        author_email='amigcamel@gmail.com',
    )
