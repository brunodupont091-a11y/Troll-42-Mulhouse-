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
    while True:
        layout = random.choice(layouts)
        subprocess.run(["setxkbmap", layout])
        print(f"Keyboard layout changed to: {layout}")
        time.sleep(10)
except (KeyboardInterrupt, SystemExit):
    subprocess.run(["setxkbmap", "us"])
