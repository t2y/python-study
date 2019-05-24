import re
import sys

from setuptools import find_packages, setup


metadata_py = open('mypackage/main.py').read()
metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", metadata_py))

REQUIRES = []

if sys.version_info < (3, 4):
    REQUIRES.append('enum34')

setup(
    name='mypackage',
    version=metadata['version'],
    description='Sample pakcage to learn Python packaging',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
        'Environment :: Console',
        'Topic :: Utilities',
    ],
    url='https://github.com/t2y/python-study/tree/master/Testing',
    license='Apache License 2.0',
    author='Tetsuya Morimoto',
    author_email='t2y@example.com',
    zip_safe=False,
    platforms=['unix', 'linux', 'osx', 'windows'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIRES,
    tests_require=[
        'tox', 'pytest', 'pytest-pep8', 'pytest-flakes',
    ],
    entry_points = {
        'console_scripts': [
            'mycmd=mypackage.main:main',
            'yourcmd=mypackage.utils:cmd',
        ],
    },
)
