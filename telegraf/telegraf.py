###############################################################################
# Telegraf Agent Configuration
# Balena Demo IoT Fleet
###############################################################################

[agent]

  interval = "5s"

  round_interval = true

  metric_batch_size = 1000

  metric_buffer_limit = 10000

  collection_jitter = "0s"

  flush_interval = "5s"

  flush_jitter = "0s"

  precision = ""



###############################################################################
# MQTT CONSUMER INPUT
###############################################################################

[[inputs.mqtt_consumer]]

  ## MQTT broker
  servers = [
    "tcp://mosquitto:1883"
  ]


  ## Subscribe to all devices

  topics = [

    "devices/coffee/+/telemetry",

    "devices/fridge/+/telemetry"

  ]


  qos = 1


  connection_timeout = "30s"


  ## JSON telemetry

  data_format = "json"



  ## Fields that should remain strings

  json_string_fields = [

    "deviceId",

    "deviceType",

    "firmware",

    "status",

    "compressor"

  ]



###############################################################################
# OPTIONAL TAG EXTRACTION
###############################################################################

  tag_keys = [

    "deviceId",

    "deviceType",

    "firmware",

    "status"

  ]



###############################################################################
# INFLUXDB OUTPUT
###############################################################################

[[outputs.influxdb_v2]]

  urls = [

    "http://influxdb:8086"

  ]


  token = "$INFLUX_TOKEN"


  organization = "balena-demo"


  bucket = "iot"
