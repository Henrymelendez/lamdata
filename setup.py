import setuptools
from distutils.core import setup 
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata_henrymelendez", # Replace with your own username
    version="0.1.1",
    author="Henrymelendez",
    author_email="author@example.com",
    description="A small example package that splits dates into month year day, and a function that checks for null values ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Henrymelendez/lamdata",
    packages=setuptools.find_packages(include=['pandas', 'numpy']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
