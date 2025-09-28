<div>
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue">
  <img alt="Docker" src="https://img.shields.io/badge/Docker-ready-blue?logo=docker">
  <img alt="ROS2" src="https://img.shields.io/badge/ROS2-Humble-blueviolet?logo=ros">
  <img alt="Flask" src="https://img.shields.io/badge/Flask-3.0-lightgrey?logo=flask">
  <img alt="React" src="https://img.shields.io/badge/React-19-61DAFB?logo=react">
  <img alt="Node.js" src="https://img.shields.io/badge/Node.js-22-339933?logo=nodedotjs">
</div>

# ros2-web-bridge

**ros2-web-bridge** is a boilerplate MVP that lets a browser-based UI communicate with ROS 2 nodes through an internal HTTP bridge. It provides a ready-made, containerized starting point for ROS 2 developers building web dashboards that read data from ROS 2 topics.

The stack uses **Docker Compose** to run three lightweight services:

* **ros2**: Runs a ROS 2 *talker* node and an internal HTTP bridge (`bridge_server.py`) that exposes the latest `/chatter` message at `GET /latest` on port **9090** (within the Docker network and exposed to host).
* **backend** (Flask): Polls `http://ros2:9090/latest` every second and re-exposes it as `GET /api/chatter` on port **5000** (host-visible).
* **frontend** (Nginx serving static UI or React build): Runs on port **5173**, polls the backend (`/api/chatter`), and displays the latest message.  

This setup allows quick prototyping and development of browser-based interfaces for ROS 2 systems, with all components running in Docker containers.

---

## Main Features

* **ROS 2 → Web Bridge**: `bridge_server.py` subscribes to `/chatter` and serves **HTTP**.
* **Strict Decoupling**: Web app never links ROS libs; Flask polls the bridge over HTTP.
* **Containerized**: Same dev/prod wiring with Docker Compose.
* **Minimal UI**: Static frontend (Nginx) or React build; polls the backend regularly.
* **Extensible**: Add more topics or endpoints without touching the web stack contracts.

---

## Start Using

```bash
# 1) Create and configure .env file
# (Manually create a .env file with the following content)

echo 'ROS_DISTRO=humble
ROS_DOMAIN_ID=7
DEV_UID=1000
DEV_GID=1000' > .env

# 2) Build and run all services
docker compose up --build

# 3) Open in browser:
# Frontend UI
http://localhost:5173

# Backend API (proxies ROS2 message)
http://localhost:5000/api/chatter
```

> The **bridge** is available at `http://localhost:9090/latest` if you want to access it directly.

---

## Prerequisites

* **Docker**: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
* **Docker Compose**: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)
* **Git**
* **Node.js 22+** *(optional — only if building React UI locally before containerizing)*: [https://nodejs.org/](https://nodejs.org/)

---

## Tech Stack

* **Common:** Docker, Docker Compose
* **ROS 2:** Humble Hawksbill (Python talker via `rclpy`)
* **Bridge:** Python `bridge_server.py` (simple HTTP server)
* **Backend:** Flask 3.0 (dev server; swap to Gunicorn for prod)
* **Frontend:** Nginx serving static UI (React-ready)

---

## Project Structure

```text
ros2-web-bridge/
├── ros_ws/
│   ├── src/
│   │   └── py_basics/
│   │       ├── package.xml
│   │       ├── setup.py
│   │       ├── resource/py_basics
│   │       ├── launch/mvp.launch.py
│   │       └── py_basics/               
│   └── ros2.dev.Dockerfile
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   └── index.html                        # or React build output
├── docker-compose.yml
├── .env
└── README.md
```

---

## Architecture Principles

* **Decouple concerns**: ROS logic (ros2) vs HTTP transport (bridge) vs web app (backend/frontend).
* **Stable contract**: Web only speaks HTTP to the backend; backend only speaks HTTP to the bridge.
* **Composable**: Add endpoints/topics without cross-contamination of dependencies.

---

## License

MIT — see `LICENSE`.



