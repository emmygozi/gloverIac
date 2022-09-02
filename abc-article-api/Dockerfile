FROM php:8.1.9
RUN apt-get update -y && apt-get install -y openssl zip unzip git
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN docker-php-ext-install pdo_mysql
WORKDIR /app
COPY . /app
EXPOSE 8080
RUN composer install --optimize-autoloader --no-dev
CMD php artisan serve --host=0.0.0.0 --port 8080