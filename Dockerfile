FROM ubuntu:latest

RUN apt update && \
    apt install -y iputils-ping


CMD ["/bin/bash"]
