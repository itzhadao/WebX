import platform
import os

def detect_os():
    system = platform.system().lower()
    distro_info = {}
    machine = platform.machine().lower()

    if system == "windows":
        return "Windows", platform.version()

    elif system == "darwin":
        return "macOS", platform.mac_ver()[0]

    elif system == "linux":
        if os.path.exists("/etc/os-release"):
            with open("/etc/os-release") as f:
                for line in f:
                    line = line.strip()
                    if "=" in line:
                        key, val = line.split("=", 1)
                        val = val.strip().strip("\"'")
                        distro_info[key] = val.lower()

        if "ubuntu" in distro_info.get("name", "") or "ubuntu" in distro_info.get("id", ""):
            return "Ubuntu (Linux)", distro_info.get("version_id", "")

        if "chrome os" in distro_info.get("name", "") or "chromium os" in distro_info.get("name", ""):
            return "Chrome OS (Linux)", distro_info.get("version_id", "")

        try:
            with open("/proc/cpuinfo") as f:
                cpuinfo = f.read().lower()
                if "raspberry pi" in cpuinfo:
                    return "Raspberry Pi OS (Linux)", ""
        except FileNotFoundError:
            pass

        return "Linux", platform.release()

    else:
        return f"Unknown OS ({system})", ""


def clear():
    """Xóa toàn bộ nội dung console, tự phát hiện OS bằng detect_os()."""
    os_name, _ = detect_os()

    if "windows" in os_name.lower():
        os.system("cls")
    else:
        os.system("clear")
