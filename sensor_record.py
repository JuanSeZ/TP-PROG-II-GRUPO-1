
class SensorRecord:
    def __init__(self):
        self.sensors = []

    def get_sensors(self):
        return self.sensors

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

sensor_record = SensorRecord()