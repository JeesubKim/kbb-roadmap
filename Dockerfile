FROM python:3.12
ENV PATH /usr/local/bin:$PATH
RUN mkdir /code

WORKDIR /code

ADD ./requirements.txt /code/requirements.txt 

RUN pip install --upgrade pip && pip install -r /code/requirements.txt

RUN pip install gunicorn 

ADD . /code

RUN ["chmod", "+x", "run.sh"]

ENTRYPOINT ["sh","./run.sh"]