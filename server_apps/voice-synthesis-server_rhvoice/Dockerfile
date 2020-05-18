FROM php:7.2-cli

ENV RHVOICE_PATH /opt/RHVoice

RUN apt-get update --allow-releaseinfo-change

RUN apt-get install -y pkg-config \
    && apt-get install -y scons \
    && apt-get install -y git \
    # Lib that allows make audio output to file
    && apt-get install -y libao-dev \
    # Lib to convert wav -> mp3
    && apt-get install -y lame \
    # python
    && apt-get install -y python3 python-pip \
    && pip install lxml

WORKDIR $RHVOICE_PATH

RUN git clone --progress --depth=1 -b 1.2.2 https://github.com/Olga-Yakovleva/RHVoice.git .
RUN scons install && ldconfig

ADD ./dicts /usr/local/etc/RHVoice/dicts/
ADD ./php-www/ /var/www/html/

WORKDIR /var/www/html

EXPOSE 8080

CMD ["php", "-S", "0.0.0.0:8080"]
