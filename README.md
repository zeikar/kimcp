# KiMCP (Korea-integrated Model Context Protocol)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<p align="center">
  <a href="README.md">🇺🇸 English</a> |
  <a href="README.ko.md">🇰🇷 한국어</a>
</p>

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server implementation that seamlessly integrates Korean APIs into your LLM applications.

![Screenshot](screenshots/screenshot-0.png)

## Features

- **Naver Blog Search**: Search and retrieve blog content from Naver
- More features in development...

## Prerequisites

- [Claude Desktop](https://claude.ai/download)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python Package Manager)
- [Naver API credentials](https://developers.naver.com/apps/#/register)

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/zeikar/kimcp
   cd kimcp
   ```

2. **Install dependencies**

   ```bash
   uv sync
   ```

3. **Configure environment variables**

   ```bash
   echo "NAVER_CLIENT_ID=your_naver_client_id" > .env
   echo "NAVER_CLIENT_SECRET=your_naver_client_secret" >> .env
   ```

4. **Install to Claude Desktop**

   ```bash
   uv run mcp install main.py -f .env
   ```

5. **Restart Claude Desktop** to apply changes

## Development

Run the MCP inspector for testing and development:

```bash
uv run mcp dev main.py
```

## Roadmap

- ✅ Naver API integration
- ⬜ Kakao API integration
- ⬜ Korea Meteorological Administration (KMA) integration

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Special thanks to [py-mcp-naver](https://github.com/pfldy2850/py-mcp-naver)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Naver Developers](https://developers.naver.com/main)
