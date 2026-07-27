import json
import time
import paho.mqtt.client as mqtt

from config import (
    MQTT_BROKER,
    MQTT_PORT,
    MQTT_USERNAME,
    MQTT_PASSWORD,
    MQTT_KEEPALIVE
)


class MQTTClient:

    def __init__(self):
        self.client = mqtt.Client(
            client_id="balena-demo-simulator"
        )

        if MQTT_USERNAME:
            self.client.username_pw_set(
                MQTT_USERNAME,
                MQTT_PASSWORD
            )

        self.connected = False

        # Callbacks
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect


    def on_connect(self, client, userdata, flags, rc):

        if rc == 0:
            print(
                f"MQTT connected to {MQTT_BROKER}:{MQTT_PORT}"
            )
            self.connected = True

        else:
            print(
                f"MQTT connection failed. Code: {rc}"
            )


    def on_disconnect(self, client, userdata, rc):

        self.connected = False

        if rc != 0:
            print(
                "Unexpected MQTT disconnect. Reconnecting..."
            )


    def connect(self):

        try:

            print(
                f"Connecting MQTT broker {MQTT_BROKER}:{MQTT_PORT}"
            )

            self.client.connect(
                MQTT_BROKER,
                MQTT_PORT,
                MQTT_KEEPALIVE
            )

            # Start network loop
            self.client.loop_start()

            # Wait for connection
            timeout = 10
            elapsed = 0

            while not self.connected and elapsed < timeout:
                time.sleep(1)
                elapsed += 1


            if not self.connected:
                raise Exception(
                    "Unable to connect MQTT broker"
                )


        except Exception as e:

            print(
                f"MQTT connection error: {e}"
            )

            raise



    def publish(self, topic, payload):

        if not self.connected:

            print(
                "MQTT not connected. Skipping publish."
            )

            return


        try:

            message = json.dumps(payload)

            result = self.client.publish(
                topic,
                message,
                qos=1
            )


            if result.rc != mqtt.MQTT_ERR_SUCCESS:

                print(
                    f"Failed publishing to {topic}"
                )


        except Exception as e:

            print(
                f"MQTT publish error: {e}"
            )


    def disconnect(self):

        try:

            self.client.loop_stop()
            self.client.disconnect()

            print(
                "MQTT disconnected"
            )

        except Exception as e:

            print(
                f"Disconnect error: {e}"
            )
