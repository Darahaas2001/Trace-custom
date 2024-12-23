import os
import setuptools

here = os.path.abspath(os.path.dirname(__file__))
version = {}
with open(os.path.join(here, "opto/version.py")) as fp:
    exec(fp.read(), version)
__version__ = version["__version__"]


install_requires = [
    "autogen-agentchat~=0.2",
    "graphviz>=0.20.1",
    "scikit-learn",
    "xgboost",
]

setuptools.setup(
    name="trace-opt",
    version=__version__,
    author="Trace Team",
    author_email="chinganc@microsoft.com",
    url="https://github.com/microsoft/trace",
    license="MIT LICENSE",
    description="An AutoDiff-like tool for training AI systems end-to-end with general feedback",
    long_description=open("README.md", encoding="utf-8").read(),
    packages=setuptools.find_packages(include=["opto*"]),
    install_requires=install_requires,
    python_requires=">=3.9",
)
