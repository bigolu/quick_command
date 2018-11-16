from setuptools import setup

setup(name='quick_command',
      version='0.1',
      description='cli for remembering commands',
      url='https://github.com/bigolu/quick_command',
      author='Olaolu Biggie Emmanuel',
      author_email='hi@bigo.lu',
      license='MIT',
      packages=['quick_command'],
      install_requires=[
          'click==7.0',
          'colorama==0.4.0',
          'fuzzywuzzy==0.17.0',
          'pick==0.6.4',
          'pickledb==0.8.1',
          'python-Levenshtein==0.12.0',
      ],
      extras_require={
          'dev': [
            'flake8',
            'rope'
          ]
      },
      entry_points={
          'console_scripts': ['qc=quick_command.qc:qc'],
      },
      zip_safe=False)

