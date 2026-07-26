import os


# MQTT Configuration

MQTT_BROKER = os.getenv(
    "MQTT_BROKER",
    "localhost"
)

MQTT_PORT = int(
    os.getenv(
        "MQTT_PORT",
        1883
    )
)


MQTT_USERNAME = os.getenv(
    "MQTT_USERNAME",
    ""
)


MQTT_PASSWORD = os.getenv(
    "MQTT_PASSWORD",
    ""
)


MQTT_KEEPALIVE = int(
    os.getenv(
        "MQTT_KEEPALIVE",
        60
    )
)


# Telemetry publishing interval
# seconds between device messages

PUBLISH_INTERVAL = int(
    os.getenv(
        "PUBLISH_INTERVAL",
        5
    )
)


# Device configuration

DEVICE_FLEET_NAME = os.getenv(
    "DEVICE_FLEET_NAME",
    "balena-demo"
)


# Firmware version

FIRMWARE_VERSION = os.getenv(
    "FIRMWARE_VERSION",
    "1.0.0"
)
