FROM archlinux:latest
EXPOSE 80

WORKDIR /app
COPY . .

RUN pacman -Syu --noconfirm && \
    pacman -S --noconfirm base-devel git sudo wget python-pip && \
    pip install flask requests jsonify --break-system-packages

RUN mkdir images
RUN git clone https://github.com/dstndstn/astrometry.net/

CMD ["python", "route.py"]