
import os
import time

class MemInfo(object):
    _timestamp = None
    _MemTotal = None
    _MemFree = None
    _MemAvailable = None
    _Buffers = None
    _Cached = None
    _SwapCached = None
    _Active = None
    _Inactive = None
    _Active_Anon = None
    _Inactive_Anon = None
    _Active_File = None
    _Inactive_File = None
    _Unevictable = None
    _Mlocked = None
    _SwapTotal = None
    _SwapFree = None
    _Dirty = None
    _Writeback = None
    _AnonPages = None
    _Mapped = None
    _Shmem = None
    _KReclaimable = None
    _Slab = None
    _SReclaimable = None
    _SUnreclaim = None
    _KernelStack = None
    _PageTables = None
    _NFS_Unstable = None
    _Bounce = None
    _WritebackTmp = None
    _CommitLimit = None
    _Committed_AS = None
    _VmallocTotal = None
    _VmallocUsed = None
    _VmallocChunk = None
    _Percpu = None
    _HardwareCorrupted = None
    _DirectMap4k = None
    _DirectMap2M = None
    _DirectMap1G = None

    def __init__(self, data=None):
        if data is not None:
            self._parse(data)

    def __lt__(self, other):
        if self.timestamp is not None and other.timestamp is not None:
            return self.timestamp < other.timestamp

    def __repr__(self):
        pass

    def __sub__(self, other):
        pass

    def _parse(self, data):
        self._timestamp = time.time()

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def mem_total(self):
        return self._MemTotal

    @property
    def mem_free(self):
        return self._MemFree

    @property
    def mem_available(self):
        return self._MemAvailable

    @property
    def buffers(self):
        return self._Buffers

    @property
    def cached(self):
        return self._Cached

    @property
    def swap_cached(self):
        return self._SwapCached

    @property
    def active(self):
        return self._Active

    @property
    def inactive(self):
        return self._Inactive

    @property
    def active_anon(self):
        return self._Active_Anon

    @property
    def inactive_anon(self):
        return self._Inactive_Anon

    @property
    def active_file(self):
        return self._Active_File

    @property
    def inactive_file(self):
        return self._Inactive_File

    @property
    def unevictable(self):
        return self._Unevictable

    @property
    def m_locked(self):
        return self._Mlocked

    @property
    def swap_total(self):
        return self._SwapTotal

    @property
    def swap_free(self):
        return self._SwapFree

    @property
    def dirty(self):
        return self._Dirty

    @property
    def writeback(self):
        return self._Writeback

    @property
    def anon_pages(self):
        return self._AnonPages

    @property
    def mapped(self):
        return self._Mapped

    @property
    def shmem(self):
        return self._Shmem

    @property
    def k_reclaimable(self):
        return self._KReclaimable

    @property
    def slab(self):
        return self._Slab

    @property
    def s_reclaimable(self):
        return self._SReclaimable

    @property
    def s_unreclaim(self):
        return self._SUnreclaim

    @property
    def kernel_stack(self):
        return self._KernelStack

    @property
    def page_tables(self):
        return self._PageTables

    @property
    def nfs_unstable(self):
        return self._NFS_Unstable

    @property
    def bounce(self):
        return self._Bounce

    @property
    def writeback_tmp(self):
        return self._WritebackTmp

    @property
    def commit_limit(self):
        return self._CommitLimit

    @property
    def committed_as(self):
        return self._Committed_AS

    @property
    def vmalloc_total(self):
        return self._VmallocTotal

    @property
    def vmalloc_used(self):
        return self._VmallocUsed

    @property
    def vmalloc_chunk(self):
        return self._VmallocChunk

    @property
    def per_cpu(self):
        return self._Percpu

    @property
    def hardware_corrupted(self):
        return self._HardwareCorrupted

    @property
    def direct_map_4k(self):
        return self._DirectMap4k

    @property
    def direct_map_2m(self):
        return self._DirectMap2M

    @property
    def direct_map_1g(self):
        return self._DirectMap1G
