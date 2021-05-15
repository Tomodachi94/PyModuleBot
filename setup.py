# PyPIDataBot by Tomodachi94
# (c) 2021 Tomodachi94, under the MIT License
# The license should have been distributed with this program.
# If not, the license can be found here:
# mit-license.org

# Not your average setup.py

import sys, os

arg = sys.argv[1]

def help():
    print(initializeConfig.__doc__())

def initializeConfig():
    print("Initializing config...")
    os.system(f"cp {os.cwd}/pypidatabot/defaults/config-default.toml")
    os.system(f"cp {os.cwd}/pypidatabot/defaults/cred-default.toml")

def installDependancies():
