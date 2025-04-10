import logging

logger = logging.getLogger(__name__)


class LoadBalancerService:
    def __init__(self, api_client, base_url):
        self.api_client = api_client
        self.base_url = base_url

    def get_load_balancer_instance_list(self, region_code="KR", vpc_no=None):
        req_path = "/vloadbalancer/v2/getLoadBalancerInstanceList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        if vpc_no:
            params["vpcNo"] = vpc_no
        return self.api_client.get(self.base_url, req_path, params=params)

    def get_targetgroup_list(self, region_code="KR", vpc_no=None):
        req_path = "/vloadbalancer/v2/getTargetGroupList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        if vpc_no:
            params["vpcNo"] = vpc_no
        return self.api_client.get(self.base_url, req_path, params=params)
