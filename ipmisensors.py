#!/usr/bin/env python3

import csv
import subprocess
import time
from ipmi import sensors


def poll_stats(interval, iterations):
    """

    :return: List of SensorData objects containing readings for each iteration
    :rtype: list[SensorData]
    """
    iteration = 0
    stats = []

    while iteration < iterations:
        iteration += 1
        start_time = time.time()
        stats.append(sensors.collect())
        runtime = time.time() - start_time
        time.sleep(max(0.0, interval - runtime))
    return stats


def stats_to_rows(data):
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


def print_stats(stats):
    header, rows = stats_to_rows(stats)

    print(','.join(header))
    for row in rows:
        print(row)


def stats_to_csv(stats):
    header, rows = stats_to_rows(stats)

    with open('ipmi-sensors.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


if __name__ == "__main__":
    stats_data = poll_stats(10, 3)
    stats_to_csv(stats_data)
