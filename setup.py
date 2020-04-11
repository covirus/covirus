from setuptools import setup, find_packages


setup(
    name="covirus",
    version="0.0.4-2",
    author="Victor Maricato",
    author_email="maricatovictor@gmail.com",
    description="A library for dealing with COVID19 analysis",
    long_description_content_type="text/markdown",
    url="https://github.com/maricatovictor/covirus",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
