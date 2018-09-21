from setuptools import setup, find_packages


setup(
    name='gol_rand',
    version='1.0.1',
    install_requires=[
        'numpy',
        'pillow',
        'imageio'
    ],
    packages=find_packages()
)
