#!/usr/bin/env python3
"""
Introspect jon_gui_state structure and generate documentation in JSON and Markdown formats.

This script loads the Python bindings and uses reflection to walk through
the jon_gui_state structure, documenting all fields and nested structures.

Usage:
    python3 introspect_bindings.py

Output:
    - jon_gui_state.json: JSON representation of the structure
    - jon_gui_state.md: Markdown documentation of the structure
"""

import sys
import json
import ctypes
from ctypes import Structure, Union, Array, c_char, c_byte, c_ubyte, c_short, c_ushort, c_int, c_uint, c_long, c_ulong, c_longlong, c_ulonglong, c_float, c_double, c_char_p, c_void_p, c_bool
from typing import Any, Dict, List, Optional, Type
from pathlib import Path

# Import the bindings from the current directory
sys.path.insert(0, str(Path(__file__).parent))
from jon_shared_data_bindings import jon_gui_state

def get_ctype_name(ctype: Any) -> str:
    """Get human-readable name for ctypes type."""
    type_map = {
        c_char: "char",
        c_byte: "int8",
        c_ubyte: "uint8",
        c_short: "int16",
        c_ushort: "uint16",
        c_int: "int32",
        c_uint: "uint32",
        c_long: "long",
        c_ulong: "ulong",
        c_longlong: "int64",
        c_ulonglong: "uint64",
        c_float: "float",
        c_double: "double",
        c_char_p: "char*",
        c_void_p: "void*",
        c_bool: "bool"
    }

    # Check if it's a basic type
    for base_type, name in type_map.items():
        if ctype == base_type:
            return name

    # Check if it's an array
    if hasattr(ctype, '_type_') and hasattr(ctype, '_length_'):
        element_type = get_ctype_name(ctype._type_)
        return f"{element_type}[{ctype._length_}]"

    # Check if it's a pointer
    if hasattr(ctype, '_type_'):
        if hasattr(ctype, 'contents'):
            return f"{get_ctype_name(ctype._type_)}*"

    # Check if it's a structure or union
    if hasattr(ctype, '__name__'):
        return ctype.__name__

    # Default to string representation
    return str(ctype).replace("<class '", "").replace("'>", "").split('.')[-1]

def introspect_structure(struct_class: Type[Structure], seen: Optional[set] = None, depth: int = 0, max_depth: int = 10) -> Dict[str, Any]:
    """Recursively introspect a ctypes Structure."""
    if seen is None:
        seen = set()

    # Avoid infinite recursion
    struct_name = struct_class.__name__ if hasattr(struct_class, '__name__') else str(struct_class)

    # Stop at max depth or if we've seen this structure
    if depth >= max_depth or struct_name in seen:
        return {"type": "reference", "name": struct_name}

    seen.add(struct_name)

    result = {
        "type": "structure",
        "name": struct_name,
        "fields": []
    }

    if hasattr(struct_class, '_fields_'):
        for field_entry in struct_class._fields_:
            # Handle both (name, type) and (name, type, bits) formats
            if len(field_entry) == 2:
                field_name, field_type = field_entry
            elif len(field_entry) == 3:
                field_name, field_type, _ = field_entry  # Ignore bit field size
            else:
                continue

            field_info = {
                "name": field_name,
                "ctype": get_ctype_name(field_type)
            }

            # If it's another structure, recurse
            try:
                if isinstance(field_type, type) and issubclass(field_type, (Structure, Union)):
                    field_info["details"] = introspect_structure(field_type, seen.copy(), depth + 1, max_depth)
                elif hasattr(field_type, '_type_') and hasattr(field_type, '_length_'):
                    # It's an array
                    field_info["array_length"] = field_type._length_
                    if isinstance(field_type._type_, type) and issubclass(field_type._type_, (Structure, Union)):
                        field_info["element_details"] = introspect_structure(field_type._type_, seen.copy(), depth + 1, max_depth)
            except Exception as e:
                field_info["error"] = str(e)

            result["fields"].append(field_info)

    return result

def generate_markdown(struct_info: Dict[str, Any], indent: int = 0) -> str:
    """Generate Markdown documentation from structure info."""
    lines = []
    indent_str = "  " * indent

    if struct_info["type"] == "reference":
        return f"{indent_str}- *→ {struct_info['name']}* (reference)"

    if indent == 0:
        lines.append(f"# jon_gui_state Structure Documentation\n")
        lines.append("This document describes the complete structure of the `jon_gui_state` data type.")
        lines.append("This structure is used for sharing GUI state data between components.\n")
        lines.append(f"## Structure: {struct_info['name']}\n")
    else:
        lines.append(f"{indent_str}### {struct_info['name']}")

    for field in struct_info.get("fields", []):
        field_line = f"{indent_str}- **`{field['name']}`** : `{field['ctype']}`"

        if "array_length" in field:
            field_line += f" [array of {field['array_length']}]"

        lines.append(field_line)

        if "details" in field and field["details"]["type"] != "reference":
            lines.append(generate_markdown(field["details"], indent + 1))
        elif "element_details" in field:
            lines.append(f"{indent_str}  Array element type:")
            lines.append(generate_markdown(field["element_details"], indent + 2))

    return "\n".join(lines)

def main():
    print("Introspecting jon_gui_state structure...")

    # Introspect the main structure
    structure_info = introspect_structure(jon_gui_state)

    # Generate JSON output
    json_output = json.dumps(structure_info, indent=2)
    output_dir = Path(__file__).parent

    json_path = output_dir / "jon_gui_state.json"
    with open(json_path, "w") as f:
        f.write(json_output)
    print(f"JSON documentation written to {json_path}")

    # Generate Markdown output
    md_output = generate_markdown(structure_info)
    md_path = output_dir / "jon_gui_state.md"
    with open(md_path, "w") as f:
        f.write(md_output)
    print(f"Markdown documentation written to {md_path}")

    # Print summary
    print(f"\nStructure: {structure_info['name']}")
    print(f"Number of top-level fields: {len(structure_info['fields'])}")
    print("\nTop-level fields:")
    for field in structure_info['fields']:
        print(f"  - {field['name']}: {field['ctype']}")

if __name__ == "__main__":
    main()