import asyncio
import pytest
pytest_plugins = ('pytest_asyncio',)

from .aes import aesencrypt, aesdecrypt

teststr = "TestString"

@pytest.mark.asyncio
async def test_aes():
      estr = await aesencrypt(teststr)
      dstr = await aesdecrypt(estr)
      return teststr == dstr