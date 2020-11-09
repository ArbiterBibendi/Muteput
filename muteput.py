import sys
import subprocess


if sys.argv[1] == "-h":
    print("python3 mute (in|out) [application]\n")
if sys.argv[1] == "out":
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
    param = sys.argv[2].lower()
    for binary in bins:
        if binary == param:
            break
        i = i + 1

    sinkinput = indexes[i]

    subprocess.run("pactl set-sink-input-mute " + sinkinput + " toggle", shell=True)
if sys.argv[1] == "in":
    indexes = subprocess.check_output("pactl list source-outputs | grep 'Source Output'", shell=True)
    bins = subprocess.check_output("pactl list source-outputs | grep binary", shell=True)

    indexStr = indexes.decode()
    binStr = bins.decode()

    indexStr = indexStr.replace("Source Output #", "").lower()
    binStr = binStr.replace("\t\tapplication.process.binary = ", "").lower()
    binStr = binStr.replace("\"", "")

    indexes = indexStr.split()
    bins = binStr.split()

    i = 0
    param = sys.argv[2].lower()
    for binary in bins:
        if binary == param:
            break
        i = i + 1

    sourceoutput = indexes[i]

    subprocess.run("pactl set-source-output-mute " + sourceoutput + " toggle", shell=True)

