import random
import subprocess
import time

layouts = [
    "fr",
    "us",
    "de",
    "es",
    "it",
    "fa",
    "ar",
    "de",
    "at",
    "es",
    "pt",
    "br",
    "it",
    "nl",
    "dk",
    "no",
    "se",
    "fi",
    "is",
    "pl",
    "cz",
    "sk",
    "hu",
    "ro",
    "bg",
    "hr",
    "si",
    "rs",
    "ba",
    "mk",
    "al",
    "gr",
    "tr",
    "ru",
    "ua",
    "by",
    "ge",
    "am",
    "il",
    "ar",
    "ir",
    "in",
    "jp",
    "kr",
    "cn",
    "tw",
    "vn",
    "th",
]

try:
    x = 0
    while True:
        layout = random.choice(layouts)
        subprocess.run(["setxkbmap", layout])
        time.sleep(10)
        x += 1
        if x >= 30:
            subprocess.run(["setxkbmap", "us"])
            exit(0)
except (KeyboardInterrupt, SystemExit, Exception):
    subprocess.run(["setxkbmap", "us"])
