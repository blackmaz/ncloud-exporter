from ncloud.request_manager import RequestManager


class ApiClient:
    def __init__(self, access_key, secret_key):
        self._rm = RequestManager(access_key, secret_key)

    def get(self, base_url, path, params=None):
        self._rm.set_base_url(base_url)
        return self._rm.request("GET", path, params=params)

    def post(self, base_url, path, json=None):
        self._rm.set_base_url(base_url)
        return self._rm.request("POST", path, json=json)

    async def get_async(self, base_url, path, session, params=None):
        self._rm.set_base_url(base_url)
        return await self._rm.async_request("GET", path, session, params=params)

    async def post_async(self, base_url, path, session, json=None):
        self._rm.set_base_url(base_url)
        return await self._rm.async_request("POST", path, session, json=json)
