# Count-Stomata

This is for biologists, a step by step guide to count stomata using Linux. 

Every file is given separately to cross check the results,  before proceeding to the next step.

The below codes are tested on Ubuntu 18.04.5 LTS using bash, Python2.7 or ImageMagick.

Install conda as instructed by https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html. 

Install ImageMagick as instructed by https://anaconda.org/conda-forge/imagemagick. By default, it will install all the dependencies along with the relavant libraries.

Here, *png* format is used, since the image captured by microscope must be edited/measured using Microsoft paint 2D. If you saved the file in another format such as TIF or jpg. then open the file in the PAINT 3D and start painting as mentioned below.

Drawing a sticker over the leaf
1. Open image file in PAINT 3D
2. Select option -> 2D Shapes -> round shape -> Both line type and fill should be red for _stomata_ -> similarly do for the _pavement cells_ using yellow color -> save image in a new folder. Save image file with the ending dots.png. (**file Extension** and **name ending** is much more important, since the next python file will look for this and start creating batch files). Warning: You should not work with original file received taken from microscope.




