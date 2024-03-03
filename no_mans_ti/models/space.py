import random

from typing import Optional

from no_mans_ti.constants import Anomalies, Wormholes, SPACE_OBJECT_DISTRIBUTION


class Space:
    wormholes: set[Wormholes]
    anomalies: set[Anomalies]

    def __init__(
        self,
        wormholes: Optional[set[Wormholes]] = None,
        anomalies: Optional[set[Anomalies]] = None,
    ) -> None:
        if wormholes is not None and anomalies is not None:
            self.wormholes = wormholes
            self.anomalies = anomalies
        else:
            self.randomize_space()

            if wormholes is not None:
                self.wormholes = wormholes
            
            if anomalies is not None:
                self.anomalies = anomalies

    def __str__(self):
        """String repr."""
        return f"Wormholes: {self.wormholes}\nAnomalies: {self.anomalies}"

    def randomize_space(self):
        """
        Randomizes the wormholes and anomalies within a space
        area.
        """
        object_distribution = SPACE_OBJECT_DISTRIBUTION
        space_objects = random.choice(object_distribution)

        wormholes = set()
        anomalies = set()

        for i in range(space_objects):
            if random.random() > 0.5:
                wormholes.add(random.choice(Wormholes._member_names_))
            else:
                anomalies.add(random.choice(Anomalies._member_names_))

        self.wormholes = wormholes
        self.anomalies = anomalies


if __name__ == "__main__":
    print(Space())
