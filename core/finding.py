from dataclasses import dataclass
from typing import Optional


@dataclass
class Finding:
    module_id: str
    title: str
    severity: str
    description: str
    recommendation: str
    evidence: Optional[str] = None

    SEVERITY_LEVELS = ["critical", "high", "medium", "low", "info"]

    def to_dict(self) -> dict:
        return {
            "module_id": self.module_id,
            "title": self.title,
            "severity": self.severity,
            "description": self.description,
            "recommendation": self.recommendation,
            "evidence": self.evidence,
        }
