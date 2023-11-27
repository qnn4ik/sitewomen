FROM nginx:latest

# remove default config
RUN rm /etc/nginx/conf.d/default.conf

# copy created configs to nginx
COPY nginx.conf /etc/nginx/conf.d
COPY proxy_params /etc/nginx