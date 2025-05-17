FROM nginx:alpine

COPY nginx/index.html /usr/share/nginx/html/

RUN apk update && apk add iputils-ping && rm -rf /var/lib/apt/lists/*
    
CMD ["nginx", "-g", "daemon off;"]
