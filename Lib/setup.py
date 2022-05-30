from setuptools import find_packages, setup
setup(
    name='Omegalib',
    packages=find_packages(include=['Omegalib']),
    version='0.0.9-2',
    scripts=['bin/omega.bat'],
    install_requires=['wheel','setuptools','twine'],
    description='Python library to create android apps',
    author='Prasad joshi, Saurabh Wani, Aniket Brahmankar, Shyam Sulbhewar',
    license='GCOEJ',
)