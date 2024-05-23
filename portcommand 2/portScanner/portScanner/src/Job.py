class Job:
    def __init__(
        self, target, start_port, end_port, threads, timeout, protocol, verbose=False
    ):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.threads = threads
        self.timeout = timeout
        self.protocol = protocol
        self.results = None
        self.verbose = verbose

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        if not isinstance(value, str):
            raise ValueError("Target must be a string")
        self._target = value

    @property
    def start_port(self):
        return self._start_port

    @start_port.setter
    def start_port(self, value):
        if not isinstance(value, int):
            raise ValueError("Start port must be an integer")
        self._start_port = value

    @property
    def end_port(self):
        return self._end_port

    @end_port.setter
    def end_port(self, value):
        if not isinstance(value, int):
            raise ValueError("End port must be an integer")
        self._end_port = value

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Timeout must be an integer or float")
        self._timeout = value

    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        if value not in ["tcp", "udp", "http"]:
            raise ValueError("Protocol must be one of: tcp, udp or http")
        self._protocol = value

    @property
    def results(self):
        return self._results

    @results.setter
    def results(self, value):
        if value is not None and not isinstance(value, list):
            raise ValueError("Results must be a list")
        self._results = value

    @property
    def verbose(self):
        return self._verbose

    @verbose.setter
    def verbose(self, value):
        if not isinstance(value, bool):
            raise ValueError("Verbose must be a boolean")
        self._verbose = value

    @property
    def threads(self):
        return self._threads

    @threads.setter
    def threads(self, value):
        if not isinstance(value, int):
            raise ValueError("Threads must be an integer")
        self._threads = value
