FROM public.ecr.aws/lambda/python:3.8

COPY src/requirements.txt /var/task/
RUN pip install -r /var/task/requirements.txt --target /var/task
# code in src/app/
COPY src /var/task

WORKDIR /var/task

CMD [api.main.handler]

# $ docker build . -t api:dev
# $ docker run --rm -p 9000:8080 --entrypoint "/usr/bin/ls" api:dev /var/task/api