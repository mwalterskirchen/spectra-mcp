from fastmcp import FastMCP
from coloraide import Color

mcp = FastMCP(
    name="Spectra MCP Server",
    instructions="""A color conversion server that provides deterministic color transformations between RGB, HEX, HSL, and OKLCH color formats.

Supported color formats:
- RGB: Accepts "rgb(255, 128, 128)", "rgb(255 128 128)", or "255, 128, 128"
- HEX: Accepts "#ff8080" or "ff8080" (with or without # prefix)
- HSL: Accepts "hsl(0 100% 75%)" or "hsl(0, 100%, 75%)" (spaces or commas)
- OKLCH: Accepts "oklch(0.7 0.2 180)" or "oklch(0.7, 0.2, 180)" (spaces or commas)

All conversions are bidirectional between these four formats. The server uses the coloraide library for accurate, mathematically precise conversions.

When converting colors:
1. Use the appropriate tool based on the source and target formats (e.g., rgb_to_hex for RGB→HEX)
2. Pass color strings in standard CSS-like formats (the parser is flexible with spaces/commas)
3. Output formats follow CSS specification standards

Example: To convert #ff8080 to HSL, use hex_to_hsl("#ff8080") which returns "hsl(0 100% 75%)"
"""
)


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

@mcp.tool
def rgb_to_hsl(rgb: str) -> str:
    """Convert an RGB color to an HSL color."""
    color = Color(rgb)
    return color.convert("hsl").to_string()

@mcp.tool
def hsl_to_rgb(hsl: str) -> str:
    """Convert an HSL color to an RGB color."""
    color = Color(hsl)
    return color.convert("srgb").to_string()

@mcp.tool
def oklch_to_hsl(oklch: str) -> str:
    """Convert an OKLCH color to an HSL color."""
    color = Color(oklch)
    return color.convert("hsl").to_string()

@mcp.tool
def hsl_to_oklch(hsl: str) -> str:
    """Convert an HSL color to an OKLCH color."""
    color = Color(hsl)
    return color.convert("oklch").to_string()

@mcp.tool
def hex_to_hsl(hex: str) -> str:
    """Convert a hex color to an HSL color."""
    color = Color(hex)
    return color.convert("hsl").to_string()

@mcp.tool
def hsl_to_hex(hsl: str) -> str:
    """Convert an HSL color to a hex color."""
    color = Color(hsl)
    return color.convert("srgb").to_string(hex=True)

@mcp.tool
def oklch_to_hex(oklch: str) -> str:
    """Convert an OKLCH color to a hex color."""
    color = Color(oklch)
    return color.convert("srgb").to_string(hex=True)

@mcp.tool
def hex_to_oklch(hex: str) -> str:
    """Convert a hex color to an OKLCH color."""
    color = Color(hex)
    return color.convert("oklch").to_string()


if __name__ == "__main__":
    mcp.run(transport="http", port=8000)