#!/usr/bin/env python3

import os
import csv
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

    def _parse(self, data):
        pass

    def sub(self, other):
        pass

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


class VmStat(object):
    timestamp = None
    nr_free_pages = None
    nr_zone_inactive_anon = None
    nr_zone_active_anon = None
    nr_zone_inactive_file = None
    nr_zone_active_file = None
    nr_zone_unevictable = None
    nr_zone_write_pending = None
    nr_mlock = None
    nr_page_table_pages = None
    nr_kernel_stack = None
    nr_bounce = None
    nr_free_cma = None
    numa_hit = None
    numa_miss = None
    numa_foreign = None
    numa_interleave = None
    numa_local = None
    numa_other = None
    nr_inactive_anon = None
    nr_active_anon = None
    nr_inactive_file = None
    nr_active_file = None
    nr_unevictable = None
    nr_slab_reclaimable = None
    nr_slab_unreclaimable = None
    nr_isolated_anon = None
    nr_isolated_file = None
    workingset_nodes = None
    workingset_refault = None
    workingset_activate = None
    workingset_restore = None
    workingset_nodereclaim = None
    nr_anon_pages = None
    nr_mapped = None
    nr_file_pages = None
    nr_dirty = None
    nr_writeback = None
    nr_writeback_temp = None
    nr_shmem = None
    nr_shmem_hugepages = None
    nr_shmem_pmdmapped = None
    nr_file_hugepages = None
    nr_file_pmdmapped = None
    nr_anon_transparent_hugepages = None
    nr_unstable = None
    nr_vmscan_write = None
    nr_vmscan_immediate_reclaim = None
    nr_dirtied = None
    nr_written = None
    nr_kernel_misc_reclaimable = None
    nr_dirty_threshold = None
    nr_dirty_background_threshold = None
    pgpgin = None
    pgpgout = None
    pswpin = None
    pswpout = None
    pgalloc_dma = None
    pgalloc_dma32 = None
    pgalloc_normal = None
    pgalloc_movable = None
    allocstall_dma = None
    allocstall_dma32 = None
    allocstall_normal = None
    allocstall_movable = None
    pgskip_dma = None
    pgskip_dma32 = None
    pgskip_normal = None
    pgskip_movable = None
    pgfree = None
    pgactivate = None
    pgdeactivate = None
    pglazyfree = None
    pgfault = None
    pgmajfault = None
    pglazyfreed = None
    pgrefill = None
    pgsteal_kswapd = None
    pgsteal_direct = None
    pgscan_kswapd = None
    pgscan_direct = None
    pgscan_direct_throttle = None
    zone_reclaim_failed = None
    pginodesteal = None
    slabs_scanned = None
    kswapd_inodesteal = None
    kswapd_low_wmark_hit_quickly = None
    kswapd_high_wmark_hit_quickly = None
    pageoutrun = None
    pgrotated = None
    drop_pagecache = None
    drop_slab = None
    oom_kill = None
    pgmigrate_success = None
    pgmigrate_fail = None
    compact_migrate_scanned = None
    compact_free_scanned = None
    compact_isolated = None
    compact_stall = None
    compact_fail = None
    compact_success = None
    compact_daemon_wake = None
    compact_daemon_migrate_scanned = None
    compact_daemon_free_scanned = None
    unevictable_pgs_culled = None
    unevictable_pgs_scanned = None
    unevictable_pgs_rescued = None
    unevictable_pgs_mlocked = None
    unevictable_pgs_munlocked = None
    unevictable_pgs_cleared = None
    unevictable_pgs_stranded = None
    nr_tlb_remote_flush = None
    nr_tlb_remote_flush_received = None
    nr_tlb_local_flush_all = None
    nr_tlb_local_flush_one = None

    def __init__(self, data=None):
        if data is not None:
            self._parse(data)

    def __lt__(self, other):
        if self.timestamp is not None and other.timestamp is not None:
            return self.timestamp < other.timestamp

    def __repr__(self):
        pass

    def _parse(self, data):
        pass

    def sub(self, other):
        pass
