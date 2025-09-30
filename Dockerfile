FROM ubuntu:22.04

RUN apt-get update && apt-get install -y fortune-mod cowsay netcat-openbsd

COPY wisecow.sh /wisecow.sh
RUN chmod +x /wisecow.sh

EXPOSE 4499
CMD ["/wisecow.sh"]
