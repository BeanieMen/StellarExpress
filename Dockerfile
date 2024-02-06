FROM archlinux:latest

WORKDIR /
COPY ./setup.sh .
RUN bash setup.sh
COPY ./index/*.fits /usr/local/astrometry/data/
COPY ./index/download.sh /usr/local/astrometry/bin/

WORKDIR /
RUN bash
