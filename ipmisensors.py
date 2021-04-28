#!/usr/bin/env python3

import csv
import subprocess
import time


def call_stats():
    """

    :rtype subprocess.CompletedProcess
    """
    process = subprocess.run(
        ['ipmitool', 'sensor'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True)

    # print(process.stderr)
    return process


def parse_ipmi_output(stats_text):
    """

    :param stats_text:
    :type stats_text: str
    :return: Dictionary of sensor names an values
    :rtype dict
    """
    data = {}

    for line in stats_text.splitlines():
        columns = line.split('|')
        label, value = columns[0].strip(), columns[1].strip()
        if "." in value:
            value = float(value)
        elif value == "na":
            value = 0
        data[label] = value
    return data


def collect_stats(interval, iterations):
    """

    :return: Dictionary with timestamps as the keys, and parse_ipmi_output as values
    :rtype: dict[int, dict[Any, Union[int, float]]]
    """
    iteration = 0
    stats = {}

    while iteration < iterations:
        iteration += 1
        timestamp = int(time.time())
        start_time = time.time()
        p = call_stats()
        d = parse_ipmi_output(p.stdout)
        stats[timestamp] = d
        runtime = time.time() - start_time
        time.sleep(max(0.0, interval - runtime))
    return stats


def stats_to_rows(stats):
    """

    :rtype: list, list
    """
    column_labels = ['timestamp', ]
    output_rows = []
    timestamps = sorted(stats.keys())

    for timestamp in timestamps:
        output_row = [timestamp, ]
        for k in stats[timestamp]:
            if k not in column_labels:
                column_labels.append(k)
        for label in column_labels[1:]:
            output_row.append(stats[timestamp][label])
        output_rows.append(output_row)
    return column_labels, output_rows


def print_stats(stats):
    header, rows = stats_to_rows(stats)

    print(','.join(header))
    print(','.join(rows))


def stats_to_csv(stats):
    header, rows = stats_to_rows(stats)

    with open('ipmi-sensors.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


if __name__ == "__main__":
    stats_data = collect_stats(10, 3)
    stats_to_csv(stats_data)
