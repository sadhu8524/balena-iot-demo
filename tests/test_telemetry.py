import sys
import os


sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../src"
        )
    )
)


from devices import CoffeeMachine, Refrigerator



def test_coffee_machine_telemetry_fields():

    device = CoffeeMachine(
        "coffee-01"
    )


    telemetry = device.generate_telemetry()


    required_fields = [

        "deviceId",
        "deviceType",
        "firmware",
        "battery",
        "wifiSignal",
        "timestamp",
        "status",

        "temperature",
        "waterLevel",
        "beanLevel",
        "cupsServed",
        "cleaningRequired"

    ]


    for field in required_fields:

        assert field in telemetry



def test_refrigerator_telemetry_fields():

    device = Refrigerator(
        "fridge-01"
    )


    telemetry = device.generate_telemetry()


    required_fields = [

        "deviceId",
        "deviceType",
        "firmware",
        "battery",
        "wifiSignal",
        "timestamp",
        "status",

        "temperature",
        "humidity",
        "doorOpen",
        "compressor",
        "powerConsumption"

    ]


    for field in required_fields:

        assert field in telemetry



def test_coffee_temperature_range():

    device = CoffeeMachine(
        "coffee-01"
    )


    telemetry = device.generate_telemetry()


    # Coffee machines normally operate around 90-95°C

    assert telemetry["temperature"] > 80

    assert telemetry["temperature"] < 110



def test_fridge_temperature_range():

    device = Refrigerator(
        "fridge-01"
    )


    telemetry = device.generate_telemetry()


    # Normal fridge range plus temporary spikes

    assert telemetry["temperature"] < 15



def test_coffee_resource_values():

    device = CoffeeMachine(
        "coffee-01"
    )


    telemetry = device.generate_telemetry()


    assert telemetry["waterLevel"] >= 0

    assert telemetry["beanLevel"] >= 0



def test_refrigerator_door_state():

    device = Refrigerator(
        "fridge-01"
    )


    telemetry = device.generate_telemetry()


    assert isinstance(
        telemetry["doorOpen"],
        bool
    )



def test_device_status_online():

    coffee = CoffeeMachine(
        "coffee-01"
    )

    fridge = Refrigerator(
        "fridge-01"
    )


    assert coffee.generate_telemetry()["status"] == "ONLINE"

    assert fridge.generate_telemetry()["status"] == "ONLINE"
