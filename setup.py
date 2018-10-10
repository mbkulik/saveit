from setuptools import setup

setup(
    name='saveit',
    version='1.0',
    description='save article link for later use',
    author='Michael B. Kulik',
    author_email='mkulik@pinkertonacademy.org',
    packages=['saveit'],
    install_requires=['requests', 'beautifulsoup4'],
)
