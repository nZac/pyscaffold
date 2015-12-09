"""A simple Python library scaffold reference.

pyscaffold is an opinionated Python library scaffold.  Mostly created for later
reference by the writer.
"""
import ast
import re
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('scaffold/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name="PyScaffold",
    version=version,
    url='https://github.com/nzac/py-scaffold',
    license='MIT',
    author='Nick Zaccardi',
    author_email='nicholas.zaccardi@gmail.com',
    description='A simple reference for setting up a Python library.',
    long_description=__doc__,
    packages=['scaffold'],
    zip_safe=False,
    platforms='any',
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
