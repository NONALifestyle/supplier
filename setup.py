from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in nona_supplier/__init__.py
from nona_supplier import __version__ as version

setup(
	name="nona_supplier",
	version=version,
	description="App for NONA Lifestyle Suppliers",
	author="mustakim",
	author_email="mustakim@nonalifestyle.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
