"""Identify unexplored boundaries in an occupancy grid."""

from typing import List, Tuple

from nav_msgs.msg import OccupancyGrid


Frontier = Tuple[int, int]


class FrontierDetector:
    def __init__(self):
        # TODO: Define occupancy thresholds.
        # TODO: Initialize frontier storage.
        pass

    def is_unknown(self, value: int) -> bool:
        """Check whether a grid cell is unexplored."""
        # TODO: Check occupancy grid unknown value.
        pass

    def is_free(self, value: int) -> bool:
        """Check whether a grid cell is traversable."""
        # TODO: Check occupancy threshold.
        pass

    def get_neighbors(
        self, x: int, y: int, width: int, height: int
    ) -> List[Frontier]:
        """Return neighboring grid coordinates."""
        # TODO: Generate valid neighboring coordinates.
        pass

    def is_frontier(
        self, grid: OccupancyGrid, x: int, y: int
    ) -> bool:
        """Check whether a free cell borders an unknown cell."""
        # TODO: Check current cell.
        # TODO: Inspect neighboring cells.
        pass

    def detect_frontiers(
        self, grid: OccupancyGrid
    ) -> List[Frontier]:
        """Identify all frontier cells in the occupancy grid."""
        # TODO: Iterate through grid.
        # TODO: Collect frontier cells.
        pass

    def group_frontiers(
        self, frontiers: List[Frontier]
    ) -> List[List[Frontier]]:
        """Group neighboring frontier cells into regions."""
        # TODO: Group connected frontier cells.
        pass

    def calculate_centers(
        self, groups: List[List[Frontier]]
    ) -> List[Frontier]:
        """Calculate representative coordinates for each frontier."""
        # TODO: Calculate center of each group.
        pass

    def grid_to_world(
        self, grid: OccupancyGrid, x: int, y: int
    ) -> Tuple[float, float]:
        """Convert grid coordinates into world coordinates."""
        # TODO: Apply map resolution and origin.
        pass


def main(args=None):
    """Optional ROS 2 node entry point for frontier detection."""
    # TODO: Create a node subscribing to the shared occupancy grid.
    # TODO: Publish detected exploration targets.
    raise NotImplementedError
