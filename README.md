# Spectra MCP Server

A powerful [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server for converting colors between different color spaces and formats. Built with FastMCP and powered by the coloraide library.

## 🌐 Hosted Deployment

**Spectra is now available as a hosted service!** No installation required - integrate directly with any MCP client that supports remote HTTP servers.

**Server URL:** `https://spectra-mcp.fastmcp.app/mcp`

Simply add the URL to your MCP client configuration and start using color conversion tools immediately.

## Overview

Spectra provides seamless color conversion capabilities through MCP tools, enabling AI assistants and applications to convert colors between various formats including RGB, HEX, HSL, and OKLCH color spaces. This server is ideal for design tools, theme generators, and any application requiring robust color manipulation.

### Why Spectra?

Large Language Models (LLMs) struggle with converting colors between different formats in a deterministic way. Even seemingly simple conversions like `#ff8080` to RGB or OKLCH to HEX can produce inconsistent or incorrect results when attempted through pure reasoning. Spectra solves this problem by providing reliable, deterministic color conversion tools that AI assistants can call, ensuring accurate and consistent color transformations every time.

## Features

- **🌐 Hosted Service**: Available remotely at `https://spectra-mcp.fastmcp.app/mcp` - no installation needed
- **Multiple Color Space Support**: Convert between RGB, HEX, HSL, and OKLCH color spaces
- **Bidirectional Conversions**: Convert colors in any direction between supported formats
- **High-Quality Conversions**: Powered by the coloraide library for accurate color science
- **MCP Protocol**: Standardized interface for integration with AI assistants and tools
- **HTTP Transport**: Supports remote HTTP MCP servers for seamless integration

## Supported Conversions

The following table shows all supported color format conversions:

| From \ To | RGB | HEX | HSL | OKLCH |
| --------- | --- | --- | --- | ----- |
| **RGB**   | —   | ✅  | ✅  | ✅    |
| **HEX**   | ✅  | —   | ✅  | ✅    |
| **HSL**   | ✅  | ✅  | —   | ✅    |
| **OKLCH** | ✅  | ✅  | ✅  | —     |

All conversions are bidirectional—you can convert between any two formats in either direction.

## Installation

### 🚀 Quick Start (Recommended - Hosted Service)

The easiest way to use Spectra is via the hosted service. No installation or setup required!

### One-Click Installation

#### Cursor IDE

**Option 1: Via Settings UI**

1. Open Cursor Settings (`Cmd/Ctrl + ,`)
2. Navigate to **Features** → **MCP** (or **AI** → **MCP Servers**)
3. Click **"Add Server"** or **"+ Add New MCP Server"**
4. Configure:
   - **Name**: `Spectra` (or any name you prefer)
   - **URL**: `https://spectra-mcp.fastmcp.app/mcp`
5. Save and restart Cursor

**Option 2: Via Configuration File**

1. Open or create `~/.cursor/mcp.json` (macOS/Linux) or `%APPDATA%\Cursor\mcp.json` (Windows)
2. Add the following configuration:

```json
{
  "mcpServers": {
    "spectra": {
      "url": "https://spectra-mcp.fastmcp.app/mcp"
    }
  }
}
```

3. Save and restart Cursor

#### Claude Desktop

1. Open the Claude Desktop configuration file:

   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`

2. Add Spectra to the `mcpServers` section:

```json
{
  "mcpServers": {
    "spectra": {
      "url": "https://spectra-mcp.fastmcp.app/mcp"
    }
  }
}
```

3. Save the file and restart Claude Desktop

#### Other MCP Clients

For any MCP client that supports remote HTTP servers, add this configuration:

```json
{
  "mcpServers": {
    "spectra": {
      "url": "https://spectra-mcp.fastmcp.app/mcp"
    }
  }
}
```

Refer to your client's documentation for the exact location of the configuration file.

---

### 💻 Development Setup (For Contributors)

If you want to contribute to Spectra or run it locally:

#### Prerequisites

- Python 3.14 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)

#### Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd spectra-mcp
```

2. Install dependencies using uv:

```bash
uv sync
```

3. Start the server:

```bash
uv run python main.py
```

The server will start on `http://127.0.0.1:8000` by default.

4. Configure your MCP client to use the local server:

```json
{
  "mcpServers": {
    "spectra": {
      "url": "http://127.0.0.1:8000"
    }
  }
}
```

Or using command transport:

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

Convert an RGB color to a hex color.

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

#### `hex_to_oklch`

Convert a hex color to an OKLCH color.

**Parameters:**

- `hex` (string): Hex color string (e.g., `"#ff8080"` or `"ff8080"`)

**Returns:**

- OKLCH color string (e.g., `"oklch(0.7 0.2 180)"`)

#### `rgb_to_hsl`

Convert an RGB color to an HSL color.

**Parameters:**

- `rgb` (string): RGB color string (e.g., `"rgb(255, 128, 128)"` or `"255, 128, 128"`)

**Returns:**

- HSL color string (e.g., `"hsl(0 100% 75%)"`)

#### `hsl_to_rgb`

Convert an HSL color to an RGB color.

**Parameters:**

- `hsl` (string): HSL color string (e.g., `"hsl(0 100% 75%)"`)

**Returns:**

- RGB color string (e.g., `"rgb(255, 128, 128)"`)

#### `oklch_to_hsl`

Convert an OKLCH color to an HSL color.

**Parameters:**

- `oklch` (string): OKLCH color string (e.g., `"oklch(0.7 0.2 180)"`)

**Returns:**

- HSL color string (e.g., `"hsl(0 100% 75%)"`)

#### `hsl_to_oklch`

Convert an HSL color to an OKLCH color.

**Parameters:**

- `hsl` (string): HSL color string (e.g., `"hsl(0 100% 75%)"`)

**Returns:**

- OKLCH color string (e.g., `"oklch(0.7 0.2 180)"`)

#### `hex_to_hsl`

Convert a hex color to an HSL color.

**Parameters:**

- `hex` (string): Hex color string (e.g., `"#ff8080"` or `"ff8080"`)

**Returns:**

- HSL color string (e.g., `"hsl(0 100% 75%)"`)

#### `hsl_to_hex`

Convert an HSL color to a hex color.

**Parameters:**

- `hsl` (string): HSL color string (e.g., `"hsl(0 100% 75%)"`)

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

### Converting HEX to OKLCH

```
Input: #ff8080
Output: oklch(0.7 0.2 180)
```

### Converting RGB to HSL

```
Input: rgb(255, 128, 128)
Output: hsl(0 100% 75%)
```

### Converting HSL to RGB

```
Input: hsl(0 100% 75%)
Output: rgb(255, 128, 128)
```

### Converting OKLCH to HSL

```
Input: oklch(0.7 0.2 180)
Output: hsl(0 100% 75%)
```

### Converting HSL to OKLCH

```
Input: hsl(0 100% 75%)
Output: oklch(0.7 0.2 180)
```

### Converting HEX to HSL

```
Input: #ff8080
Output: hsl(0 100% 75%)
```

### Converting HSL to HEX

```
Input: hsl(0 100% 75%)
Output: #ff8080
```

## Configuration

### Remote/Hosted Server

No configuration needed! The hosted service at `https://spectra-mcp.fastmcp.app/mcp` is ready to use.

### Local Server

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
