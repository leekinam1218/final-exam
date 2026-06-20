from setuptools import setup, find_packages

setup(
    name="media_library",
    version="1.0.0",
    author="이기남",
    description="Book and Movie Management Package",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "matplotlib"
    ]
)