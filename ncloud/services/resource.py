import logging

logger = logging.getLogger(__name__)


class ResourceService:
    def __init__(self, api_client, base_url):
        self.api_client = api_client
        self.base_url = base_url

    def get_resource_list(self, region_code="KR"):
        req_path = "/api/v1/resources"

        json_data = {
            "regionCode": region_code,
            "resourceType": "Storage",
            "pageSize": 100,
        }

        return self.api_client.post(
            self.base_url,
            req_path,
            json=json_data,
        )

    def get_resource_group_list(self):
        req_path = "/api/v1/groups"

        params = {"responseFormatType": "json"}

        return self.api_client.get(self.base_url, req_path, params=params)
