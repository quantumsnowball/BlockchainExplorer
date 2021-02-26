from setuptools import setup

setup(name='blockscan',
      version='1.0',
      description='blockscan',
      entry_points={
          'console_scripts': [
              'blockscan=blockscan.manager:cli',
          ]
      }
)