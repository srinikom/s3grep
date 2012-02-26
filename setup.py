from distutils.core import setup

setup(name='s3grep',
      version='0.1',
      description='grep for Amazon S3',
      author='Barnaby Gray',
      author_email='barnaby@pickle.me.uk',
      url='http://github.com/barnybug/s3grep/',
      requires=['boto'],
      scripts=['s3grep'],
      )