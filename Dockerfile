FROM python:3.9.0
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

COPY . /app/server/MyTone

WORKDIR /app/server/MyTone

RUN apt-get update && apt-get install -y cmake && apt-get -y install libgl1-mesa-glx && apt-get install -y --no-install-recommends gcc
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# 도커라이즈 설치
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# DB연결되기까지 15초 대기시간을 설정
ENTRYPOINT ["dockerize", "-wait", "tcp://db:3306", "-timeout", "15s"]