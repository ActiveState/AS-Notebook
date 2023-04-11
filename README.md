# AS-Notebook

AS-Notebook is an integration tool that makes compatible ActiveState Python runtimes avliable as kernels to Jupter Notebook & Jupyter Lab.

## Installation

### Linux & macOS

Naviagte to the settings page of your ActiveState Platform project and add the url of this git repo in the appropriate field. When you state checkout your runtime for the first time this repo will automaticly be cloned. Otherwise you can clone this repo manaully using Git.


## Usage

If you added this repo to your ActiveState project it will automaitlcly be run when you activate or checkout your runtime for the first time. You can also run main.py manually at any time. When this integration tool is run all projects (not just the runtime that executed the tool) currently checked out by the state tool will be synced with Jupyter's Kernel Manager. 

### Requirements

* ActiveState StateTool is installed.
* The runtime you want jupyter to recognize has ipykernel installed and is checked out on your system.
* Only works on Mac & Linux
* Your Jupyter IDE is looking for kernels in the default path 
