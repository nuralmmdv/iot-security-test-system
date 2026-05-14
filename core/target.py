from dataclasses import dataclass, field
from typing import List


@dataclass
class Target:
    host: str
    ports: List[int] = field(default_factory=lambda: [21, 22, 23, 80, 443, 8080, 8443])
    timeout: int = 5

    def __post_init__(self):
        if not self.host:
            raise ValueError("The host cannot be empty.")
        if self.timeout < 1:
            raise ValueError("Timeout must be at least 1 second.")

    def to_dict(self) -> dict:
        return {
            "host": self.host,
            "ports": self.ports,
            "timeout": self.timeout,
        }
