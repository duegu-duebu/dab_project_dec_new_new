from setuptools import setup, find_packages

setup(
    name="dab_project_dec",
    version="0.0.2",
    description="This contains the code in the ./src directory",
    author="Saurabh Pal",
    packages=find_packages(where="./src"),
    package_dir={"":"./src"},
    install_requires=["setuptools"]
)