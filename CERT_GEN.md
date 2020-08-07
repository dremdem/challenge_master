# Self-signed certificate generation

## create 

openssl req -newkey rsa:2048 -sha256 -nodes -keyout TELEBOT_PRIVATE.key -x509 -days 365 -out TELEBOT_PUBLIC.pem -subj "/C=RU/ST=Moscow/L=Moscow/O=Dremdem company/CN=dremdem.ru"

## inspect 

openssl x509 -text -noout -in TELEBOT_PUBLIC.pem



