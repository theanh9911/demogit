from mcp import ClientSession
from mcp.client.sse import sse_client


async def check():
    async with sse_client('http://127.0.0.1:8000/sse') as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()

            #List tools
            tools = await session.list_tools()
            print(tools)

            results = await  session.call_tool(name ="add", arguments= {"a" : 4,"b" : 5})
            print(results)


if __name__ == '__main__':
    import asyncio
    asyncio.run(check())