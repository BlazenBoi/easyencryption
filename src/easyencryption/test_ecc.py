import asyncio
import pytest
pytest_plugins = ('pytest_asyncio',)

from .ecc import eccencrypt, eccdecrypt

teststr = "TestString"

@pytest.mark.asyncio
async def test_ecc():
      estr = await eccencrypt(teststr)
      dstr = await eccdecrypt(estr)
      return teststr == dstr