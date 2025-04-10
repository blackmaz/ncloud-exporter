import logging

logger = logging.getLogger(__name__)


class RedisService:

    def __init__(self, api_client, base_url):
        self.api_client = api_client
        self.base_url = base_url

    def get_cloud_redis_instance_list(self, region_code="KR", vpc_no=None):
        req_path = "/vredis/v2/getCloudRedisInstanceList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        if vpc_no:
            params["vpcNo"] = vpc_no
        return self.api_client.get(self.base_url, req_path, params=params)
