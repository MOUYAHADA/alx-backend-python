"""asynchronous coroutine"""
import asyncio
import random
import time


async def wait_random(max_delay=10):
    start_time = time.time()
    """waits for a random delay between 0 and max_delay"""
    await asyncio.sleep(random.uniform(0, max_delay))
    return time.time() - start_time
