from distutils.core import setup
import setuptools


setup(
    name='gol_rand',
    version='',
    install_requires=[
        'numpy',
        'pillow',
        'imageio'
    ],
    packages=[
        'gol_rand'
    ],
    entry_points={
        "console_scripts": [
        ]
    }
)
