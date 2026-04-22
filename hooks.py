"""Sweeppea plugin lifecycle hooks."""


def install():
    print("Sweeppea plugin installed.")
    print("Open Settings > Plugins > Sweeppea to enter your API token and connect.")


def uninstall():
    """Remove the Sweeppea MCP server from Agent Zero settings."""
    try:
        import json
        from helpers.settings import get_settings, set_settings_delta

        current = get_settings()
        mcp_raw = current.get("mcp_servers", '{"mcpServers": {}}')
        try:
            mcp_data = json.loads(mcp_raw)
        except Exception:
            mcp_data = {"mcpServers": {}}

        servers = mcp_data.get("mcpServers", {})
        if "sweeppea" in servers:
            del servers["sweeppea"]
            mcp_data["mcpServers"] = servers
            set_settings_delta({"mcp_servers": json.dumps(mcp_data, indent=2)})
            print("Sweeppea MCP server removed from Agent Zero settings.")
        else:
            print("Sweeppea MCP server was not configured — nothing to remove.")

    except Exception as e:
        print(f"Sweeppea plugin: could not remove MCP server config: {e}")
