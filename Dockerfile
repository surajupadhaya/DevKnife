FROM ubuntu:latest

RUN apt install update \

apt install iputils-ping


CMD ["/bin/bash"]
