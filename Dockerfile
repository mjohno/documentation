FROM ubuntu:xenial

RUN apt-get update && apt-get install -y \
    gcc \
    make \
    libffi-dev \
    ruby-dev \
    ruby

RUN gem install jekyll

WORKDIR /apps

COPY . .

RUN jekyll build

EXPOSE 4000

CMD ["jekyll", "serve", "/apps", "--host", "0.0.0.0"]
