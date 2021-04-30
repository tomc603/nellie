#!/usr/bin/env python3

import csv
import time

from block import stat


def poll_disk_stats(device, interval, iterations):
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
    iteration = 0
    device_stats = []

    while iteration < iterations:
        iteration += 1
        start_time = time.time()
        device_stats.append(stat.collect(device))
        run_time = time.time() - start_time
        time.sleep(max(interval - run_time, 0))

    return device_stats


def stats_to_csv(values):
    """
    Write the I/O stats between DeviceStats instances to a CSV file

    :param values: A list of DeviceStats to print
    :type values: list[DeviceStats]
    """
    with open('device-stat.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(stat.DeviceStats.fields())
        for device_stats in values:
            writer.writerow(device_stats.list())


def print_stats(values):
    """
    Print the I/O stats between DeviceStats instances

    :param values: A list of DeviceStats to print
    :type values: list[DeviceStats]
    """
    last_stat = None
    print(stat.DeviceStats.fields())
    for device_stats in values:
        if last_stat is None:
            print(device_stats.list())
        else:
            print(device_stats - last_stat)
        last_stat = device_stats


if __name__ == '__main__':
    s = poll_disk_stats('sda', 10, 3)
    # print_stats(s)
    stats_to_csv(s)
