# NGNIX SETUP

## Development setup

### Description

In order to debug our application I'm going to setup dev server with NGNIX.
Why I'm doing it? If I'm planning to use webhook then I have to use SSL. 
For the first very basic step I don't want to make an individual domain name.
It will be a VPS with associated ip-address only.
The only way to manage webhook with ip-address is a self-signed certificate.
I don't find the way how to manage it in dev-mode.

> To be honest - yes, but I didn't tried so far.
> https://isotoma.com/blog/2012/07/17/running-a-django-dev-instance-over-https/
> https://www.ianlewis.org/en/testing-https-djangos-development-server

The plan is: 
1. Run dev-server remotely at port 9000
2. Issue self-signed cert for my local IP
3. Setup the ngnix to proxy incoming HTTPS-request to a dev-server.
4. PROFIT!

Later in a prod I'll change this shitty-setup to a right, well-designed PrODuCtion setup :) 

### Setup



```shell script
vim /etc/nginx/snippets/ssl-params.conf
```

```shell script
# Источники: https://cipherli.st/
# и https://raymii.org/s/tutorials/Strong_SSL_Security_On_nginx.html

ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_prefer_server_ciphers on;
ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";
ssl_ecdh_curve secp384r1;
ssl_session_cache shared:SSL:10m;
ssl_session_tickets off;
ssl_stapling on;
ssl_stapling_verify on;
resolver 8.8.8.8 8.8.4.4 valid=300s;
resolver_timeout 5s;
# отключаем заголовочный файл HSTS
# add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload";
add_header X-Frame-Options DENY;
add_header X-Content-Type-Options nosniff;

ssl_dhparam /etc/ssl/certs/dhparam.pem;
```

```shell script
vim /etc/nginx/snippets/dremdem.ru.conf
```

```shell script
ssl_certificate /etc/letsencrypt/live/dremdem.ru/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/dremdem.ru/privkey.pem;
```

```shell script
vim /etc/nginx/sites-available/cm
```

```shell script
server {
    listen 443 ssl;
    listen [::]:443 ssl;
    include snippets/dremdem.ru.conf;
    include snippets/dremdem.ru.conf;

    server_name dremdem.ru;  
  
    location / {
        include proxy_params;
        proxy_pass http://localhost:9000;
    }
}
```

```shell script
ln -s /etc/nginx/sites-available/cm /etc/nginx/sites-enabled
```

```shell script
sudo nginx -t
```

```shell script
sudo systemctl restart nginx
```

## LINKS

[ngnix redirecting to dev-server](https://dizballanze.com/ru/nastraivaem-dev-server-dlia-udobnoi-razrabotki-na-django/)
[DO tutorial how self-signed setup](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu-16-04)
[one more self-signed setup](https://hostadvice.com/how-to/how-to-configure-nginx-to-use-self-signed-ssl-tls-certificate-on-ubuntu-18-04-vps-or-dedicated-server/)
[let's encrypt setup](https://tproger.ru/translations/ssl-certificate/)
