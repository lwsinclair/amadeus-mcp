# Amadeus MCP Server

This MCP server integrates Amadeus flight search capabilities with Claude Desktop.

## Setup

1. Environment variables required in `.env`:
```
AMADEUS_API_KEY=your_key
AMADEUS_API_SECRET=your_secret
```

2. Claude Desktop config:
```json
{
  "mcpServers": {
    "amadeus": {
      "command": "python",
      "args": ["path/to/amadeus/server.py"],
      "env": {
        "AMADEUS_API_KEY": "your_key",
        "AMADEUS_API_SECRET": "your_secret",
        "PYTHONPATH": "path/to/amadeus"
      }
    }
  }
}
```

## Available Tools

### search_flights
Parameters:
- origin: IATA airport code
- destination: IATA airport code
- date: YYYY-MM-DD format

## Troubleshooting

### Common Issues

1. Connection Timeouts
- Check server.py logs in amadeus_mcp.log
- Verify environment variables
- Check Claude Desktop logs
- See [MCP Documentation](https://modelcontextprotocol.io/llms-full.txt) for protocol details

2. Authentication Errors
- Verify Amadeus API credentials
- Check .env file permissions
- Ensure credentials are properly loaded

### Debugging Steps

1. Run standalone test:
```bash
npx @modelcontextprotocol/inspector python path/to/server.py
```

2. Check logs:
```bash
tail -f amadeus_mcp.log
```

3. Verify environment:
```python
python -c "import os; print(os.getenv('AMADEUS_API_KEY'))"
```

### Architecture Notes

- Uses FastMCP for server implementation
- Implements stdio transport
- Logs to both stderr and file
- Handles async flight search operations

## Support Resources

1. [Model Context Protocol Documentation](https://modelcontextprotocol.io/llms-full.txt)
2. [Amadeus API Documentation](https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335)
3. [Claude Desktop MCP Guide](https://modelcontextprotocol.io/docs/tools/debugging)
