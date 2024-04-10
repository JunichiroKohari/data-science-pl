# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestOptimizeBookToBuy.test_it_snapshot[altnight-5000] result-altnight-5000'] = GenericRepr('        title  n_readers  price\n1  かんたんDjango          2   2500\n2     難しい機械学習          2   2000')

snapshots['TestOptimizeBookToBuy.test_it_snapshot[kashew-4000] result-kashew-4000'] = GenericRepr('        title  n_readers  price\n0  おいしいPython          1   1000\n2  たのしいPython          4   3000')

snapshots['TestOptimizeBookToBuy.test_it_snapshot[susumuis-3000] result-susumuis-3000'] = GenericRepr('        title  n_readers  price\n0  たのしいPython          4   3000')
