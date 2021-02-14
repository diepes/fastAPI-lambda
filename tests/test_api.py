""" Testing part."""
import pytest
# from multiprocessing import Process
# import asynctest
import asyncio
# import aiohttp
import uvicorn


# content of test_assert1.py
def f():
    return 4


def test_function():
    assert f() == 4


class WebServer():
    """ Test the app class. """

    async def setUp(self):
        """ Bring server up. """
        app = App()
        self.proc = Process(target=uvicorn.run,
                            args=(app.api,),
                            kwargs={
                                "host": "127.0.0.1",
                                "port": 5000,
                                "log_level": "info"},
                            daemon=True)
        self.proc.start()
        await asyncio.sleep(0.1)  # time for the server to start

    async def tearDown(self):
        """ Shutdown the app. """
        self.proc.terminate()

    async def test_read_root(self):
        """ Fetch an endpoint from the app. """
        async with aiohttp.ClientSession() as session:
            async with session.get("http://127.0.0.1:5000/") as resp:
                data = await resp.json()
        self.assertEqual(data, {"Hello": "World"})


@pytest.fixture(scope="session")
def webapp():
    return WebServer()
