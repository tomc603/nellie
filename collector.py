#!/usr/bin/env python3

import csv
import time

from block import stat
from ipmi import sensors


def poll_ipmi_sensors(interval, iterations):
    """

    :return: List of sensors.SensorData objects containing readings for each iteration
    :rtype: list[sensors.SensorData]
    """
    iteration = 0
    readings = []

    while iteration < iterations:
        iteration += 1
        start_time = time.time()
        readings.append(sensors.collect())
        runtime = time.time() - start_time
        time.sleep(max(0.0, interval - runtime))
    return readings


def poll_disk_stats(device, interval, iterations):
    """

    :param device: A block device name (ie: sda or nvme0n1)
    :type device: string

    :param interval: Number of seconds between collections
    :type interval: float

    :param iterations: Number of collections to perform
    :type iterations: int

    :return: List of block.DeviceStats objects
    :rtype: list[block.DeviceStats]
    """
    iteration = 0
    readings = []

    while iteration < iterations:
        iteration += 1
        start_time = time.time()
        readings.append(stat.collect(device))
        run_time = time.time() - start_time
        time.sleep(max(interval - run_time, 0))

    return readings


def main():
    ipmi_readings = poll_ipmi_sensors(10, 10)
    block_stat_readings = poll_disk_stats('sda', 10, 10)


if __name__ == '__main__':
    main()
