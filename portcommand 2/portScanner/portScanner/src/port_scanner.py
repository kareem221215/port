

import socket
from tqdm import tqdm
from src.Job import Job
from src.ScanResults import ScanResults
from concurrent.futures import ThreadPoolExecutor

open_ports = []  


def scan_port(target, port, protocol, timeout):

    try:
        if protocol == "tcp":
            sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM
            )  # Create a TCP socket
        elif protocol == "udp":
            sock = socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM
            )  # Create a UDP socket
        elif protocol == "http":
            sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM
            )  # Create a TCP socket for HTTP
            sock.sendall(
                b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n"
            )  # Send an HTTP GET request
        else:
            raise ValueError(
                f"Unsupported protocol: {protocol}"
            )  # Raise an error for unsupported protocols

        if timeout:
            sock.settimeout(timeout)  # Set the socket timeout

        result = sock.connect_ex((target, port))  # Connect to the target and port
        if result == 0:
            open_ports.append(port)  # Add the open port to the list
        sock.close()  # Close the socket
    except socket.error as e:
        raise ValueError from e


def scan_ports(job: Job):
    """
    Scan the ports of a target using multiple threads with progress bar
    """
    if job.verbose:
        print(f"Scanning {job.target}...")
    with tqdm(total=job.end_port - job.start_port + 1) as pbar:
        with ThreadPoolExecutor(max_workers=job.threads) as executor:
            futures = [
                executor.submit(scan_port, job.target, port, job.protocol, job.timeout)
                for port in range(job.start_port, job.end_port + 1)
            ]
            for future in futures:
                future.result()
                pbar.update(1)
    if job.verbose:
        print("Scan complete")
    return open_ports


def write_to_file(scan_results: ScanResults):
    """
    Write the scan results to a file
    """
    with open(scan_results.output_file, "w", encoding="utf-8") as file:
        file.write(f"Port Scanner Results on {scan_results.job.target}\n")
        file.write(f"Protocol: {scan_results.job.protocol}\n")
        file.write(
            f"Port Range: {scan_results.job.start_port}-{scan_results.job.end_port}\n"
        )
        file.write(f"Timeout: {scan_results.job.timeout}\n")
        file.write(f"Start Time: {scan_results.start_time}\n")
        file.write(f"End Time: {scan_results.end_time}\n\n")
        for port in scan_results.data:
            file.write(f"Port {port} is open\n")
        file.write(
            f"\nScan completed in {scan_results.end_time - scan_results.start_time} seconds.\n"
        )
        file.write("========================================\n\n")
