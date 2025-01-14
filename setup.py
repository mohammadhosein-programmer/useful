# from pathlib import Path

import setuptools

VERSION = "0.0.1"  # PEP-440

NAME = "mmd-coder-useful"

INSTALL_REQUIRES = []


setuptools.setup(
    name=NAME,
    version=VERSION,
    description="A python package for supporting everyday works in python.",
    url="https://github.com/mohammadhosein-programmer/useful",
    project_urls={
        "Source Code": "https://github.com/mohammadhosein-programmer/useful",
    },
    author="MMD_Coder",
    author_email="mohammadhamze1387@gmail.com",
    # license="Apache License 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.10",
    ],
    # Snowpark requires Python 3.8
    # python_requires=">=3.8",
    # Requirements
    install_requires=INSTALL_REQUIRES,
    packages=["mmdcoder_useful"],
    # long_description=Path("README.md").read_text(),
    # long_description_content_type="text/markdown",
)