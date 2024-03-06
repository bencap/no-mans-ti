import random

from typing import Optional

from no_mans_ti.constants import Anomalies, Wormholes, SPACE_OBJECT_DISTRIBUTION


wormhole_str_map = {
    Wormholes.ALPHA: "α",
    Wormholes.BETA: "β",
    Wormholes.DELTA: "δ",
    Wormholes.GAMMA: "γ",
}

anomaly_str_map = {
    Anomalies.ASTEROID_FIELD: "A",
    Anomalies.GRAVITY_RIFT: "G",
    Anomalies.SUPERNOVA: "S",
    Anomalies.NEBULA: "N",
}


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

    def __compact_str__(self):
        """Compact string repr."""

        # XXX: ugly.
        wormhole_str = ""
        for idx, wormhole in enumerate(self.wormholes):
            if idx != 0:
                wormhole_str += ", "

            wormhole_str += wormhole_str_map[wormhole]

        anomaly_str = ""
        for idx, anomaly in enumerate(self.anomalies):
            if idx != 0:
                anomaly_str += ", "

            anomaly_str += anomaly_str_map[anomaly]

        return f"({wormhole_str} | {anomaly_str})"

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
                wormholes.add(random.choice([w for w in Wormholes]))
            else:
                anomalies.add(random.choice([a for a in Anomalies]))

        self.wormholes = wormholes
        self.anomalies = anomalies


if __name__ == "__main__":
    print(Space())
