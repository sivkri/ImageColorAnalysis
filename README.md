# Count-Stomata

A step by step guide to count stomata using Linux for biologists

**Disclaimer** : Every file is given separately to cross check the results,  before proceeding to the next step. The below codes are tested on Ubuntu 18.04.5 LTS using bash, Python2.7 or ImageMagick.

A. **_Installation_**

Install **conda** as instructed by https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html. 

Install **ImageMagick** as instructed by https://anaconda.org/conda-forge/imagemagick. By default, it will install all the dependencies along with the relavant libraries.

Install **python** using conda and then use pip, to install module/packages required - _sys, os, glob_.

It doesnt matter abou the usage of file format either *png or jpg* format are recommended. Since the image captured by microscope must be edited/measured using Microsoft paint 2D. If you saved the file in another format such like TIF, then you can change to above mentioned preferred format.

B. **_Drawing a sticker over the leaf_**
1. Open the file in the PAINT 3D and start painting as mentioned below.
2. Select option -> 2D Shapes -> round shape -> Both line type and fill should be red for _stomata_ -> similarly do for the _pavement cells_ using yellow color -> save image in a new folder. 

Save image file with the ending "dots.png" or "dots.jpg" (**file Extension** and **name ending** is much more important, since the next python file will look for this and start creating bash files). Warning: You should not work with original file received taken from microscope.

C. **_Create bash files for every images_**

D. **_Counting the cells_**
