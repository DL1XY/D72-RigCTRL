try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='D72-RigCTRL',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=[
        'tests',
        'app',
        'tests.unit',
        'tests.unit.d72',
        'tests.unit.d72.cmds',
        'app.view',
        'app.d72',
        'app.d72.cmds',
    ],
)
