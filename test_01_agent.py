import asyncio
from agent_reasoning import handle_user_query

async def test():

    response = await handle_user_query(
        "What courses do I have?"
    )

    print(response)

asyncio.run(test())

import asyncio
from agent_reasoning import handle_user_query


async def test():

    query = "What courses do I have?"

    response = await handle_user_query(query)

    print("User:", query)
    print("Agent:", response)


asyncio.run(test())
