import importlib
import os
from typing import List
from core.finding import Finding


class ModuleLoader:
    def __init__(self, modules_dir: str = "modules"):
        self.modules_dir = modules_dir

    def load_all(self) -> List:
        modules = []
        for folder in sorted(os.listdir(self.modules_dir)):
            folder_path = os.path.join(self.modules_dir, folder)
            if not os.path.isdir(folder_path):
                continue
            module_file = os.path.join(folder_path, "module.py")
            if not os.path.exists(module_file):
                continue
            module = self._load(folder)
            if module:
                modules.append(module)
        return modules

    def _load(self, folder_name: str):
        try:
            module_path = f"modules.{folder_name}.module"
            imported = importlib.import_module(module_path)
            cls = getattr(imported, "Module")
            return cls()
        except Exception as e:
            print(f"[!] Module cannot be installed: {folder_name} → {e}")
            return None
