# docker selenium on lambda


# build image
```sh
$ chmod +x build.sh \
  && ./build.sh
```


# test image
1. run docker environment
```sh
$ docker run \
  -it \
  -p 9000:8080 \
  kagemeka/lambda-selenium:python
```
2. request from client
```sh
$ curl \
  -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" \
  -d '{}'
```

# rename
```sh
$ docker tag \
  kagemeka/lambda-selenium:python \
  <aws_account_id>.dkr.ecr.<region>.amazonaws.com/<repository>:<tag> 
```


# other reference
- docs.aws.amazon.com/lambda/latest/dg/images-create.html