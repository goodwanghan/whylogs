from enum import Enum

from whylogs_v1.core.metrics.column_metrics import (
    ColumnCountsMetric,
    TypeCountersMetric,
)
from whylogs_v1.core.metrics.metrics import (
    CardinalityMetric,
    DistributionMetric,
    FrequentItemsMetric,
    IntsMetric,
    Metric,
)


class StandardMetric(Enum):
    types = TypeCountersMetric
    dist = DistributionMetric
    cnt = ColumnCountsMetric
    int = IntsMetric
    card = CardinalityMetric
    fi = FrequentItemsMetric

    def __init__(self, clz: Metric):
        self._clz = clz

    def zero(self, schema) -> Metric:  # type: ignore
        return self._clz.zero(schema)
