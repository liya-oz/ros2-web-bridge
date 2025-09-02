ARG ROS_DISTRO=humble
FROM osrf/ros:${ROS_DISTRO}-desktop
ARG DEV_UID=1000
ARG DEV_GID=1000
RUN groupadd -g ${DEV_GID} dev && useradd -m -u ${DEV_UID} -g ${DEV_GID} dev

RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions vim less git \
    && rm -rf /var/lib/apt/lists/*

ENV ROS_DISTRO=${ROS_DISTRO}
ENV ROS_DOMAIN_ID=88

WORKDIR /work

USER dev

RUN pip3 install --no-cache-dir fastapi uvicorn rclpy
# or if you keep a requirements.txt:
# COPY bridge/requirements.txt /tmp/requirements.txt
# RUN pip3 install -r /tmp/requirements.txt
