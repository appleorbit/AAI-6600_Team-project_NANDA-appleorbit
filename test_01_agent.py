import asyncio
from agent_reasoning import handle_user_query

async def test():

    response = await handle_user_query(
        "What courses do I have?"
    )

    print(response)

asyncio.run(test())
