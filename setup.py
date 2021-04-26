#!/usr/bin/env python3
from setuptools import find_packages, setup
from pathlib import Path

project_dir = Path(__file__).parent
install_requires = (project_dir / 'requirements.txt').open().read().splitlines()

setup(
    name='notifier',
    version='0.0.1',
    python_requires='>=3.6.0',
    description='Notifcation from experiments to you devices (via slack)',
    author='Ondrej Platek',
    license='Apache-2.0 License',
    packages=find_packages(),
    scripts=['notifier/bin/ntf'],
    install_requires=install_requires,
)
