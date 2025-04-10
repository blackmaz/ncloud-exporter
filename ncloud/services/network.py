import logging

logger = logging.getLogger(__name__)


class NetworkService:

    def __init__(self, api_client, base_url):
        self.api_client = api_client
        self.base_url = base_url

    def get_region_list(self):
        req_path = "/vserver/v2/getRegionList"
        params = {"responseFormatType": "json"}
        return self.api_client.get(self.base_url, req_path, params=params)

    def get_zone_list(self, region_code="KR"):
        req_path = "/vserver/v2/getZoneList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        return self.api_client.get(self.base_url, req_path, params=params)

    def get_vpc_list(self, region_code="KR"):
        req_path = "/vpc/v2/getVpcList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        return self.api_client.get(self.base_url, req_path, params=params)

    def get_subnet_list(self, region_code="KR", vpc_no=None):
        req_path = "/vpc/v2/getSubnetList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        if vpc_no:
            params["vpcNo"] = vpc_no
        return self.api_client.get(self.base_url, req_path, params=params)

    def get_natgw_list(self, region_code="KR", vpc_no=None):
        req_path = "/vpc/v2/getNatGatewayInstanceList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        if vpc_no:
            params["vpcNo"] = vpc_no
        return self.api_client.get(self.base_url, req_path, params=params)

    def get_peering_list(self, region_code="KR", vpc_no=None):
        req_path = "/vpc/v2/getVpcPeeringInstanceList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        if vpc_no:
            params["vpcNo"] = vpc_no
        return self.api_client.get(self.base_url, req_path, params=params)

    def get_routetable_list(self, region_code="KR", vpc_no=None):
        req_path = "/vpc/v2/getRouteTableList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        if vpc_no:
            params["vpcNo"] = vpc_no
        return self.api_client.get(self.base_url, req_path, params=params)
