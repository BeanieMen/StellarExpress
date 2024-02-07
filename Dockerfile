FROM archlinux:latest

WORKDIR /app
COPY . .
RUN pacman -Syu --noconfirm
RUN pacman -S --noconfirm base-devel git sudo wget python-pip
RUN bash
# RUN source bin/activate
# RUN pip install flask requests jsonify
# RUN python src/route.py