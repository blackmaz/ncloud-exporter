import logging
import time
import datetime
import importlib
from config.config_loader import config


def setup_logging():
    logger = logging.getLogger()

    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s : %(message)s")
    stream_handler.setFormatter(formatter)

    logger.setLevel(level=config.log_level)
    if not logger.handlers:
        logger.addHandler(stream_handler)


def logger_decorator(func):

    logger = logging.getLogger("common")

    def decorated(*args, **kwargs):
        start = time.time()
        time.strftime("%Y%m%d-%H%M%S", time.localtime(start))
        logger.debug(
            f"{func.__name__} start time: {time.strftime('%Y%m%d-%H%M%S', time.localtime(start))}"
        )

        result = func(*args, **kwargs)

        end = time.time()
        logger.debug(
            f"{func.__name__} end time: {time.strftime('%Y%m%d-%H%M%S', time.localtime(end))}"
        )
        logger.debug(
            f"{func.__name__} elapsed time: {datetime.timedelta(seconds=(end-start))}"
        )

        return result

    return decorated


def conv_date_time(srt_date_time):
    res_date_time = datetime.datetime.strptime(srt_date_time, "%Y-%m-%d %H:%M:%S")
    return str(int(res_date_time.timestamp()) * 1000)


def get_object_by_name(module_class_path):
    module_name, class_name = module_class_path.rsplit(".", 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)


def get_method_from_config(service_path, method_name, *args, **kwargs):
    module_name, class_name = service_path.rsplit(".", 1)
    module = importlib.import_module(module_name)
    service_class = getattr(module, class_name)
    instance = service_class(*args, **kwargs)
    return getattr(instance, method_name)


def current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def current_time_n_min_ago(n=5):
    return (datetime.datetime.now() - datetime.timedelta(minutes=n)).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
