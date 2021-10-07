FROM public.ecr.aws/lambda/python:3.8

ENV DEBIAN_FRONTEND=noninteractive
RUN \
  yum update -y \
  && yum install -y \
  zip 

COPY requirements.txt .
RUN \
  mkdir -p /python \
  && pip3 install -r requirements.txt -t /python/ \
  && rm requirements.txt \
  && zip -r /python.zip /python \
  -x /python/**/__pycache__/* \
  /python/**/__pycache__/ \
  /python/__pycache__/* \
  /python/__pycache__/



ENTRYPOINT ["mv", "/python.zip"]

CMD ["/tmp/"]