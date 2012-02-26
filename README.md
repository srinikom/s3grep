# s3grep

grep for Amazon S3.

Searches text files on an S3 bucket for specific content. The search is parallelised in order to
yield good performance, using multiple connections to S3.

## Usage

Search for straw in bucket 'mybucket', keys starting 'prefix':

    $ s3grep s3://mybucket/prefix straw

Supports regular expressions:

    $ s3grep s3://mybucket/prefix a.+b

To see all options:

    $ s3grep -h

## Installation

    $ pip install s3grep
or:

    $ easy_install s3grep
    
from sources, the usual:

    $ sudo python setup.py install

## AWS Credentials

Your credentials can be set through environment variables:

    AWS_ACCESS_KEY_ID - Your AWS Access Key ID
    AWS_SECRET_ACCESS_KEY - Your AWS Secret Access Key

Alternatively they can be configured in the boto configuration file,
in short, create  ~/.boto with the content:

    [Credentials]
    aws_access_key_id = <your access key>
    aws_secret_access_key = <your secret key>

## TODO

 * support for compressed content
