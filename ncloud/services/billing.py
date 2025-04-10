import logging

logger = logging.getLogger(__name__)


class BillingService:
    def __init__(self, api_client, base_url):
        self.api_client = api_client
        self.base_url = base_url

    def get_contract_summary(self, region_code="KR"):
        req_path = "/billing/v1/cost/getContractSummaryList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        params["contractMonth"] = "202411"
        return self.api_client.get(self.base_url, req_path, params=params)

    def get_contract_usage_list(
        self, region_code="KR", start_ym="202412", end_ym="202412"
    ):
        req_path = "/billing/v1/cost/getContractUsageList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        params["startMonth"] = start_ym
        params["endMonth"] = end_ym
        return self.api_client.get(self.base_url, req_path, params=params)

    def get_contract_demand_cost_list(
        self, region_code="KR", start_ym="202412", end_ym="202412"
    ):
        req_path = "/billing/v1/cost/getContractDemandCostList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        params["startMonth"] = start_ym
        params["endMonth"] = end_ym
        return self.api_client.get(self.base_url, req_path, params=params)

    def get_demand_cost_list(
        self, region_code="KR", start_ym="202412", end_ym="202412"
    ):
        req_path = "/billing/v1/cost/getDemandCostList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        params["startMonth"] = start_ym
        params["endMonth"] = end_ym
        return self.api_client.get(self.base_url, req_path, params=params)

    def get_contract_product_cost_list(
        self, region_code="KR", start_ym="202412", end_ym="202412"
    ):
        req_path = "/billing/v1/cost/getProductDemandCostList"
        params = {"responseFormatType": "json", "regionCode": region_code}
        params["startMonth"] = start_ym
        params["endMonth"] = end_ym

        return self.api_client.get(self.base_url, req_path, params=params)
