
import os
import time


class MemInfo(object):
    _timestamp = None
    _mem_total = None
    _mem_free = None
    _mem_available = None
    _buffers = None
    _cached = None
    _swap_cached = None
    _active = None
    _inactive = None
    _active_anon = None
    _inactive_anon = None
    _active_file = None
    _inactive_file = None
    _unevictable = None
    _m_locked = None
    _swap_total = None
    _swap_free = None
    _dirty = None
    _writeback = None
    _anon_pages = None
    _mapped = None
    _shmem = None
    _k_reclaimable = None
    _slab = None
    _s_reclaimable = None
    _s_unreclaimable = None
    _kernel_stack = None
    _page_tables = None
    _nfs_unstable = None
    _bounce = None
    _writeback_tmp = None
    _commit_limit = None
    _committed_as = None
    _vmalloc_total = None
    _vmalloc_used = None
    _vmalloc_chunk = None
    _per_cpu = None
    _hardware_corrupted = None
    _direct_map_4k = None
    _direct_map_2m = None
    _direct_map_1g = None

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
        return self._mem_total

    @property
    def mem_free(self):
        return self._mem_free

    @property
    def mem_available(self):
        return self._mem_available

    @property
    def buffers(self):
        return self._buffers

    @property
    def cached(self):
        return self._cached

    @property
    def swap_cached(self):
        return self._swap_cached

    @property
    def active(self):
        return self._active

    @property
    def inactive(self):
        return self._inactive

    @property
    def active_anon(self):
        return self._active_anon

    @property
    def inactive_anon(self):
        return self._inactive_anon

    @property
    def active_file(self):
        return self._active_file

    @property
    def inactive_file(self):
        return self._inactive_file

    @property
    def unevictable(self):
        return self._unevictable

    @property
    def m_locked(self):
        return self._m_locked

    @property
    def swap_total(self):
        return self._swap_total

    @property
    def swap_free(self):
        return self._swap_free

    @property
    def dirty(self):
        return self._dirty

    @property
    def writeback(self):
        return self._writeback

    @property
    def anon_pages(self):
        return self._anon_pages

    @property
    def mapped(self):
        return self._mapped

    @property
    def shmem(self):
        return self._shmem

    @property
    def k_reclaimable(self):
        return self._k_reclaimable

    @property
    def slab(self):
        return self._slab

    @property
    def s_reclaimable(self):
        return self._s_reclaimable

    @property
    def s_unreclaimable(self):
        return self._s_unreclaimable

    @property
    def kernel_stack(self):
        return self._kernel_stack

    @property
    def page_tables(self):
        return self._page_tables

    @property
    def nfs_unstable(self):
        return self._nfs_unstable

    @property
    def bounce(self):
        return self._bounce

    @property
    def writeback_tmp(self):
        return self._writeback_tmp

    @property
    def commit_limit(self):
        return self._commit_limit

    @property
    def committed_as(self):
        return self._committed_as

    @property
    def vmalloc_total(self):
        return self._vmalloc_total

    @property
    def vmalloc_used(self):
        return self._vmalloc_used

    @property
    def vmalloc_chunk(self):
        return self._vmalloc_chunk

    @property
    def per_cpu(self):
        return self._per_cpu

    @property
    def hardware_corrupted(self):
        return self._hardware_corrupted

    @property
    def direct_map_4k(self):
        return self._direct_map_4k

    @property
    def direct_map_2m(self):
        return self._direct_map_2m

    @property
    def direct_map_1g(self):
        return self._direct_map_1g


def collect():
    return MemInfo()
