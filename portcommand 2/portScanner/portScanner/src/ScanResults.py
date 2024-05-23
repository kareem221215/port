from src.Job import Job


class ScanResults:
    def __init__(
        self,
        data,
        output_file,
        job: Job,
        start_time,
        end_time,
    ):
        self.data = data
        self.output_file = output_file
        self.job = job
        self.start_time = start_time
        self.end_time = end_time

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, list):
            raise ValueError("Data must be a list")
        self._data = value

    @property
    def output_file(self):
        return self._output_file

    @output_file.setter
    def output_file(self, value):
        if not isinstance(value, str):
            raise ValueError("Output file must be a string")
        self._output_file = value

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Start time must be an integer or float")
        self._start_time = value

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("End time must be an integer or float")
        self._end_time = value

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if not isinstance(value, Job):
            raise ValueError("Job must be a Job object")
        self._job = value
