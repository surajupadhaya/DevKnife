FROM nginx:alpine


COPY nginx/index.html /usr/share/nginx/html/

RUN apt update && apt install -y iputils-ping && rm -rf /var/lib/apt/lists/*
    
CMD ["nginx", "-g", "daemon off;"]
