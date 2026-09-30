#!/usr/bin/env python3
"""Ping monitor: alert kalau host down N kali berturut."""
import subprocess, time, sys
host = sys.argv[1] if len(sys.argv) > 1 else "1.1.1.1"
fail = 0
while True:
      r = subprocess.run(["ping", "-c", "1", "-W", "2", host], capture_output=True)
      ok = r.returncode == 0
      fail = 0 if ok else fail + 1
      print(f"{time.strftime('%H:%M:%S')} {'UP' if ok else f'DOWN x{fail}'}")
      if fail >= 3: print("ALERT: host down 3x berturut!")
            time.sleep(30)
