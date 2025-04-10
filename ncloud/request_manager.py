import time
import logging
import requests
import base64
import hashlib
import hmac
from ncloud.response_data import ResponseData

logger = logging.getLogger(__name__)


class RequestManager:
    def __init__(self, access_key, access_secret, base_url=None):
        self.access_key = access_key
        self.access_secret = access_secret
        self.base_url = base_url

    def set_base_url(self, base_url):
        self.base_url = base_url

    def _check_base_url(self):
        if not self.base_url:
            raise ValueError("Base URL is not set. Please call 'set_base_url()' first.")

    def _build_headers(self, method, path, params=None):
        timestamp = str(int(time.time() * 1000))
        full_path = (
            path + "?" + "&".join([f"{k}={v}" for k, v in params.items()])
            if params
            else path
        )
        message = f"{method} {full_path}\n{timestamp}\n{self.access_key}"
        signature = base64.b64encode(
            hmac.new(
                bytes(self.access_secret, "UTF-8"),
                bytes(message, "UTF-8"),
                hashlib.sha256,
            ).digest()
        ).decode("UTF-8")

        return {
            "Content-Type": "application/json; charset=UTF-8",
            "x-ncp-apigw-timestamp": timestamp,
            "x-ncp-iam-access-key": self.access_key,
            "x-ncp-apigw-signature-v2": signature,
            "x-ncp-dmn_cd": "PUB",
        }

    def request(self, method, path, params=None, json=None):
        self._check_base_url()
        url = self.base_url + path
        headers = self._build_headers(method, path, params)
        response = requests.request(
            method, url, headers=headers, params=params, json=json
        )

        logger.debug(f"api send: {headers}")
        logger.debug(f"api send: {url}, {params}")
        logger.debug(f"api send: {response.status_code}")

        try:
            json_data = response.json()
        except Exception:
            json_data = None
        return ResponseData(response.status_code, response.text, json_data)

    async def async_request(self, method, path, session, params=None, json=None):
        self._check_base_url()
        url = self.base_url + path
        headers = self._build_headers(method, path, params)
        async with session.request(
            method, url, headers=headers, params=params, json=json
        ) as response:
            text = await response.text()
            try:
                json_data = await response.json()
            except:
                json_data = None
            return ResponseData(response.status, text, json_data)
