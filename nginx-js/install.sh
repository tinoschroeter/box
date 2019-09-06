apt-get install -y nginx-module-njs nginx
cp hello_world.js /etc/nginx/
rm /var/www/html/index.nginx-debian.html 
tee /etc/nginx/nginx.conf >/dev/null <<EOF
load_module modules/ngx_http_js_module.so;

events {}

http {
    js_include hello_world.js;

    server {
        listen 80;

        location / {
            js_content hello;
        }
    }
}
EOF
