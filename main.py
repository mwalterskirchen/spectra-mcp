from fastmcp import FastMCP
from coloraide import Color

mcp = FastMCP(name="Spectra MCP Server", instructions="This is a MCP server for converting colors between different spaces and formats.")


@mcp.tool
def oklch_to_rgb(oklch: str) -> str:
    """Convert an OKLCH color to an RGB color."""
    color = Color(oklch)
    return color.convert("srgb").to_string()

@mcp.tool
def rgb_to_oklch(rgb: str) -> str:
    """Convert an RGB color to an OKLCH color."""
    color = Color(rgb)
    return color.convert("oklch").to_string()

@mcp.tool
def hex_to_rgb(hex: str) -> str:
    """Convert a hex color to an RGB color."""
    color = Color(hex)
    return color.convert("srgb").to_string()

@mcp.tool
def rgb_to_hex(rgb: str) -> str:
    """Convert an RGB color to a hex color."""
    color = Color(rgb)
    return color.convert("srgb").to_string(hex=True)

@mcp.tool
def oklch_to_hex(oklch: str) -> str:
    """Convert an OKLCH color to a hex color."""
    color = Color(oklch)
    return color.convert("srgb").to_string(hex=True)

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)