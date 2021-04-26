#!/usr/bin/env python3
from setuptools import find_packages, setup
from pathlib import Path

project_dir = Path(__file__).parent
install_requires = (project_dir / 'requirements.txt').open().read().splitlines()

setup(
    name='exp-notifier',
    version='0.0.1',
    python_requires='>=3.6.0',
    description='Notifcation from experiments to you devices (via slack)',
    author='Ondrej Platek',
    author_email='ondrej.platek@seznam.cz',
    license='Apache-2.0 License',
    url='https://github.com/oplatek/exp-notifier',
    donwload_url='https://github.com/oplatek/exp-notifier/archive/refs/tags/0.0.1.tar.gz',
    packages=find_packages(),
    scripts=['notifier/bin/ntf'],
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: System :: Logging',
        'Topic :: System :: Networking :: Monitoring',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
