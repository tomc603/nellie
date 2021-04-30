#!/usr/bin/env python3

import argparse
import csv
import time

from block import stat
from ipmi import sensors


def poll_collector(interval, iterations, pollfunc, *args, **kwargs):
    iteration = 0
    readings = []

    while iteration < iterations:
        iteration += 1
        start_time = time.time()
        readings.append(pollfunc(*args, **kwargs))
        runtime = time.time() - start_time
        time.sleep(max(0.0, interval - runtime))
    return readings


def ipmi_poll(interval, iterations):
    """

    :return: List of sensors.SensorData objects containing readings for each iteration
    :rtype: list[sensors.SensorData]
    """
    return poll_collector(interval, iterations, sensors.collect)


def ipmi_readings_to_rows(data):
    """

    :type data: list[SensorData]
    :rtype: list, list
    """
    column_labels = ['timestamp', ]
    output_rows = []

    for sensor_data in data:
        output_row = [sensor_data.timestamp, ]
        for k in sensor_data.readings:
            if k not in column_labels:
                column_labels.append(k)
        for label in column_labels[1:]:
            output_row.append(sensor_data.readings[label])
        output_rows.append(output_row)
    return column_labels, output_rows


def ipmi_print_readings(stats):
    header, rows = ipmi_readings_to_rows(stats)

    print(','.join(header))
    for row in rows:
        print(row)


def ipmi_readings_to_csv(stats):
    header, rows = ipmi_readings_to_rows(stats)

    with open('ipmi-sensors.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def block_poll(interval, iterations, device):
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
    return poll_collector(interval, iterations, stat.collect, device=device)


def main():
    ipmi_readings = []
    block_stat_readings = []

    parser = argparse.ArgumentParser(description='Collect system data.')
    parser.add_argument('-i', '--ipmi', action='store_true', dest='cli_collect_ipmi',
                        help='Collect IPMI sensor readings.')
    parser.add_argument('-b', '--block', action='store_true', dest='cli_collect_block',
                        help='Collect block device stats.')
    parser.add_argument('-d', '--debug', action='store_true', dest='cli_debug',
                        help='Enable debugging output for development.')
    parser.add_argument('-m', '--memory', action='store_true', dest='cli_collect_memory',
                        help='Collect memory usage stats.')
    parser.add_argument('-t', '--interval', type=float, dest='cli_interval', default=10.0,
                        help='Floating point seconds between collection intervals.')
    parser.add_argument('-c', '--iterations', type=int, dest='cli_iterations', default=1,
                        help='Number of collection iterations.')
    parser.add_argument('-D', '--device', action='append', dest='cli_devices', default='all',
                        help='Block device to collect stats from.')
    args=parser.parse_args()

    args.cli_interval = max(5.0, args.cli_interval)
    args.cli_iterations = max(1, args.cli_iterations)

    if args.cli_collect_ipmi:
        ipmi_readings = ipmi_poll(args.cli_interval, args.cli_iterations)

    # TODO: Collect stats for each device in args.cli_devices.
    # TODO: Detect 'all' special case.
    if args.cli_collect_block:
        block_stat_readings = block_poll(args.cli_interval, args.cli_iterations, 'sda')

    print(ipmi_readings, block_stat_readings)


if __name__ == '__main__':
    main()
