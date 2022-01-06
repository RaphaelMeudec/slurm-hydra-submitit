from setuptools import find_packages, setup

setup(
    name='slurm-hydra-submitit',
    packages=find_packages(),
    install_requires=[
        "hydra-core",
        "hydra-submitit-launcher",
    ]
)
