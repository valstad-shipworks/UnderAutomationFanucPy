from setuptools import setup, find_packages

setup(
    name="underautomation",
    version="1.2.0",
    package_dir={"": "src"},
    packages=find_packages(where="src", include=["underautomation*"]),
    py_modules=["underautomation"]
)
