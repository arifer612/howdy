# Open the config file in an editor

# Import required modules
import os
import subprocess
import shlex

# Let the user know what we're doing
print("Opening config.ini in the default editor")

# Default to the nano editor
editor = ["/bin/nano"]

# Use the user preferred editor if available
user = os.getenv("SUDO_USER")
if user:
	user_editor = subprocess.run(["su", "-", user, "-c", "source ~/.profile; echo $EDITOR"], stdout=subprocess.PIPE).stdout.decode().strip('\n')

if user_editor:
	editor = shlex.split(user_editor) # To split $EDITOR if the user specified a string command as an alias
elif os.path.isfile("/etc/alternatives/editor"):
	editor = ["/etc/alternatives/editor"]

# Open the editor as a subprocess and fork it
subprocess.call([*editor, os.path.dirname(os.path.realpath(__file__)) + "/../config.ini"])
