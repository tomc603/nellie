#!/usr/bin/env python3

import os
import csv
import time

import block.stat
from block import stat


def collect_disk_stats(device, interval, iterations):
    """

    :param device: A block device name (ie: sda or nvme0n1)
    :type device: string

    :param interval: Number of seconds between collections
    :type interval: float

    :param iterations: Number of collections to perform
    :type iterations: int

    :return: List of DeviceStats objects
    :rtype: list
    """
    dev_stats_path = os.path.join('/sys/block', device, 'stat')
    iteration = 0
    devicestats = []

    while iteration < iterations:
        iteration += 1
        start_time = time.time()
        with open(dev_stats_path, 'r') as f:
            data = f.read().split()
            devicestats.append(stat.DeviceStats(data))
        run_time = time.time() - start_time
        time.sleep(max(interval - run_time, 0))

    return devicestats


def stats_to_csv(values):
    """
    Write the I/O stats between DeviceStats instances to a CSV file

    :param values: A list of DeviceStats to print
    :type values: list[DeviceStats]
    """
    with open('device-stat.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(stat.DeviceStats.fields())
        for devicestat in values:
            writer.writerow(devicestat.list())


def print_stats(values):
    """
    Print the I/O stats between DeviceStats instances

    :param values: A list of DeviceStats to print
    :type values: list[DeviceStats]
    """
    last_stat = None
    print(stat.DeviceStats.fields())
    for devicestat in values:
        if last_stat is None:
            print(devicestat.list())
        else:
            print(devicestat - last_stat)
        last_stat = devicestat


if __name__ == '__main__':
    s = collect_disk_stats('sda', 10, 3)
    # print_stats(s)
    stats_to_csv(s)
