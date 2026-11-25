import os

ENTRY = "I can turn invisible — but only in photographs, and only when someone actually wants me in the picture."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY + "\n")
