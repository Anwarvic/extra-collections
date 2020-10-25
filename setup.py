import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="extra-collections",
    version="1.0.1",
    author="Anwarvic",
    author_email="mohamedanwarvic@gmail.com",
    description=(
        "extra-collections (or extra for short) is a python3 pacakge that "
        + "provides a pythonic, intuitive, and easy implementation of the "
        + "most common data structures used in software projects."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Anwarvic/extra-collections",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
)
