
import subprocess
import time


class SensorData(object):
    _timestamp = None
    readings = {}

    def __init__(self, data=None):
        if data is not None:
            self._parse(data)

    def __gt__(self, other):
        return self.timestamp > other.timestamp

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def _parse(self, data):
        """

        :param data: Text output from ipmi sensors command
        :type data: str
        """
        self._timestamp = time.time()

        for line in data.splitlines():
            columns = line.split('|')
            label, value = columns[0].strip(), columns[1].strip()

            # Clean up some known data types
            if "." in value:
                value = float(value)
            elif value == "na":
                value = 0

            self.readings[label] = value

    @property
    def timestamp(self):
        return self._timestamp


def collect():
    process = subprocess.run(
        ['ipmitool', 'sensor'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True)

    return SensorData(process.stdout)
