# docker build -t dishankgoel/hackrushctf:pwn .
# docker run -d -p 1337:1337 -p 12345:12345 -p 12346:12346 -p 12347:12347 --rm -it dishankgoel/hackrushctf:pwn

FROM ubuntu:20.04

RUN apt-get update && \
      apt-get -y install sudo

RUN useradd -d /home/ctf -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY real_hack ./real_hack
COPY cliff ./cliff
COPY echo_back ./echo_back
COPY simple_login ./simple_login
COPY start.sh .

RUN chown -R root:root /home/ctf

EXPOSE 1337 12345 12346 12347

CMD ./start.sh