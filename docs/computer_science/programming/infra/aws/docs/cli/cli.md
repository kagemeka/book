# AWS CLI


# Install
- https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
```sh
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
  && unzip awscliv2.zip \
  && sudo ./aws/install \
  -i /usr/local/aws-cli -b /usr/local/bin
```


# Configure a Profile
```sh
$ aws configure --profile=<profile> # or simply 'aws configure' to change main config.

# enter following informations
# accesskey = <ACCESSKEY>
# secretkey = <SECRETKEY>
# region = <region>
# format = <format> 
```
e.g. 
- <profile>=new-user
- <region>=ap-northeast-1
- <format>=json



# S3 
- https://docs.aws.amazon.com/cli/latest/reference/s3/index.html


## cp
- https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html
```sh
$ aws s3 cp --recursive --region=<region> --profile=<profile> <src> s3://<bucket name>/<path to upload> 
``` 

e.g. 
```sh
$ aws s3 cp \
  --recursive \
  --region=ap-northeast-1 \
  --profile=new-user \
  <src> \
  s3://<bucket>/<dst> 
```


## S3 transfer acceleration 
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration-examples.html

1. setting
```sh
# for bucket
$ aws s3api put-bucket-accelerate-configuration --bucket <bucketname> --accelerate-configuration Status=Enabled
# or for all 
$ aws configure --profile=<profile> set default.s3.use_accelerate_endpoint true
```

2. upload 
```sh 
$ aws configure --profile=<profile> set s3.addressing_style virtual
$ aws s3 cp --region=<region> <src> s3://<bucketname>/<keyname> --endpoint-url http://s3-accelerate.amazonaws.com
```


## sync
- https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html

```sh
$ aws s3 sync --profile=<profile> --region=<region> --size-only <src> <dst>
```