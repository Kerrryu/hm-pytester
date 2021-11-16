from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='smaj_hm_pyhelper',
    version='0.11.16',
    author="smaj Nebra Ltd",
    author_email="",
    description="Helium Python Helper (FORKED FOR TEST DO NOT USE)",
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SebastianMaj/hm-pytester",
    install_requires=[
        'requests>=2.26.0',
        'jsonrpcclient==3.3.6',
        'retry==0.9.2'
    ],
    project_urls={
        "Bug Tracker": "https://github.com/SebastianMaj/hm-pytester/issues",
    },
    packages=find_packages(),
    include_package_data=True
)
