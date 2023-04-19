# AS-Notebook

AS-Notebook is an integration tool that makes compatible ActiveState Python runtimes avliable as kernels to Jupter Notebook & Jupyter Lab.

## Installation

### Linux & macOS
If you do not already have the State Tool installed open a terminal and install by running:
```
sh <(curl -q https://platform.activestate.com/dl/cli/1755101228.1671555745_pdli01/install.sh)
```
In your terminal checkout the ActiveState platform project AS-Notebook. This will include a Python runtime to run this tool and a copy of Jupyter Notebook itself.
```
state checkout ActiveStateSE/AS-Notebook
```
This will create a new folder AS-Notebook with the necessary files.

## Usage

Navigate to the AS-Notebook folder and run

```
state run syncAgent
```
This will make all State Tool projects that support Jupyter Notebook visible to any local instance of the IDE. 

Optionally at this point if you need to start a local instance of Jupyter Notebook

```
state exec jupyter notebook
```


### Requirements

* ActiveState StateTool is installed.
* The projects/runtimes to be installed into Jupyter Notebook have ipykernel installed and are checked out on your system.
* macOS or Linux only
* Your local Jupyter IDE is looking for kernels in the default paths 
