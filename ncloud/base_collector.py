import aiohttp
import asyncio
from common import current_time, current_time_n_min_ago
from config.config_loader import config
from ncloud.resource_manager import ResourceManager
from ncloud.api_client import ApiClient
from ncloud.services.monitoring import MonitoringService


class BaseCollector:

    def __init__(self, account_name, product_name):
        self.account_name = account_name
        self.product_name = product_name
        self.api_client = ApiClient(config.access_key, config.secret_key)
        self.resource_manager = ResourceManager(self.product_name, self.api_client)
        self.metrics = self.resource_manager.get_metrics()
        self.resources = self.resource_manager.get_resources()
        self.service = MonitoringService(self.api_client, config.api_urls.ci)

    async def collect(self):
        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(limit=5)
        ) as session:
            tasks = [
                self._fetch_metric_data(session, resource)
                for resource in self.resources
            ]
            results = await asyncio.gather(*tasks)
            return [metric for batch in results for metric in batch]

    async def _fetch_metric_data(self, session, resource):
        start_datetime, end_datetime = current_time_n_min_ago(5), current_time()
        dimensions = {"instanceNo": resource["id"]}
        metrics_json = await self._query_metrics_with_retry(
            session, dimensions, start_datetime, end_datetime
        )

        if not metrics_json:
            return []

        return [self._format_metric(resource, item) for item in metrics_json]

    async def _query_metrics_with_retry(
        self, session, dimensions, start_datetime, end_datetime
    ):
        aggregation = "MAX"
        for attempt in range(config.max_retry):
            response = await self.service.query_data_multiple_async(
                self.product_name,
                dimensions,
                self.metrics,
                aggregation,
                start_datetime,
                end_datetime,
                session,
            )

            if response.status == 200 and response.json:
                return response.json
            if response.status == 429:
                await asyncio.sleep(2**attempt)
            else:
                break

    def _format_metric(self, resource, item):
        return {
            "metric_name": item["metric"],
            "account_name": self.account_name,
            "product_name": self.product_name,
            "resource_id": resource["id"],
            "resource_name": resource["name"],
            "dps": item["dps"],
        }
