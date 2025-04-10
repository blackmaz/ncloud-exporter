import logging

logger = logging.getLogger(__name__)


class ServerService:
    def __init__(self, api_client, base_url):
        self.api_client = api_client
        self.base_url = base_url

    def get_server_instance_list(self, region_code="KR", vpc_no=None):
        req_path = "/vserver/v2/getServerInstanceList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        if vpc_no:
            params["vpcNo"] = vpc_no
        return self.api_client.get(self.base_url, req_path, params=params)

    def get_server_image_list(self, region_code="KR", vpc_no=None):
        req_path = "/vserver/v2/getServerImageList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        if vpc_no:
            params["vpcNo"] = vpc_no
        return self.api_client.get(self.base_url, req_path, params=params)

    def get_block_storage_instance_list(self, region_code="KR", vpc_no=None):
        req_path = "/vserver/v2/getBlockStorageInstanceList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        if vpc_no:
            params["vpcNo"] = vpc_no
        return self.api_client.get(self.base_url, req_path, params=params)

    def get_block_storage_snapshot_instance_list(self, region_code="KR", vpc_no=None):
        req_path = "/vserver/v2/getBlockStorageSnapshotInstanceList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        if vpc_no:
            params["vpcNo"] = vpc_no
        return self.api_client.get(self.base_url, req_path, params=params)

    def get_public_ip_instance_list(self, region_code="KR", vpc_no=None):
        req_path = "/vserver/v2/getPublicIpInstanceList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        if vpc_no:
            params["vpcNo"] = vpc_no
        return self.api_client.get(self.base_url, req_path, params=params)

    def get_access_control_group_instance_list(self, region_code="KR", vpc_no=None):
        req_path = "/vserver/v2/getAccessControlGroupInstanceList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        if vpc_no:
            params["vpcNo"] = vpc_no
        return self.api_client.get(self.base_url, req_path, params=params)
