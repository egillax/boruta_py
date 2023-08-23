from setuptools import setup

setup(name='Boruta',
      version='0.4',
      description='Python Implementation of Boruta Feature Selection',
      url='https://github.com/egillax/boruta_py',
      download_url='https://github.com/egillax/boruta_py/tarball/v0.4',
      author='Daniel Homola',
      license='BSD 3 clause',
      packages=['boruta'],
      package_dir={'boruta': 'boruta'},
      package_data={'boruta/examples/*csv': ['boruta/examples/*.csv']},
      include_package_data=True,
      keywords=['feature selection', 'machine learning', 'random forest'],
      install_requires=['numpy>=1.10.4',
                        'scikit-learn>=0.17.1',
                        'scipy>=0.17.0'
                        ])
