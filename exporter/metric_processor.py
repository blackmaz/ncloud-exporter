from prometheus_client import Gauge


class MetricProcessor:
    def __init__(self):
        self.metrics = {}

    def get_or_create_gauge(self, metric_key, metric_name):
        if metric_key not in self.metrics:
            self.metrics[metric_key] = Gauge(
                metric_key,
                f"{metric_name} from Ncloud",
                ["account_name", "product_name", "resource_id", "resource_name"],
            )
        return self.metrics[metric_key]

    def process_metric_data(self, metric):

        if not metric["dps"]:
            return
        metric_name = metric["metric_name"]
        metric_key = f"ncloud_{metric_name.replace('.', '_')}"
        latest_value = metric["dps"][-1][1]
        gauge = self.get_or_create_gauge(metric_key, metric["metric_name"])
        gauge.labels(
            account_name=metric["account_name"],
            product_name=metric["product_name"],
            resource_id=metric["resource_id"],
            resource_name=metric["resource_name"],
        ).set(latest_value)
