from setuptools import setup, find_packages

setup(
    name="lab2",
    version=1.0,
    description="Lab2 -- Serialization tool",
    author="Anton Novikov",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        'PyYAML==5.4.1',
        'toml==0.10.0'
    ],
)
