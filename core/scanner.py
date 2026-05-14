from typing import List
from core.target import Target
from core.finding import Finding
from core.module_loader import ModuleLoader


class Scanner:
    def __init__(self, target: Target):
        self.target = target
        self.findings: List[Finding] = []
        self.loader = ModuleLoader()

    def run(self) -> List[Finding]:
        modules = self.loader.load_all()

        if not modules:
            print("[!] No modules found.")
            return []

        print(f"[*] Target: {self.target.host}")
        print(f"[*] {len(modules)} module is installed.\n")

        for module in modules:
            print(f"[*] Working: {module.__class__.__name__}")
            try:
                results = module.run(self.target)
                self.findings.extend(results)
                print(f"[+] {len(results)} find\n")
            except Exception as e:
                print(f"[!] Error: {module.__class__.__name__} → {e}\n")

        return self.findings

    def summary(self) -> dict:
        summary = {"critical": 0, "high": 0, "medium": 0, "low": 0, "info": 0}
        for finding in self.findings:
            severity = finding.severity.lower()
            if severity in summary:
                summary[severity] += 1
        return summary
