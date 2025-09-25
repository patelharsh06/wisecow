FROM ubuntu:22.04

# Install required packages
RUN apt-get update && \
    apt-get install -y fortune-mod cowsay netcat-openbsd && \
    apt-get clean

# Add /usr/games to PATH so fortune and cowsay are found
ENV PATH="/usr/games:${PATH}"

# Copy the script
COPY wisecow.sh /app/wisecow.sh
WORKDIR /app
RUN chmod +x wisecow.sh

# Expose the port
EXPOSE 4499

# Run the script
CMD ["./wisecow.sh"]
