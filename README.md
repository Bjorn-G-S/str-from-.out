# str from .out


* [General](#general-info)
* [Purpose](#purpose)
* [How-to](#how-to)
* [Dependencies](#Dependencies)
* [Contact](#Contact)
* [License](#License)


## General

`str from .out` is a python program to be used for 
changing reading a line from large number for files based on a string descriptor.
Currently `str from .out` is used at the section for catalysis at
the University of Oslo.

## Purpose

Easy batch read and copy data from files with of the ´.out´ format, creating a .csv with the data of interest data within the parent folder.


## How-to
How to use the program. The program can also be run using the Voila GUI for iPython


1. Import the program:
```
from scale_class import ScaleDataExtractor
```
2. Define the directory of the files that are to be screened and define an object:
```
folder_path = r'XXXXXX'
scale_extractor = ScaleDataExtractor(folder_path)
```
3. Run the program. the following message will the apear:
```
scale_extractor.extract_data()
```

A progress bar will show up indicating the progress of the screening, and a pop-up message will apear once the program is finished.

### Optional

If the code is to be run using voila, do the following. In the command promt, navigate tot the folder where the 'scale_class_voila.ipynb' is located:
```
cd C:\folder\...
```
Then write the following:
```
voila scale_class_voila.ipynb
```
This will open up the program with the voila GUI.

## Dependencies
This script requires a python enviornment with the following packages, and the packaged these depend on:
```
python          (3.9.7)
pandas          (1.3.3)
ipywidgets      (7.6.5)
jupyterlab      (3.1.7)
```

Optional when using the Voila GUI to excecute the code:
```
python          (3.9.7)
pandas          (1.3.3)
ipywidgets      (7.6.5)
jupyterlab      (3.1.7)
ipyfilechooser  (0.6.0)
voila           (0.4.0)
```

## Contact

For developer issues, please start a ticket in Github. You can also write to the dev team directly at  **b.g.solemsli@smn.uio.no**
#### Authors: 
Bjørn Gading Solemsli (@bjorngso).

## License
This script is under the MIT license scheme. 


