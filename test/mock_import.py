import sys
import builtins
from unittest.mock import MagicMock

def mock_imports(module_names):
    original_import = builtins.__import__
    def _import(name, *args, **kwargs):
        if any(map(name.startswith, module_names)):
            print("Import mocked", name)
            if name not in sys.modules:
                sys.modules[name] = MagicMock()
            return sys.modules[name]
        else:
            return original_import(name, *args, **kwargs)
    builtins.__import__ = _import
    return original_import
    
def restore_imports(module_names, original_import):
    builtins.__import__ = original_import
    for name in list(sys.modules.keys()):
        if any(map(name.startswith, module_names)):
            del sys.modules[name]
