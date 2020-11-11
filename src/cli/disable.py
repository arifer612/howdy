# Set the disable flag

# Import required modules
import sys
import os
import builtins
import fileinput
import configparser
import datetime

# Get the absolute filepath
config_path = os.path.dirname(os.path.abspath(__file__)) + "/../config.ini"

# Read config from disk
config = configparser.ConfigParser()
config.read(config_path)

# Check if enough arguments have been passed
if builtins.howdy_args.argument is None:
	print("Please add a 0 (enable) or a 1 (disable) as an argument")
	sys.exit(1)

# Translate the argument to the right string
if builtins.howdy_args.argument == "1" or builtins.howdy_args.argument.lower() == "true":
	out_value = "true"
elif builtins.howdy_args.argument == "0" or builtins.howdy_args.argument.lower() == "false":
	out_value = "false"
else:
    try:
        # Checks if the argument is a valid time frame
        start, end = [datetime.datetime.strptime(time.strip(), "%H:%M") for time in builtins.howdy_args.argument.split('-')]
        datetime.datetime.strftime
    except Exception:
        # If it's not a boolean or time period, it's invalid
        print("Please only use false (enable), true (disable), or a time frame (disable during HH:MM-HH:MM) as an argument")
        sys.exit(1)
    else:
        out_value = " - ".join(f"{datetime.datetime.strftime(time, '%H:%M')}" for time in (start, end))

# Don't do anything when the state is already the requested one
if out_value == config.get("core", "disabled"):
	print("The disable option has already been set to " + out_value)
	sys.exit(1)

# Loop though the config file and only replace the line containing the disable config
for line in fileinput.input([config_path], inplace=1):
	print(line.replace("disabled = " + config.get("core", "disabled"), "disabled = " + out_value), end="")

# Print what we just did
if out_value == 'true':
	print("Howdy has been disabled")
elif out_value == 'false':
	print("Howdy has been enabled")
else:
    print(f"Howdy has been set to be disabled during {out_value}")
