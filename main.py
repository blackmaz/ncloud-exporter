import asyncio
import logging
from flask import Flask, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from config.config_loader import config
from exporter.metric_exporter import MetricExporter
from exporter.metric_processor import MetricProcessor
from ncloud.base_collector import BaseCollector
from common import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

app = Flask(__name__)
exporters = []


@app.route("/")
def home():
    return "<h1>NCloud Cloud Insight Exporter</h1>"


@app.route("/health")
def health():
    return {"status": "healthy"}


@app.route("/metrics")
async def metrics_endpoint():
    tasks = [exporter.fetch_metrics() for exporter in exporters]
    await asyncio.gather(*tasks)
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


async def initialize_exporters():
    for product in config.product_names:
        collector = BaseCollector(config.account_name, product)
        processor = MetricProcessor()
        exporter = MetricExporter(collector, processor)
        exporters.append(exporter)


if __name__ == "__main__":
    """
    --account_name huniverse \
    --product_name Server Redis \
    --access_key ncp_iam_* \
    --secret_key ncp_iam_**
    """
    asyncio.run(initialize_exporters())
    app.run(host="0.0.0.0", port=9000)
