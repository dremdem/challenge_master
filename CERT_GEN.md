# Let's encrypt certificates for a domain name 

## DOCS
[let's encrypt setup](https://tproger.ru/translations/ssl-certificate/)

## Setup

Install certbot

```shell script
sudo add-apt-repository ppa:certbot/certbot
```

```shell script
apt-get update
```

```shell script
apt-get install certbot
```

```shell script
vim /etc/nginx/sites-available/default
```

Add lines to the server block:

```shell script
location ~ /.well-known {
    allow all;
}
```

```shell script
systemctl restart nginx
```

```shell script
certbot certonly --webroot --webroot-path=/var/www/html -d dremdem.ru -d www.dremdem.ru
```

```shell script
sudo ls -l /etc/letsencrypt/live/dremdem.ru/
```


# Self-signed certificate generation (that didn't work out)

## DOCS

[DO docs] (https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu-16-04)
[Telegram docs] (https://core.telegram.org/bots/self-signed)


## create 

openssl req -newkey rsa:2048 -sha256 -nodes -keyout TELEBOT_PRIVATE.key -x509 -days 365 -out TELEBOT_PUBLIC.pem -subj "/C=RU/ST=Moscow/L=Moscow/O=Dremdem company/CN=dremdem.ru"
openssl req -newkey rsa:2048 -sha256 -nodes -keyout TELEBOT_PRIVATE.key -x509 -days 365 -out TELEBOT_PUBLIC.pem -subj "/C=RU/ST=Moscow/L=Moscow/O=Dremdem company/CN=164.90.187.183"

## inspect 

```shell script
openssl x509 -text -noout -in TELEBOT_PUBLIC.pem
```

## create a strong Diffie-Hellman group

```shell script
openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
```

## Move files to ssl folder

```shell script
cp TELEBOT_PRIVATE.key /etc/ssl/private/
cp TELEBOT_PUBLIC.pem /etc/ssl/certs/
```



