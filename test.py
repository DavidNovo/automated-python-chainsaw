import boto3;
import os;


s3 = boto3.resource('s3')
portfolio_bucket = s3.Bucket('portfolio.novogrodsky.net')

for obj in portfolio_bucket.objects.all():
    print(obj.key)

build_bucket = s3.Bucket('portfoliobuild.novogrodsky.net')

print(os.path.exists('/Users/davidnovogrodsky_wrk/tmp'))


build_bucket.download_file('portfolioBuild.zip', '/Users/davidnovogrodsky_wrk/tmp/portfolioBuildNani.zip')



