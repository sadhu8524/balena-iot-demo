import signal
import sys
import time

from config import PUBLISH_INTERVAL
from devices import CoffeeMachine, Refrigerator
from mqtt_client import MQTTClient


class FleetSimulator:
    def __init__(self):
        self.running = True

        self.devices = [
            CoffeeMachine("coffee-01"),
            CoffeeMachine("coffee-02"),
            CoffeeMachine("coffee-03"),
            CoffeeMachine("coffee-04"),
            Refrigerator("fridge-01"),
            Refrigerator("fridge-02"),
            Refrigerator("fridge-03"),
            Refrigerator("fridge-04"),
        ]

        self.mqtt = MQTTClient()

    def stop(self, *_):
        print("\nStopping simulator...")
        self.running = False
        self.mqtt.disconnect()
        sys.exit(0)

    def publish_device(self, device):
        topic = device.topic()
        payload = device.generate_telemetry()

        print(f"[{device.device_id}] -> {payload}")

        self.mqtt.publish(topic, payload)

    def run(self):

        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

        self.mqtt.connect()

        print("=" * 60)
        print("Balena Demo Fleet Simulator")
        print("=" * 60)

        print(f"Connected devices : {len(self.devices)}")

        for device in self.devices:
            print(f" - {device.device_id}")

        print("=" * 60)

        while self.running:

            for device in self.devices:
                self.publish_device(device)

            time.sleep(PUBLISH_INTERVAL)


if __name__ == "__main__":
    simulator = FleetSimulator()
    simulator.run()
