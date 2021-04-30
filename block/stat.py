
import os
import time


class DeviceStats(object):
    _timestamp = None
    _read_ios = None
    _read_merges = None
    _read_sectors = None
    _read_ticks = None
    _write_ios = None
    _write_merges = None
    _write_sectors = None
    _write_ticks = None
    _ios_progress = None
    _total_ticks = None
    _rq_ticks = None
    _discard_ios = None
    _discard_merges = None
    _discard_sectors = None
    _discard_ticks = None
    _flush_ios = None
    _flush_ticks = None

    def __init__(self, data):
        self._parse(data)

    def __repr__(self):
        reprstr = \
            "<{}(ts={}, read_ios={}, read_merges={}, read_sectors={}, read_ticks={}, write_ios={}," \
            "write_merges={}, write_sectors={}, write_ticks={}, ios_progress={}, total_ticks={}, rq_ticks={}" \
            "discard_ios={}, discard_merges={}, discard_sectors={}, discard_ticks={}, flush_ios={}," \
            "flush_ticks={})>".format(
                self.__class__.__name__,
                self.timestamp,
                self.read_ios,
                self.read_merges,
                self.read_sectors,
                self.read_ticks,
                self.write_ios,
                self.write_merges,
                self.write_sectors,
                self.write_ticks,
                self.ios_progress,
                self.total_ticks,
                self.rq_ticks,
                self.discard_ios,
                self.discard_merges,
                self.discard_sectors,
                self.discard_ticks,
                self.flush_ios,
                self.flush_ticks)
        return reprstr

    def __sub__(self, other):
        """
        Calculate the difference between the current values and the values supplied in new

        :param other: A DeviceStats to subtract from the current
        :type other: DeviceStats
        :return: tuple
        """
        return (
            self.timestamp - other.timestamp,
            self.read_ios - other.read_ios,
            self.read_merges - other.read_merges,
            self.read_sectors - other.read_sectors,
            self.read_ticks - other.read_ticks,
            self.write_ios - other.write_ios,
            self.write_merges - other.write_merges,
            self.write_sectors - other.write_sectors,
            self.write_ticks - other.write_ticks,
            self.ios_progress - other.ios_progress,
            self.total_ticks - other.total_ticks,
            self.rq_ticks - other.rq_ticks,
            self.discard_ios - other.discard_ios if self.discard_ios is not None else 0,
            self.discard_merges - other.discard_merges if self.discard_merges is not None else 0,
            self.discard_sectors - other.discard_sectors if self.discard_sectors is not None else 0,
            self.discard_ticks - other.discard_ticks if self.discard_ticks is not None else 0,
            self.flush_ios - other.flush_ios if self.flush_ios is not None else 0,
            self.flush_ticks - other.flush_ticks if self.flush_ticks is not None else 0,
        )

    def _parse(self, data):
        """
        Read a list of values, and place them into the proper fields

        :param data: A list of elements from a device's stats file
        :type data: list
        """
        self._timestamp = time.time()
        if len(data) >= 11:
            self._read_ios = int(data[0])
            self._read_merges = int(data[1])
            self._read_sectors = int(data[2])
            self._read_ticks = int(data[3])
            self._write_ios = int(data[4])
            self._write_merges = int(data[5])
            self._write_sectors = int(data[6])
            self._write_ticks = int(data[7])
            self._ios_progress = int(data[8])
            self._total_ticks = int(data[9])
            self._rq_ticks = int(data[10])

            if len(data) >= 15:
                self._discard_ios = int(data[11])
                self._discard_merges = int(data[12])
                self._discard_sectors = int(data[13])
                self._discard_ticks = int(data[14])

            if len(data) >= 17:
                self._flush_ios = int(data[15])
                self._flush_ticks = int(data[16])

    @staticmethod
    def fields():
        return ('timestamp', 'read ios', 'read merges', 'read sectors',
                'read ticks', 'write ios', 'write merges',
                'write sectors', 'write ticks', 'ios progress',
                'total ticks', 'rq ticks', 'discard ios', 'discard merges',
                'discard sectors', 'discard ticks', 'flush ios',
                'flush ticks')

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def read_ios(self):
        return self._read_ios

    @property
    def read_merges(self):
        return self._read_merges

    @property
    def read_sectors(self):
        return self._read_sectors

    @property
    def read_ticks(self):
        return self._read_ticks

    @property
    def write_ios(self):
        return self._write_ios

    @property
    def write_merges(self):
        return self._write_merges

    @property
    def write_sectors(self):
        return self._write_sectors

    @property
    def write_ticks(self):
        return self._write_ticks

    @property
    def ios_progress(self):
        return self._ios_progress

    @property
    def total_ticks(self):
        return self._total_ticks

    @property
    def rq_ticks(self):
        return self._rq_ticks

    @property
    def discard_ios(self):
        return self._discard_ios

    @property
    def discard_merges(self):
        return self._discard_merges

    @property
    def discard_sectors(self):
        return self._discard_sectors

    @property
    def discard_ticks(self):
        return self._discard_ticks

    @property
    def flush_ios(self):
        return self._flush_ios

    @property
    def flush_ticks(self):
        return self._flush_ticks

    def list(self):
        """
        Return a tuple containing the values from DeviceStats

        :return: Tuple of values in DeviceStats
        :rtype: tuple
        """
        return (
            self.timestamp,
            self.read_ios,
            self.read_merges,
            self.read_sectors,
            self.read_ticks,
            self.write_ios,
            self.write_merges,
            self.write_sectors,
            self.write_ticks,
            self.ios_progress,
            self.total_ticks,
            self.rq_ticks,
            self.discard_ios if self.discard_ios is not None else 0,
            self.discard_merges if self.discard_merges is not None else 0,
            self.discard_sectors if self.discard_sectors is not None else 0,
            self.discard_ticks if self.discard_ticks is not None else 0,
            self.flush_ios if self.flush_ios is not None else 0,
            self.flush_ticks if self.flush_ticks is not None else 0
        )


def collect(device):
    dev_stats_path = os.path.join('/sys/block', device, 'stat')

    with open(dev_stats_path, 'r') as f:
        data = f.read().split()
        return DeviceStats(data)
