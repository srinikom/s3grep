from distutils.core import setup
__version__ = '0.1'

setup(name='s3grep',
      version=__version__,
      description='grep for Amazon S3',
      author='Barnaby Gray',
      author_email='barnaby@pickle.me.uk',
      url='http://github.com/barnybug/s3grep/',
      download_url='http://github.com/barnybug/s3grep/tarball/'+__version__+'#egg=s3grep-'+__version__,
      requires=['boto'],
      scripts=['s3grep'],
      )
