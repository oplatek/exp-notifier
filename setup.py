# coding=utf-8
from setuptools import find_packages, setup
from pathlib import Path

project_root = Path(__file__).parent
# install_requires = (project_root / 'requirements.txt').read_text().splitlines()

setup(
    name='exp-notifier',
    version='0.0.5',
    python_requires='>=3.6.0',
    description='Notifcation from experiments to you devices (via slack)',
    long_description=(project_root / 'README.md').read_text(),
    long_description_content_type="text/markdown",
    author='Ondrej Platek',
    author_email='ondrej.platek@seznam.cz',
    license='Apache-2.0 License',
    url='https://github.com/oplatek/exp-notifier',
    donwload_url='https://github.com/oplatek/exp-notifier/archive/refs/tags/0.0.3.tar.gz',
    packages=find_packages(),
    scripts=['notifier/bin/ntf'],
    # install_requires=install_requires,  # TODO make working
    install_requires=['slack_bolt', 'click'],
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
