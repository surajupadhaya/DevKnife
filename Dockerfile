FROM nginx

# Copy static files
COPY nginx/index.html /usr/share/nginx/html/  
COPY nginx/nginx.conf /etc/nginx/ 
COPY wrapper.sh /wrapper.sh
COPY backend.py /backend.py

# Install essential DevOps tools
RUN apt update -y   && apt install -y \
      iputils-ping \
      curl \
      wget \
      openssh-server \
      bash \
      vim \
      jq \
      yq \
      python3-flask \
      python3-requests \
      net-tools \
      dnsutils \
      jsonlint \
      xmlstarlet \
      && chmod +x /wrapper.sh \
      && rm -rf /var/cache/apk/*
CMD ["/wrapper.sh"]