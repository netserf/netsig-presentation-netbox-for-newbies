# 🌐 NetSIG Presentation - 📦 NetBox for Newbies

Welcome to *NetBox for Newbies*! This repository contains a presentation and
demo designed to introduce you to the world of **NetBox**, the open-source
infrastructure resource modeling (IRM) tool.

Whether you're a network engineer, sysadmin, or just NetBox-curious, this repo
will help you get your bearings and maybe even have a bit of fun along the way.

[![Actions Status](https://github.com/netserf/netsig-presentation-netbox-for-newbies/workflows/Lint/badge.svg)](https://github.com/netserf/netsig-presentation-netbox-for-newbies/actions)

## 📦 Contents

- `slides/`: [PDF presentation](slides/netsig-netbox-for-newbies.pdf)
- `data/`: Data imports for NetBox demo
- `scripts/`: Scripts and configurations used in the NetBox demo

## 👥 Who is this for?

- Network operators who want a better way to manage sites, devices, IPs, etc.
- Engineers tired of tracking infrastructure in spreadsheets
- Anyone who’s heard of NetBox but hasn’t had a chance to try it
- People looking for ways to improve network documentation and automation

## 🎯 What you'll learn

- What NetBox is and why people use it
- Key concepts: Sites, Devices, Racks, IPAM, and more
- How to install and run NetBox (locally or with Docker)
- How to use NetBox’s web UI to manage your infrastructure
- A peek at the API and automation potential

## 🧰 Pre-requisites

- Basic knowledge of networking (IP addresses, VLANs, devices)
- Familiarity with the Linux command line
- (Optional) Docker installed if you want to try the demo

## 🎤 Presentation

- The slide deck is available here:\
  📽️ [netbox-for-newbies.pdf](slides/netsig-netbox-for-newbies.pdf) (coming soon!)

## 🛜 Who is NetSIG?

NetSIG is a Special Interest Group focused on computer networking. We're
affiliated with Victoria Raspberry PiMakers group located in Victoria, Canada.
These presentations are hosted in person and on-line.

## ❓ Where can I find more on NETSIG and presentation schedules?

- [NetSIG site](https://vicpimakers.ca/netsig/)
- [Victoria PiMakers site](https://vicpimakers.ca/)

## 🛠️ Demo

- A simple demo environment to try out NetBox yourself!

1. Clone this repo:

   ```bash
   git clone https://github.com/netbox-community/netbox-docker.git
   cd netbox-docker
   ```

1. Launch NetBox with Docker:

   ```bash
   docker compose up -d
   ```

1. Configure the admin password:

    ```bash
    docker exec -it netboxdemo-netbox-1 /opt/netbox/netbox/manage.py \
        changepassword admin
    ```

1. Open your browser to [http://localhost:8000](http://localhost:8000)

1. Login with:

   - **Username:** `admin`
   - **Password:** `(newly configured password)`

1. Start exploring! 🎈

## 🙏 Feedback

- Spotted a typo? Got a better way to explain a concept?
- I’d love your feedback! Open an issue or pull request 🛠️

## 🧠 Acknowledgements

- [NetBox Project](https://github.com/netbox-community/netbox) – the real stars
  of the show 🌟
- [NetBox Docker](https://github.com/netbox-community/netbox-docker) – for an
  easy demo site

## 🪪 License

[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

This content is licensed under the Creative Commons Attribution 4.0
International License.
