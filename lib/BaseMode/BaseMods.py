from lib.BaseMode.BaseOptions import BaseOption
from lib.BaseMode.BaseOptions import BaseOptions
from lib.BaseMode.BaseResult import BaseResult


class BaseExploit:
    name = None
    description = None
    author = []
    references = []
    disclosure_date = None
    service_name = None
    service_version = None
    info_fields = ['name', 'description', 'author', 'references', 'disclosure_date', 'service_name', 'service_version']
    multi_target = False
    targets = []
    target_type = None
    options = None
    results = None

    def __init__(self):
        self.multi_target = False
        self.target_type = None
        self.targets = []
        self.options = BaseOptions()
        self.results = BaseResult()

    def get_info(self):
        info = {}
        for field_name in self.info_fields:
            info[field_name] = getattr(self, field_name)
        return info

    def register_tcp_target(self, port_value=None, timeout_value=5, threads_value=1):
        self.target_type = "tcp"
        self.register_options([
            BaseOption(name="HOST", required=True, description="The IP address to be tested"),
            BaseOption(name="PORT", required=True, description="The port to be tested", value=port_value),
            BaseOption(name="TIMEOUT", required=True, description="Connection timeout", value=timeout_value),
            BaseOption(name="THREADS", required=True, description="The number of threads", value=threads_value)
        ])

    def register_http_target(self, timeout_value=5, threads_value=1):
        self.target_type = "http"
        self.register_options([
            BaseOption(name="URL", required=True, description="The url to be tested"),
            BaseOption(name="TIMEOUT", required=True, description="Connection timeout", value=timeout_value),
            BaseOption(name="THREADS", required=True, description="The number of threads", value=threads_value)
        ])

    def update_info(self, info):
        for name in info:
            if name in self.info_fields:
                setattr(self, name, info[name])

    def register_options(self, option_array):
        for option in option_array:
            self.options.add_option(option)

    def get_missing_options(self):
        def is_missing(option):
            return option.required and option.value in [None, '']

        missing_options = filter(is_missing, self.options.get_options())
        return list(missing_options)
