#!/usr/bin/env python3
# to run this script use this
# └───> PIPENV_IGNORE_VIRTUALENVS=1 pipenv run ipython webotron.py

import boto3
import sys
import click
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys website to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    click.echo('Listing all s3 buckets')
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List objects in an s3 bucket"
    if not bucket:
        click.echo('Missing bucket name')
        sys.exit(2)
    else:
        for obj in s3.Bucket(bucket).objects.all():
            print(obj)

if __name__ == '__main__':
    cli()
