#!/usr/bin/env python3
'''
task 0
'''

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
    an asynchronous function that waits till the max_dalay
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
