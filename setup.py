from setuptools import setup, find_packages


setup(
    name="covirus", # Replace with your own username
    version="0.0.1",
    author="Victor Maricato",
    author_email="maricatovictor@gmail.com",
    description="A library for dealing with COVID19 analysis",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)