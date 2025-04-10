class MetricExporter:

    def __init__(self, collector, processor):
        self.collector = collector
        self.processor = processor

    async def fetch_metrics(self):
        metrics = await self.collector.collect()
        for metric in metrics:
            self.processor.process_metric_data(metric)
