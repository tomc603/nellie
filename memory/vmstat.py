
import os
import time

class VmStat(object):
    _timestamp = None
    _nr_free_pages = None
    _nr_zone_inactive_anon = None
    _nr_zone_active_anon = None
    _nr_zone_inactive_file = None
    _nr_zone_active_file = None
    _nr_zone_unevictable = None
    _nr_zone_write_pending = None
    _nr_mlock = None
    _nr_page_table_pages = None
    _nr_kernel_stack = None
    _nr_bounce = None
    _nr_free_cma = None
    _numa_hit = None
    _numa_miss = None
    _numa_foreign = None
    _numa_interleave = None
    _numa_local = None
    _numa_other = None
    _nr_inactive_anon = None
    _nr_active_anon = None
    _nr_inactive_file = None
    _nr_active_file = None
    _nr_unevictable = None
    _nr_slab_reclaimable = None
    _nr_slab_unreclaimable = None
    _nr_isolated_anon = None
    _nr_isolated_file = None
    _workingset_nodes = None
    _workingset_refault = None
    _workingset_activate = None
    _workingset_restore = None
    _workingset_nodereclaim = None
    _nr_anon_pages = None
    _nr_mapped = None
    _nr_file_pages = None
    _nr_dirty = None
    _nr_writeback = None
    _nr_writeback_temp = None
    _nr_shmem = None
    _nr_shmem_hugepages = None
    _nr_shmem_pmdmapped = None
    _nr_file_hugepages = None
    _nr_file_pmdmapped = None
    _nr_anon_transparent_hugepages = None
    _nr_unstable = None
    _nr_vmscan_write = None
    _nr_vmscan_immediate_reclaim = None
    _nr_dirtied = None
    _nr_written = None
    _nr_kernel_misc_reclaimable = None
    _nr_dirty_threshold = None
    _nr_dirty_background_threshold = None
    _pgpgin = None
    _pgpgout = None
    _pswpin = None
    _pswpout = None
    _pgalloc_dma = None
    _pgalloc_dma32 = None
    _pgalloc_normal = None
    _pgalloc_movable = None
    _allocstall_dma = None
    _allocstall_dma32 = None
    _allocstall_normal = None
    _allocstall_movable = None
    _pgskip_dma = None
    _pgskip_dma32 = None
    _pgskip_normal = None
    _pgskip_movable = None
    _pgfree = None
    _pgactivate = None
    _pgdeactivate = None
    _pglazyfree = None
    _pgfault = None
    _pgmajfault = None
    _pglazyfreed = None
    _pgrefill = None
    _pgsteal_kswapd = None
    _pgsteal_direct = None
    _pgscan_kswapd = None
    _pgscan_direct = None
    _pgscan_direct_throttle = None
    _zone_reclaim_failed = None
    _pginodesteal = None
    _slabs_scanned = None
    _kswapd_inodesteal = None
    _kswapd_low_wmark_hit_quickly = None
    _kswapd_high_wmark_hit_quickly = None
    _pageoutrun = None
    _pgrotated = None
    _drop_pagecache = None
    _drop_slab = None
    _oom_kill = None
    _pgmigrate_success = None
    _pgmigrate_fail = None
    _compact_migrate_scanned = None
    _compact_free_scanned = None
    _compact_isolated = None
    _compact_stall = None
    _compact_fail = None
    _compact_success = None
    _compact_daemon_wake = None
    _compact_daemon_migrate_scanned = None
    _compact_daemon_free_scanned = None
    _unevictable_pgs_culled = None
    _unevictable_pgs_scanned = None
    _unevictable_pgs_rescued = None
    _unevictable_pgs_mlocked = None
    _unevictable_pgs_munlocked = None
    _unevictable_pgs_cleared = None
    _unevictable_pgs_stranded = None
    _nr_tlb_remote_flush = None
    _nr_tlb_remote_flush_received = None
    _nr_tlb_local_flush_all = None
    _nr_tlb_local_flush_one = None

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
    def nr_free_pages(self):
        return self._nr_free_pages

    @property
    def nr_zone_inactive_anon(self):
        return self._nr_zone_inactive_anon

    @property
    def nr_zone_active_anon(self):
        return self._nr_zone_active_anon

    @property
    def nr_zone_inactive_file(self):
        return self._nr_zone_inactive_file

    @property
    def nr_zone_active_file(self):
        return self._nr_zone_active_file

    @property
    def nr_zone_unevictable(self):
        return self._nr_zone_unevictable

    @property
    def nr_zone_write_pending(self):
        return self._nr_zone_write_pending

    @property
    def nr_mlock(self):
        return self._nr_mlock

    @property
    def nr_page_table_pages(self):
        return self._nr_page_table_pages

    @property
    def nr_kernel_stack(self):
        return self._nr_kernel_stack

    @property
    def nr_bounce(self):
        return self._nr_bounce

    @property
    def nr_free_cma(self):
        return self._nr_free_cma

    @property
    def numa_hit(self):
        return self._numa_hit

    @property
    def numa_miss(self):
        return self._numa_miss

    @property
    def numa_foreign(self):
        return self._numa_foreign

    @property
    def numa_interleave(self):
        return self._numa_interleave

    @property
    def numa_local(self):
        return self._numa_local

    @property
    def numa_other(self):
        return self._numa_other

    @property
    def nr_inactive_anon(self):
        return self._nr_inactive_anon

    @property
    def nr_active_anon(self):
        return self._nr_active_anon

    @property
    def nr_inactive_file(self):
        return self._nr_inactive_file

    @property
    def nr_active_file(self):
        return self._nr_active_file

    @property
    def nr_unevictable(self):
        return self._nr_unevictable

    @property
    def nr_slab_reclaimable(self):
        return self._nr_slab_reclaimable

    @property
    def nr_slab_unreclaimable(self):
        return self._nr_slab_unreclaimable

    @property
    def nr_isolated_anon(self):
        return self._nr_isolated_anon

    @property
    def nr_isolated_file(self):
        return self._nr_isolated_file

    @property
    def workingset_nodes(self):
        return self._workingset_nodes

    @property
    def workingset_refault(self):
        return self._workingset_refault

    @property
    def workingset_activate(self):
        return self._workingset_activate

    @property
    def workingset_restore(self):
        return self._workingset_restore

    @property
    def workingset_nodereclaim(self):
        return self._workingset_nodereclaim

    @property
    def nr_anon_pages(self):
        return self._nr_anon_pages

    @property
    def nr_mapped(self):
        return self._nr_mapped

    @property
    def nr_file_pages(self):
        return self._nr_file_pages

    @property
    def nr_dirty(self):
        return self._nr_dirty

    @property
    def nr_writeback(self):
        return self._nr_writeback

    @property
    def nr_writeback_temp(self):
        return self._nr_writeback_temp

    @property
    def nr_shmem(self):
        return self._nr_shmem

    @property
    def nr_shmem_hugepages(self):
        return self._nr_shmem_hugepages

    @property
    def nr_shmem_pmdmapped(self):
        return self._nr_shmem_pmdmapped

    @property
    def nr_file_hugepages(self):
        return self._nr_file_hugepages

    @property
    def nr_file_pmdmapped(self):
        return self._nr_file_pmdmapped

    @property
    def nr_anon_transparent_hugepages(self):
        return self._nr_anon_transparent_hugepages

    @property
    def nr_unstable(self):
        return self._nr_unstable

    @property
    def nr_vmscan_write(self):
        return self._nr_vmscan_write

    @property
    def nr_vmscan_immediate_reclaim(self):
        return self._nr_vmscan_immediate_reclaim

    @property
    def nr_dirtied(self):
        return self._nr_dirtied

    @property
    def nr_written(self):
        return self._nr_written

    @property
    def nr_kernel_misc_reclaimable(self):
        return self._nr_kernel_misc_reclaimable

    @property
    def nr_dirty_threshold(self):
        return self._nr_dirty_threshold

    @property
    def nr_dirty_background_threshold(self):
        return self._nr_dirty_background_threshold

    @property
    def pgpgin(self):
        return self._pgpgin

    @property
    def pgpgout(self):
        return self._pgpgout

    @property
    def pswpin(self):
        return self._pswpin

    @property
    def pswpout(self):
        return self._pswpout

    @property
    def pgalloc_dma(self):
        return self._pgalloc_dma

    @property
    def pgalloc_dma32(self):
        return self._pgalloc_dma32

    @property
    def pgalloc_normal(self):
        return self._pgalloc_normal

    @property
    def pgalloc_movable(self):
        return self._pgalloc_movable

    @property
    def allocstall_dma(self):
        return self._allocstall_dma

    @property
    def allocstall_dma32(self):
        return self._allocstall_dma32

    @property
    def allocstall_normal(self):
        return self._allocstall_normal

    @property
    def allocstall_movable(self):
        return self._allocstall_movable

    @property
    def pgskip_dma(self):
        return self._pgskip_dma

    @property
    def pgskip_dma32(self):
        return self._pgskip_dma32

    @property
    def pgskip_normal(self):
        return self._pgskip_normal

    @property
    def pgskip_movable(self):
        return self._pgskip_movable

    @property
    def pgfree(self):
        return self._pgfree

    @property
    def pgactivate(self):
        return self._pgactivate

    @property
    def pgdeactivate(self):
        return self._pgdeactivate

    @property
    def pglazyfree(self):
        return self._pglazyfree

    @property
    def pgfault(self):
        return self._pgfault

    @property
    def pgmajfault(self):
        return self._pgmajfault

    @property
    def pglazyfreed(self):
        return self._pglazyfreed

    @property
    def pgrefill(self):
        return self._pgrefill

    @property
    def pgsteal_kswapd(self):
        return self._pgsteal_kswapd

    @property
    def pgsteal_direct(self):
        return self._pgsteal_direct

    @property
    def pgscan_kswapd(self):
        return self._pgscan_kswapd

    @property
    def pgscan_direct(self):
        return self._pgscan_direct

    @property
    def pgscan_direct_throttle(self):
        return self._pgscan_direct_throttle

    @property
    def zone_reclaim_failed(self):
        return self._zone_reclaim_failed

    @property
    def pginodesteal(self):
        return self._pginodesteal

    @property
    def slabs_scanned(self):
        return self._slabs_scanned

    @property
    def kswapd_inodesteal(self):
        return self._kswapd_inodesteal

    @property
    def kswapd_low_wmark_hit_quickly(self):
        return self._kswapd_low_wmark_hit_quickly

    @property
    def kswapd_high_wmark_hit_quickly(self):
        return self._kswapd_high_wmark_hit_quickly

    @property
    def pageoutrun(self):
        return self._pageoutrun

    @property
    def pgrotated(self):
        return self._pgrotated

    @property
    def drop_pagecache(self):
        return self._drop_pagecache

    @property
    def drop_slab(self):
        return self._drop_slab

    @property
    def oom_kill(self):
        return self._oom_kill

    @property
    def pgmigrate_success(self):
        return self._pgmigrate_success

    @property
    def pgmigrate_fail(self):
        return self._pgmigrate_fail

    @property
    def compact_migrate_scanned(self):
        return self._compact_migrate_scanned

    @property
    def compact_free_scanned(self):
        return self._compact_free_scanned

    @property
    def compact_isolated(self):
        return self._compact_isolated

    @property
    def compact_stall(self):
        return self._compact_stall

    @property
    def compact_fail(self):
        return self._compact_fail

    @property
    def compact_success(self):
        return self._compact_success

    @property
    def compact_daemon_wake(self):
        return self._compact_daemon_wake

    @property
    def compact_daemon_migrate_scanned(self):
        return self._compact_daemon_migrate_scanned

    @property
    def compact_daemon_free_scanned(self):
        return self._compact_daemon_free_scanned

    @property
    def unevictable_pgs_culled(self):
        return self._unevictable_pgs_culled

    @property
    def unevictable_pgs_scanned(self):
        return self._unevictable_pgs_scanned

    @property
    def unevictable_pgs_rescued(self):
        return self._unevictable_pgs_rescued

    @property
    def unevictable_pgs_mlocked(self):
        return self._unevictable_pgs_mlocked

    @property
    def unevictable_pgs_munlocked(self):
        return self._unevictable_pgs_munlocked

    @property
    def unevictable_pgs_cleared(self):
        return self._unevictable_pgs_cleared

    @property
    def unevictable_pgs_stranded(self):
        return self._unevictable_pgs_stranded

    @property
    def nr_tlb_remote_flush(self):
        return self._nr_tlb_remote_flush

    @property
    def nr_tlb_remote_flush_received(self):
        return self._nr_tlb_remote_flush_received

    @property
    def nr_tlb_local_flush_all(self):
        return self._nr_tlb_local_flush_all

    @property
    def nr_tlb_local_flush_one(self):
        return self._nr_tlb_local_flush_one
