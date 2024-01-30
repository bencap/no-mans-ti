from no_mans_ti.constants import Anomalies, Wormholes


class Space:
    wormholes: set[Wormholes]
    anomalies: set[Anomalies]

    def __init__(self, wormholes: set[Wormholes], anomalies: set[Anomalies]) -> None:
        self.wormholes = wormholes
        self.anomalies = anomalies
