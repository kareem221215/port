

import argparse
import re
import time
from src.port_scanner import scan_ports, write_to_file
from src.Job import Job
from src.ScanResults import ScanResults

protocols = ["tcp", "udp", "http"]
min_port = 1
max_port = 65535
default_timeout = 1
threads = 10




def main():
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument(
        "--target",
        help="The target URL or IP to scan",
        metavar="target",
        required=True,
    )

    parser.add_argument(
        "--range",
        help="The range of ports to scan in the format start_port-end_port",
        required=False,
        metavar="start_port-end_port",
        default=f"{min_port}-{max_port}",
    )

    parser.add_argument(
        "--threads",
        help="The number of threads to use for the scan",
        required=False,
        metavar="threads",
        type=int,
        default=threads,
    )

    parser.add_argument(
        "--timeout",
        help="The timeout for the scan in seconds",
        required=False,
        metavar="timeout",
        type=int,
        default=default_timeout,
    )

    parser.add_argument(
        "--protocol",
        help="The protocol to use for the scan. Options are tcp, udp, http",
        required=False,
        metavar="protocol",
        default="tcp",
    )

    parser.add_argument(
        "--output_file",
        help="The path of the file to write the results to",
        required=False,
        metavar="file path",
        default=None,
    )

    parser.add_argument(
        "--verbose",
        help="Print the results to the console",
        required=False,
        action='store_true',
    )

    args = parser.parse_args()

    if not re.match(r"\d+-\d+", args.range):
        raise ValueError("Invalid port range")

    start_port, end_port = args.range.split("-")

    if not start_port.isdigit() or not end_port.isdigit():
        raise ValueError("Invalid port range")

    if int(start_port) < min_port or int(end_port) > max_port:
        raise ValueError(f"Port range must be between {min_port} and {max_port}")

    if int(start_port) > int(end_port):
        raise ValueError(
            f"Start port - {start_port}, must be less than or equal to end port - {end_port}"
        )

    if args.protocol not in protocols:
        raise ValueError(f"Protocol must be one of: {', '.join(protocols)}")

    if args.output_file is None:
        args.output_file = f"port_scan_results_{args.target}.txt"

    args.start_port = int(start_port)
    args.end_port = int(end_port)
    args.timeout = int(args.timeout)
    args.protocols = args.protocol

    if args.threads < 1:
        raise ValueError("Threads must be a positive integer")
    args.threads = int(args.threads)

    job = Job(
        args.target,
        args.start_port,
        args.end_port,
        args.threads,
        args.timeout,
        args.protocols,
        args.verbose,
    )

    start_time = time.time()
    open_ports = scan_ports(job=job)
    end_time = time.time()

    if job.verbose:
        print(f"Scan complete in {end_time - start_time} seconds")
        print(f"Open ports: {open_ports}")

    scan_results = ScanResults(
        data=open_ports,
        output_file=args.output_file,
        job=job,
        start_time=start_time,
        end_time=end_time,
    )

    write_to_file(scan_results=scan_results)


if __name__ == "__main__":
    main()
