import sys
import os


# Add src directory to Python path
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



def test_coffee_machine_creation():

    device = CoffeeMachine(
        "coffee-test-01"
    )

    assert device.device_id == "coffee-test-01"

    assert device.device_type == "coffee"



def test_refrigerator_creation():

    device = Refrigerator(
        "fridge-test-01"
    )

    assert device.device_id == "fridge-test-01"

    assert device.device_type == "fridge"



def test_coffee_machine_topic():

    device = CoffeeMachine(
        "coffee-01"
    )

    assert (
        device.topic()
        ==
        "devices/coffee/coffee-01/telemetry"
    )



def test_refrigerator_topic():

    device = Refrigerator(
        "fridge-01"
    )

    assert (
        device.topic()
        ==
        "devices/fridge/fridge-01/telemetry"
    )



def test_device_firmware_exists():

    coffee = CoffeeMachine(
        "coffee-01"
    )

    fridge = Refrigerator(
        "fridge-01"
    )


    assert coffee.firmware == "1.0.0"

    assert fridge.firmware == "1.0.0"



def test_device_battery_range():

    device = CoffeeMachine(
        "coffee-01"
    )


    assert device.battery >= 80

    assert device.battery <= 100
