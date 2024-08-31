FROM elestio/docker-desktop-vnc:latest

USER root

# Install prerequisites
RUN apt update && apt install -y apt-transport-https wget gpg libunwind8

# Set timezone
#RUN ln -fs /usr/share/zoneinfo/Europe/Prague /etc/localtime && \
#    dpkg-reconfigure -f noninteractive tzdata

# Install VS Code
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
RUN install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
RUN echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | tee /etc/apt/sources.list.d/vscode.list > /dev/null
RUN rm -f packages.microsoft.gpg
RUN apt update && apt install -y code

# Install Azure Data Studio
RUN wget "https://go.microsoft.com/fwlink/?linkid=2282287" -O azuredatastudio.deb \
    && apt-get update && apt-get install -y ./azuredatastudio.deb \
    && rm azuredatastudio.deb

# Install Python and required libraries
RUN apt install -y python3 python3-pip python3-pandas python3-openpyxl python3-numpy python3-requests
RUN python3 -m pip install Office365-REST-Python-Client pyarrow

# Cleanup
RUN apt-get clean && apt-get autoremove
