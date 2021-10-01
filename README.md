# Count-Stomata and pavement cells

A step by step guide to count stomata using Linux

**Disclaimer** : Every file is given separately to cross check the results, before proceeding to the next step. The below codes are tested on Ubuntu 18.04.5 LTS using bash, Python2.7 or ImageMagick.

A. **_Installation_**

Install **conda** as instructed by https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html. 

Install **ImageMagick** as instructed by https://anaconda.org/conda-forge/imagemagick. By default, it will install all the dependencies along with the relavant libraries.

Install **python** using conda and then use pip, to install module/packages required - _sys, os, glob_.

Either *png or jpg* format are recommended. Since the image captured by microscope must be edited/measured using Microsoft paint 2D, if you save the file in another format like TIF, then you can change to above mentioned preferred format.

B. **_Drawing a sticker/dots over the leaf_**

Example files are attached in the rar format

location = /home/username/Documents

Steps to color the image

1. Open the file in the PAINT 3D and start painting as mentioned below.

2. Select option -> 2D Shapes -> round shape -> Both line type and fill should be red for _stomata_ -> similarly do for the _pavement cells_ using yellow color -> save image in a new folder. 

Save image file with the ending "dots.png" or "dots.jpg" (**file Extension** and **name ending** is much more important), since the next python file will look for this and start creating bash files. Warning: You should not work with original file received taken from microscope.

C. **_Create bash files for every images_**

1. Run command to create a new_folder/directory
    
    mkdir scripts
    
    Saved location = /home/username/Documents/scripts
    
2. Run the below command to create bash files separately for all the images
   
   python2.7 create_bash_files.py
    
   location = Saved location = /home/username/Documents

This will give output like below. If you want to redirect all the output to a text file then use "python2.7 create_bash_files.py >created_text.txt".

Result file should be in the file -> /home/username/Documents/created_text.txt

D. **_Counting the cells_**

Run the command "python2.7 count_stomata.sh >final_count.txt".

Result file should be in the file -> /home/username/Documents/final_count.txt
