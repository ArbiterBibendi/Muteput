import sys
import subprocess

indexes = subprocess.check_output("pactl list sink-inputs | grep 'Sink Input'", shell=True)
bins = subprocess.check_output("pactl list sink-inputs | grep binary", shell=True)

indexStr = indexes.decode()
binStr = bins.decode()

indexStr = indexStr.replace("Sink Input #", "").lower()
binStr = binStr.replace("\t\tapplication.process.binary = ", "").lower()
binStr = binStr.replace("\"", "")

indexes = indexStr.split()
bins = binStr.split()

i = 0
param = sys.argv[1].lower()
for binary in bins:
    if binary == param:
        break
    i = i + 1

sinkinput = indexes[i]

subprocess.run("pactl set-sink-input-mute " + sinkinput + " toggle", shell=True)
