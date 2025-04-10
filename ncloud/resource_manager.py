import json
import pandas as pd
from common import get_method_from_config
from config.config_loader import config


class ResourceManager:
    def __init__(self, product_name, api_client):
        self.product_name = product_name
        self.api_client = api_client

    def get_metrics(self):
        return config.resource_types[self.product_name]["metric_list"]

    def get_resources(self):
        resource_info = config.resource_types[self.product_name]

        api_method = get_method_from_config(
            resource_info["service"],
            resource_info["method"],
            self.api_client,
            config.api_urls.api,
        )

        api_result = api_method()
        api_json = json.loads(api_result.text)

        for key in resource_info["json_key"].split("."):
            api_json = api_json.get(key, {})
        df = pd.json_normalize(api_json)

        resources = []

        for _, row in df.iterrows():
            if "sub_instance_list" in resource_info.keys():
                for sub_resource in row[resource_info["sub_instance_list"]]:
                    resources.append(
                        {
                            "name": sub_resource[resource_info["sub_name_key"]],
                            "id": sub_resource[resource_info["sub_id_key"]],
                        }
                    )
            else:
                resources.append(
                    {
                        "name": row[resource_info["name_key"]],
                        "id": row[resource_info["id_key"]],
                    }
                )
        return resources
