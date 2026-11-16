"""Run repeatable cooperative exploration experiments."""

import csv
import subprocess
from pathlib import Path


class ExperimentRunner:
    def __init__(self, repetitions: int = 5):
        # TODO: Store repetition count.
        # TODO: Define experiment output directory.
        # TODO: Define experiment conditions.
        pass

    def run_independent_exploration(self) -> None:
        """Run baseline with independent robot exploration."""
        # TODO: Launch baseline configuration.
        pass

    def run_fixed_allocation(self) -> None:
        """Run exploration with fixed target assignments."""
        # TODO: Launch fixed allocation configuration.
        pass

    def run_dynamic_allocation(self) -> None:
        """Run exploration with dynamic task allocation."""
        # TODO: Launch cooperative configuration.
        pass

    def repeat_experiment(self, experiment_function) -> None:
        """Repeat an experiment multiple times."""
        # TODO: Execute function for each repetition.
        pass

    def save_experiment_metadata(self, condition: str) -> None:
        """Save experiment configuration and metadata."""
        # TODO: Record condition and repetition.
        pass


def main():
    runner = ExperimentRunner(repetitions=5)

    # TODO: Execute baseline.
    # TODO: Execute fixed allocation.
    # TODO: Execute dynamic allocation.
    # TODO: Save experiment data.


if __name__ == '__main__':
    main()
