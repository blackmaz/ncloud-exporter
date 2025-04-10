import logging

logger = logging.getLogger(__name__)


class NasService:

    def __init__(self, api_client, base_url):
        self.api_client = api_client
        self.base_url = base_url

    def get_nas_volume_instance_list(self, region_code="KR", vpc_no=None):
        req_path = "/vnas/v2/getNasVolumeInstanceList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        if vpc_no:
            params["vpcNo"] = vpc_no
        return self.api_client.get(self.base_url, req_path, params=params)
