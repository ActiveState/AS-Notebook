from ast import Str
from base64 import decode
from genericpath import exists
from importlib.metadata import metadata
import os
import json
import shutil
import subprocess
import helper
from sys import platform


# Static path info---------------------------
if platform == "linux" or platform == "linux2":  # linux
    pathToRuntimes = os.path.expanduser('~/.cache/activestate')
    pathToJupyter = os.path.expanduser('~/.local/share/jupyter/kernels')
elif platform == "darwin":    # OS X
    pathToRuntimes = os.path.expanduser('~/Library/Caches/ActiveState')
    pathToJupyter = os.path.expanduser('~/Library/Jupyter/kernels')


# Get jupyter metadata teamplate for install
with open('template.json') as file:
    metaTemplate = json.load(file)


# return a hash tables of ActiveState runtimes containg IPython that have been checked out locally
# Key = cache id, value = project name
def getCachedRuntimes():

    results = {}

    # Call project and convert to list of dictonaries
    commandOut = subprocess.run(
        ['state', 'projects', '--output', 'json'], stdout=subprocess.PIPE, env=os.environ)
    # decoding process returns to characters of garabafe
    stringOut = commandOut.stdout.decode()[:-2]
    projects = json.loads(stringOut)

    # itterate through list of projects
    for project in projects:
        checkouts = project.get("local_checkouts")
        for checkout in checkouts:
            folderHash = helper.getCachedRuntimeHash(checkout)
            # is cached and has ipython
            if os.path.exists(pathToRuntimes+'/'+folderHash+'/usr/bin/ipython'):
                name = project.get("organization")+"/"+project.get("name")

                # Runtime checked out in multiple locations (could all be diffrent)
                if len(checkouts) > 1:
                    name += "-" + checkout

                results[folderHash] = name

    return results

# reuturns a set of (activeState runtimes installed to jupyter notebook)


def getInstalledJupyterRuntimes():
    setOfInstalled = set()

    #Make sure the path to the jupyter metadata actually exists (will not if jupyter notebook has never been run)
    if not os.path.exists(pathToJupyter):
          os.mkdir(pathToJupyter)

    # itterate through runtimes in jupyter metadata location
    for dir in os.listdir(pathToJupyter):
        # it is an activestate runtime if there is a as.yaml file
        if os.path.exists(pathToJupyter+'/'+dir+'/as.yaml'):
            setOfInstalled.add(dir)

    return setOfInstalled


def syncRuntimes(cachedRuntimes, installedJupyterRuntimes):

    # First we prune runtimes that are in installed but no longer cached
    for runtimeDir in installedJupyterRuntimes:
        if (runtimeDir not in cachedRuntimes):
            # Get fingerprinted runtime name from as.yaml
            with open(pathToJupyter+'/'+runtimeDir+'/as.yaml', "r") as file:
                runtimeName = file.read()
                print("Uninstalling: " + runtimeName)
            shutil.rmtree(pathToJupyter+"/"+runtimeDir)

    # Install runtimes that are cached and not already installed
    # Runtime update beahvioru(if they are already isntalled jupyter metadata remains the same-> still pointing to same oath)
    for runtime in cachedRuntimes:
        if runtime not in installedJupyterRuntimes:
            installRuntime(runtime, cachedRuntimes.get(runtime))


def installRuntime(runtimeHash, runtimeName):
    print("Installing: " + runtimeName)
    # make new folder
    os.mkdir(pathToJupyter+'/'+runtimeHash)
    # modify template
    metaTemplate["display_name"] = runtimeName
    metaTemplate["argv"][0] = pathToRuntimes+'/'+runtimeHash+'/usr/bin/python3'
    # write the template
    with open(pathToJupyter+'/'+runtimeHash+'/kernel.json', "w") as file:
        file.write(json.dumps(metaTemplate))
    # write the as.yaml file
    with open(pathToJupyter+'/'+runtimeHash+'/as.yaml', "w") as file:
        file.write(runtimeHash + ':' + runtimeName)
    # Copy AS icons
    shutil.copy("logo-32x32.png", pathToJupyter+'/'+runtimeHash)
    shutil.copy("logo-64x64.png", pathToJupyter+'/'+runtimeHash)


syncRuntimes(getCachedRuntimes(), getInstalledJupyterRuntimes())
print("ActiveState Runtimes In Sync With Jupyter")
