# Spectra MCP Server

A powerful [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server for converting colors between different color spaces and formats. Built with FastMCP and powered by the coloraide library.

## Overview

Spectra provides seamless color conversion capabilities through MCP tools, enabling AI assistants and applications to convert colors between various formats including RGB, HEX, and OKLCH color spaces. This server is ideal for design tools, theme generators, and any application requiring robust color manipulation.

## Features

- **Multiple Color Space Support**: Convert between RGB, HEX, and OKLCH color spaces
- **Bidirectional Conversions**: Convert colors in any direction between supported formats
- **High-Quality Conversions**: Powered by the coloraide library for accurate color science
- **MCP Protocol**: Standardized interface for integration with AI assistants and tools
- **HTTP Transport**: Runs as an HTTP server for easy integration

## Supported Conversions

- ✅ OKLCH → RGB
- ✅ RGB → OKLCH
- ✅ HEX → RGB
- ✅ RGB → HEX
- ✅ OKLCH → HEX

## Installation

### Prerequisites

- Python 3.14 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)

### Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd spectra-mcp
```

2. Install dependencies using uv:

```bash
uv sync
```

## Usage

### Running the Server

Start the MCP server:

```bash
uv run python main.py
```

The server will start on `http://127.0.0.1:8000` by default.

### MCP Configuration

Add the following configuration to your MCP client (e.g., in `~/.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "spectra": {
      "command": "uv",
      "args": ["run", "python", "/path/to/spectra-mcp/main.py"]
    }
  }
}
```

Or if using HTTP transport directly:

```json
{
  "mcpServers": {
    "spectra": {
      "url": "http://127.0.0.1:8000"
    }
  }
}
```

## API Reference

### Tools

#### `oklch_to_rgb`

Convert an OKLCH color to an RGB color.

**Parameters:**

- `oklch` (string): OKLCH color string (e.g., `"oklch(0.7 0.2 180)"`)

**Returns:**

- RGB color string (e.g., `"rgb(255, 128, 128)"`)

#### `rgb_to_oklch`

Convert an RGB color to an OKLCH color.

**Parameters:**

- `rgb` (string): RGB color string (e.g., `"rgb(255, 128, 128)"` or `"255, 128, 128"`)

**Returns:**

- OKLCH color string (e.g., `"oklch(0.7 0.2 180)"`)

#### `hex_to_rgb`

Convert a hex color to an RGB color.

**Parameters:**

- `hex` (string): Hex color string (e.g., `"#ff8080"` or `"ff8080"`)

**Returns:**

- RGB color string (e.g., `"rgb(255, 128, 128)"`)

#### `rgb_to_hex`

Convert an RGB color to a hex color.j

**Parameters:**

- `rgb` (string): RGB color string (e.g., `"rgb(255, 128, 128)"` or `"255, 128, 128"`)

**Returns:**

- Hex color string (e.g., `"#ff8080"`)

#### `oklch_to_hex`

Convert an OKLCH color to a hex color.

**Parameters:**

- `oklch` (string): OKLCH color string (e.g., `"oklch(0.7 0.2 180)"`)

**Returns:**

- Hex color string (e.g., `"#ff8080"`)

## Examples

### Converting OKLCH to RGB

```
Input: oklch(0.7 0.2 180)
Output: rgb(255, 128, 128)
```

### Converting RGB to OKLCH

```
Input: rgb(255, 128, 128)
Output: oklch(0.7 0.2 180)
```

### Converting HEX to RGB

```
Input: #ff8080
Output: rgb(255, 128, 128)
```

### Converting RGB to HEX

```
Input: rgb(255, 128, 128)
Output: #ff8080
```

### Converting OKLCH to HEX

```
Input: oklch(0.7 0.2 180)
Output: #ff8080
```

## Configuration

Server configuration can be modified in `fastmcp.json`:

- **Port**: Change the `port` value (default: 8000)
- **Host**: Change the `host` value (default: 127.0.0.1)
- **Log Level**: Adjust `log_level` (default: DEBUG)
- **Environment**: Modify environment variables as needed

## Dependencies

- [coloraide](https://github.com/Facelessuser/coloraide) (>=5.1): Advanced color manipulation library
- [fastmcp](https://github.com/jlowin/fastmcp) (>=2.13.0.2): Fast MCP server framework


## Acknowledgments

- Built with [FastMCP](https://github.com/jlowin/fastmcp)
- Color conversions powered by [coloraide](https://github.com/Facelessuser/coloraide)
