#Make sure the below mentioned installer have been install previously
import sys, os, glob

#Dictionary to put all the name of the images
dict_samples = {}

for file in glob.glob('*.jpg'):
  if 'dots.jpg' in file:
    sample = file.replace('dots.jpg', '')
    dict_samples[sample] = ''

# This will create few bash script for the individual images
text = '''#!/bin/bash
for colour in red yellow ; do
   echo -n "#name#dots: $colour "
   convert #name#dots.jpg -fuzz 20%                      \
     -fill white -opaque $colour -fill black +opaque white \
     -define connected-components:verbose=true             \
     -define connected-components:area-threshold=800       \
     -connected-components 8 output.jpg | grep -c "rgb(255,255,255)"
done
'''

#Optional step: to check whether the required images were taken into consideration
#print dict_samples

k = 0
for sample in dict_samples.keys():
  k += 1
  t = text.replace('#name#', sample)
  try:
    out.close()
  except:
    pass
  out = open('scripts/result' + str(k) + '.sh', 'w')
  out.write(t)
  print 'scripts/result' + str(k) + '.sh'