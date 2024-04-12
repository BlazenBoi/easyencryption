import asyncio

from .aes import aesencrypt, aesdecrypt

teststr = "TestString"

async def aestest():
      estr = await aesencrypt(teststr)
      dstr = await aesdecrypt(estr)
      return teststr == dstr

asyncio.run(aestest())