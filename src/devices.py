import random
import time
from datetime import datetime, timezone


class BaseDevice:

    def __init__(self, device_id, device_type):
        self.device_id = device_id
        self.device_type = device_type

        self.firmware = "1.0.0"

        self.battery = random.randint(80, 100)

        self.wifi_signal = random.randint(-65, -45)


    def timestamp(self):

        return datetime.now(
            timezone.utc
        ).isoformat()


    def common_telemetry(self):

        return {
            "deviceId": self.device_id,
            "deviceType": self.device_type,
            "firmware": self.firmware,
            "battery": self.battery,
            "wifiSignal": self.wifi_signal,
            "timestamp": self.timestamp(),
            "status": "ONLINE"
        }


    def topic(self):

        return (
            f"devices/"
            f"{self.device_type}/"
            f"{self.device_id}/"
            f"telemetry"
        )


class CoffeeMachine(BaseDevice):

    def __init__(self, device_id):

        super().__init__(
            device_id,
            "coffee"
        )

        self.water_level = random.randint(50, 100)

        self.bean_level = random.randint(50, 100)

        self.cups_served = random.randint(20, 200)

        self.temperature = 90


        self.cleaning_required = False



    def generate_telemetry(self):

        # Simulate coffee temperature
        self.temperature += random.uniform(
            -0.5,
            0.5
        )


        # Consume resources slowly

        self.water_level -= random.uniform(
            0,
            0.5
        )

        self.bean_level -= random.uniform(
            0,
            0.3
        )


        # Simulate cups served

        self.cups_served += random.randint(
            0,
            5
        )


        # Fault simulation

        if self.bean_level < 15:

            self.cleaning_required = True


        data = self.common_telemetry()


        data.update({

            "temperature":
                round(
                    self.temperature,
                    2
                ),

            "waterLevel":
                round(
                    self.water_level,
                    2
                ),

            "beanLevel":
                round(
                    self.bean_level,
                    2
                ),

            "cupsServed":
                self.cups_served,

            "cleaningRequired":
                self.cleaning_required

        })


        return data



class Refrigerator(BaseDevice):

    def __init__(self, device_id):

        super().__init__(
            device_id,
            "fridge"
        )


        self.temperature = random.uniform(
            2,
            5
        )

        self.humidity = random.randint(
            35,
            55
        )

        self.door_open = False

        self.compressor = "ON"

        self.power_consumption = random.randint(
            120,
            200
        )



    def generate_telemetry(self):


        # Normal temperature variation

        self.temperature += random.uniform(
            -0.2,
            0.2
        )


        # Random door event

        chance = random.randint(
            1,
            100
        )

        if chance <= 5:

            self.door_open = True

        else:

            self.door_open = False



        # Temperature rises if door open

        if self.door_open:

            self.temperature += random.uniform(
                1,
                3
            )


        # Compressor behaviour

        if self.temperature > 6:

            self.compressor = "ON"

        else:

            self.compressor = random.choice(
                [
                    "ON",
                    "OFF"
                ]
            )


        data = self.common_telemetry()


        data.update({

            "temperature":
                round(
                    self.temperature,
                    2
                ),

            "humidity":
                self.humidity,


            "doorOpen":
                self.door_open,


            "compressor":
                self.compressor,


            "powerConsumption":
                self.power_consumption

        })


        return data
