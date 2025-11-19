from setuptools import setup, find_packages

setup(
    name='dynacir',
    version='0.1',
    packages=find_packages(),
    install_requires=['qiskit>=0.22,<=2'],
    python_requires='>=3.6',
)
