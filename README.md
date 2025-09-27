# Jettison C Data Python Bindings

Auto-generated Python bindings for Jettison shared C data structures using ctypesgen.

## Target Platform
- **Architecture**: ARM64 (aarch64)
- **OS**: Ubuntu 22.04 LTS
- **Target Device**: NVIDIA Jetson AGX Orin (BSP 6.2)
- **Build Method**: QEMU ARM64 emulation in Docker

## Source
Generated from: [jettison_shared_includes](https://github.com/lpportorino/jettison_shared_includes)

## Generated Files
- `jon_shared_data_bindings.py` - Main bindings for jon_shared_data structures

## Usage
```python
from jon_shared_data_bindings import *

# Access C structures directly
state = jon_gui_state()
```

## Generation Info
- Generated: 2025-09-27 13:45:04 UTC
- Build Architecture: ARM64 (via QEMU emulation)
- Commit: 9cf3074664b1aea10a92be937f00d8a95e4c4999
- Branch: master
