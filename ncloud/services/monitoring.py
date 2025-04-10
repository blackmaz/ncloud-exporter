from common import conv_date_time
from config.config_loader import config
import logging

logger = logging.getLogger(__name__)


class MonitoringService:
    def __init__(self, api_client, base_url):
        self.api_client = api_client
        self.base_url = base_url

    def get_system_schema_key_list(self):
        req_path = "/cw_fea/real/cw/api/schema/system/list"
        return self.api_client.get(self.base_url, req_path)

    def query_data(
        self,
        product_name,
        dimensions,
        metric_name,
        aggregation,
        start_datetime,
        end_datetime,
    ):
        req_path = "/cw_fea/real/cw/api/data/query"

        json_data = {
            "timeStart": conv_date_time(start_datetime),
            "timeEnd": conv_date_time(end_datetime),
            "cw_key": config.resource_types[product_name]["key"],
            "metric": metric_name,
            "interval": "Min1",
            "aggregation": aggregation,
            "dimensions": dimensions,
        }

        logger.debug(json_data)
        return self.api_client.post(self.base_url, req_path, json=json_data)

    async def query_data_async(
        self,
        product_name,
        dimensions,
        metric_name,
        aggregation,
        start_datetime,
        end_datetime,
        session,
    ):

        req_path = "/cw_fea/real/cw/api/data/query"

        json_data = {
            "timeStart": conv_date_time(start_datetime),
            "timeEnd": conv_date_time(end_datetime),
            "cw_key": config.resource_types[product_name]["key"],
            "metric": metric_name,
            "interval": "Min1",
            "aggregation": aggregation,
            "dimensions": dimensions,
        }

        logger.debug(json_data)
        return await self.api_client.post_async(
            self.base_url, req_path, session, json=json_data
        )

    def query_data_multiple(
        self,
        product_name,
        dimensions,
        metric_name_list,
        aggregation,
        start_datetime,
        end_datetime,
    ):
        req_path = "/cw_fea/real/cw/api/data/query/multiple"

        metric_info_list = []
        for metric_name in metric_name_list:
            metric_info_list.append(
                {
                    "aggregation": aggregation,
                    "dimensions": dimensions,
                    "interval": "Min1",
                    "metric": metric_name,
                    "prodKey": config.resource_types[product_name]["key"],
                }
            )
        json_data = {
            "metricInfoList": metric_info_list,
            "timeStart": conv_date_time(start_datetime),
            "timeEnd": conv_date_time(end_datetime),
        }
        return self.api_client.post(self.base_url, req_path, json=json_data)

    async def query_data_multiple_async(
        self,
        product_name,
        dimensions,
        metric_name_list,
        aggregation,
        start_datetime,
        end_datetime,
        session,
    ):
        req_path = "/cw_fea/real/cw/api/data/query/multiple"

        metric_info_list = []
        for metric_name in metric_name_list:
            metric_info_list.append(
                {
                    "aggregation": aggregation,
                    "dimensions": dimensions,
                    "interval": "Min1",
                    "metric": metric_name,
                    "prodKey": config.resource_types[product_name]["key"],
                }
            )
        json_data = {
            "metricInfoList": metric_info_list,
            "timeStart": conv_date_time(start_datetime),
            "timeEnd": conv_date_time(end_datetime),
        }
        return await self.api_client.post_async(
            self.base_url, req_path, session, json=json_data
        )
