from mcp.server.fastmcp import  FastMCP

# Auto mở công 8000
mcp = FastMCP(
    name="mcp-sever"
)


@mcp.tool()
def add(a: int, b: int) -> int:
    "Add two numbers"
    return a + b

@mcp.tool()
def get_current_temperature_by_city(city_name:str) -> float:
    "Get current temperature by city name"
    return "20C"

#Resource: Cung cấp tài nguyên nào đó

#Prompt: Query lấy prompt cho 1 tình huống nào đó

@mcp.resource("resource://ma_so_thue")
def get_tax_code() ->str:
    "Get tax code"
    return "TAX"


@mcp.prompt()
def review_sentences(sentences: str) ->str:
     return "Review this sentences, remove any personal information: \n\n{}".format(sentences)


if __name__ == "__main__":
    # Initialize and run the server
    print("Listening on port 8080.....")
    mcp.run(transport="stdio")