Сгенерировать свои!
```bash
cd nginx
openssl genpkey -algorithm RSA -out nginx.key -pkeyopt rsa_keygen_bits:2048
openssl req -new -x509 -key nginx.key -out nginx.crt -days 365
```

alias не используется, так как nginx используется в режиме обратного прокси, а не в режиме сервера.
