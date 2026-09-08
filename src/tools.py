import platform
import socket
import subprocess


def get_system_info():
    """Return basic information about the computer."""

    return {
        "operating_system": platform.system(),
        "operating_system_version": platform.version(),
        "computer_name": socket.gethostname(),
    }


def check_internet_connection():
    """Check whether the computer can reach the internet."""

    try:
        result = subprocess.run(
            ["ping", "-n", "1", "8.8.8.8"],
            capture_output=True,
            text=True,
            timeout=5,
        )

        if result.returncode == 0:
            return "Internet connectivity check: SUCCESS"

        return "Internet connectivity check: FAILED"

    except subprocess.TimeoutExpired:
        return "Internet connectivity check: TIMEOUT"

    except Exception as error:
        return f"Internet connectivity check failed: {error}"


def get_network_information():
    """Return basic network configuration."""

    try:
        result = subprocess.run(
            ["ipconfig"],
            capture_output=True,
            text=True,
            timeout=5,
        )

        return result.stdout

    except Exception as error:
        return f"Could not retrieve network information: {error}"


if __name__ == "__main__":
    print("System Information:")
    print(get_system_info())

    print("\nInternet Check:")
    print(check_internet_connection())

    print("\nNetwork Information:")
    print(get_network_information())
