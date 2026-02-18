# FreeCAD MCP addon — no workbench registered.
# Use the FreeCADMCP macro (or toolbar button) to start/stop the server.
# This file intentionally left minimal; it just ensures the rpc_server
# package is importable when the addon is loaded.
from rpc_server import rpc_server  # noqa: F401  (registers FreeCAD commands)
