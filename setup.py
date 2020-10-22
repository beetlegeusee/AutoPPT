import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="AutoPPT", 
    version="0.0.1",
    author="Beetleguese",
    description='''
        Make your PPTs
    ''',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
    install_requires=[
        "beautifulsoup4",
        "requests",
        "python-pptx"
    ],
)