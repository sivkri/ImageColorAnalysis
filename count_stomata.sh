#!/bin/bash

# this will find the list of files present in "*.sh" and gives us output
# command to execute -bash -name_of_this_file -output_name


for file in ./scripts/*.sh; do
	bash $file 
done