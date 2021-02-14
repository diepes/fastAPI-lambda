bucket_name="medium-aws"
root_dir='$HOME/git/github-fastAPI-lambda'
cd $root_dir
aws s3 cp lambda.zip s3://$bucket_name/lambda.zip