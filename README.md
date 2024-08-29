# KNIME Docker Setup

This repository contains the necessary files to set up and run a persistent KNIME installation using Docker and Docker Compose. Additionally, it includes a CI/CD pipeline configuration using GitLab CI for building and deploying the Docker image.

It is configured to mount and persist the following directories:
- `/opt/knime`
- `/home/knime-admin/knime-workspaces`

## Prerequisites

Docker on Linux ([Installation guide](https://docs.docker.com/desktop/install/linux-install/)).

## Run Docker image locally

To set up and run the KNIME Docker container locally, follow these steps:

Clone the repository:

```bash
git clone https://gitlab.argosmultilingual.com/argos-multilingual/knime.git
cd knime
```

Build the Docker image:

```bash
docker build -t knime-vnc-local .
```

Run the Docker container using Docker Compose:

```bash
docker compose -f docker-compose.yml -f docker-compose.dev.yml up
```

Access the KNIME environment locally:
- VNC: The container runs a VNC server that you can access on port 5900. You can use a VNC client to connect to localhost:5900 when running locally.
- Web Interface: Alternatively, you can access the desktop environment via your browser at http://localhost:6080.
- The default VNC dev password is 'password'.


## Deploy changes to production
 