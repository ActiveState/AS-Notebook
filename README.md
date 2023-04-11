# AS-Notebook

AS-Notebook is an integration tool that makes compatible ActiveState Python runtimes avliable as kernels to Jupter Notebook & Jupyter Lab.

## Installation

### Linux & macOS

In your terminal checkout the ActiveState platform project AS-Notebook. This will include a Python runtime to run this tool and a copy of Jupyter Notebook itself. Once you have the State Tool installed on your system open a terminal and run
```
state checkout ActiveStateSE/AS-Notebook
```
This will create a new folder AS-Notebook with the nessesary files. 

## Usage

Navigate to the AS-Notebook folder and run

```
state shell
```
This will make the runtimes checked out by the State Tool avliable as kernels to a local Jupyter notebook or Jupyter Lab instance. Note that a runtime needs to contain ipykernel to be compatible. 

Optionally at this point if you need to start a local instance of Jupyter notebook remeain in the AS-Notebook virtaul enviornment and run

```
jupyter notebook
```


### Requirements

* ActiveState StateTool is installed.
* The runtime you want jupyter to recognize has ipykernel installed and is checked out on your system.
* Only works on Mac & Linux
* Your Jupyter IDE is looking for kernels in the default path 
