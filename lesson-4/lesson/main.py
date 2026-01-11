import subprocess

from mcp.server.fastmcp import FastMCP

mcp = FastMCP('demo')

#Web Server -> Endpoints
#MCP Server -> Tools

@mcp.tool()
def add(a: float, b:float) -> float:
    """
    Adds two numbers and return result
    """

    return a + b

@mcp.tool()
def terminal(command: str)-> str:
    """
    Run a terminal command inside the workpace directory
    Args:
        command: The terminal command to run.
    Returns:
        The command output or an error message
    """
    try:

        result = subprocess.run(command, shell=True, capture_output=True, cwd = "D:\my data\AI Agent\lesson-4")

        if result is not None:
            try:
                return result.stdout.decode("utf-8")
            except Exception as e:
                return ""
    except Exception as e:
        return str(e)
    
if __name__ == "__main__":
    mcp.run(transport="stdio")

#mcp dev main.py
#mcp install main.py

