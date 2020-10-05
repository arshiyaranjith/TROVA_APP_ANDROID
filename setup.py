from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import datetime
import subprocess
import sys
from setuptools import setup
from setuptools import find_packages
nightly = False
if '--nightly' in sys.argv:
  nightly = True
  sys.argv.remove('--nightly')
project_name = 'tensorflow-examples'
version = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8')
if nightly:
  project_name = 'tensorflow-examples-nightly'
  datestring = datetime.datetime.now().strftime('%Y%m%d%H%M')
  version = '%s-dev%s' % (version, datestring)

DOCLINES = __doc__.split('\n')
REQUIRED_PKGS = [
    'absl-py',
    'six',]
TESTS_REQUIRE =[    'jupyter',]

if sys.version_info.major == 3:
  # Packages only for Python 3
  pass
else:
  TESTS_REQUIRE.append('mock')
  REQUIRED_PKGS.append('futures')

if sys.version_info < (3, 4):
  # enum introduced in Python 3.4
  REQUIRED_PKGS.append('enum34')
setup(
    name=project_name,
    version=version,
    long_description='\n'.join(DOCLINES[2:]),
    author='Google Inc.', description=DOCLINES[0],
    author_email='packages@tensorflow.org',
    url='http://github.com/tensorflow/examples',
    download_url='https://github.com/tensorflow/examples/tags',
    license='Apache 2.0',
    packages=find_packages(),
    scripts=[],
    install_requires=REQUIRED_PKGS,
    extras_require={
        'tests': TESTS_REQUIRE,
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='tensorflow examples',
)
