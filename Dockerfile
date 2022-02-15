# Build the frontend using NodeJS
FROM node:erbium-alpine3.15 AS build
COPY . /var/www/siemens_hw
WORKDIR /var/www/siemens_hw
RUN npm i \
  && npm run build \
  && rm -rf node_modules public src package*


# Production container
FROM nginx:alpine

# Copy project files to /var/www/siemens_hw
COPY --from=build /var/www/siemens_hw /var/www/siemens_hw

WORKDIR /var/www/siemens_hw

# Install python, install pipenv, make sites-available
# and sites-enabled directories, move siemens_hw.nginx.conf 
# to sites-available, line siemens_hw.nginx.conf to 
# sites-enabled directory, mv proxy_params and nginx.conf to 
# /etc/nginx, install pyhon dependencies using pipenv
# test the python api, uninstall pytest, clean up files
RUN apk add python3 \
  && apk add py3-pip \
  && pip install pipenv \
  && mkdir -p /etc/nginx/sites-available /etc/nginx/sites-enabled \
  && mv packaging/service_files/nginx/siemens_hw.nginx.conf /etc/nginx/sites-available \
  && ln -sf /etc/nginx/sites-available/siemens_hw.nginx.conf /etc/nginx/sites-enabled/siemens_hw.nginx.conf \
  && mv packaging/service_files/nginx/proxy_params /etc/nginx/ \
  && mv packaging/service_files/nginx/nginx.conf /etc/nginx/ \
  && cd api \
  && pipenv install --dev \
  && pipenv run python -m pytest \
  && pipenv uninstall pytest \
  && rm -rf Pipfile.lock tests/ /etc/nginx/conf.d/default.conf ../packaging/service_files


CMD ["sh", "packaging/docker/start.sh"]