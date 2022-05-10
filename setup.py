from setuptools import setup

setup(
    name='joycon-controller',
    version='1.0',
    description='Uae Joycon to control your computer',
    install_requires=['readchar', 'pynput', 'hidapi', 'pyglm', 'joycon-python']
)
