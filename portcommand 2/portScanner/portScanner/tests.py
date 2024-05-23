

import os
from src.port_scanner import scan_ports, write_to_file
from src.Job import Job
from src.ScanResults import ScanResults


def test_scan_ports():
    job = Job("localhost", 80, 80, 10, 1, "tcp", True)

    result = scan_ports(job=job)
    assert isinstance(result, list)
    if result:
        port, protocol = result[0]
        assert port == 80
        assert protocol == "tcp"


def test_write_to_file():

    scan_results = ScanResults(
        data=[80],
        output_file="test_output.txt",
        job=Job("localhost", 80, 80, 10, 1, "tcp", True),
        start_time=0,
        end_time=1,
    )

    write_to_file(scan_results=scan_results)
    assert os.path.exists(output_file)
    with open(output_file, "r", encoding="utf-8") as file:
        content = file.read()
        assert "Port Scanner Results on localhost" in content


def cleanup(file):
    if os.path.exists(file):
        os.remove(file)


output_file = "test_output.txt"
test_scan_ports()
test_write_to_file()
cleanup(output_file)
