"""
=============================================================================
MRZROOT-OS-2: Ultra-Lightweight Terminal Workspace & CLI Automation Engine
=============================================================================
Minimalist Python Engine (Zero external dependencies, pure standard library)
=============================================================================
"""

import os
import platform
import sys
import time
from datetime import datetime


def banner():
    print(r"""
\033[1;36m  __  __ _____ ______ _____   ____   ____ _______        ____   _____        ___  
 |  \/  |  __ \___  /  __ \ / __ \ / __ \__   __|      / __ \ / ____|      |__ \ 
 | \  / | |__) | / /| |__) | |  | | |  | | | | ______ | |  | | (___   ______  ) |
 | |\/| |  _  / / / |  _  /| |  | | |  | | | ||______| | |  | |\___ \ |______|/ / 
 | |  | | | \ \/ /__| | \ \| |__| | |__| | | |        | |__| |____) |        / /_ 
 |_|  |_|_|  \_\_____|_|  \_\\____/ \____/  |_|         \____/|_____/        |____|\033[0m
 \033[1;32m[+] Fast • Minimalist • High-Throughput Automation Engine [v2.4.0]\033[0m
""")


def sys_info():
    print("\n🔍 \033[1;33mSystem Architecture Diagnostics:\033[0m")
    print(f"  • Operating System : {platform.system()} {platform.release()} ({platform.machine()})")
    print(f"  • Python Runtime   : {platform.python_version()} ({platform.python_implementation()})")
    print(f"  • CPU Cores        : {os.cpu_count()}")
    print(f"  • Current Working  : {os.getcwd()}")
    print(f"  • Engine Time      : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def run_benchmark():
    print("\n⚡ \033[1;33mRunning Micro-Benchmark (Compute & Memory)...\033[0m")
    t0 = time.perf_counter()
    # Lightweight compute test
    _ = [x**2 for x in range(200_000)]
    elapsed = (time.perf_counter() - t0) * 1000
    print(f"  ✅ Benchmark Score : Completed in \033[1;32m{elapsed:.2f} ms\033[0m")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    banner()
    sys_info()
    run_benchmark()
    print("\n✨ Ready. Type \033[1;32m'exit'\033[0m or press Enter to continue.")


if __name__ == "__main__":
    main()
