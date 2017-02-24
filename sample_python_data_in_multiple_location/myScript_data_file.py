import os
import subprocess
from subprocess import call

# Define the folders where your data files are located. 
# It can be single location or multiple locations.
# The below are the example data paths. In this example 
# data files are located across data, data1, 
# data2, data3 and data4 folders in the home directory 
# /home/vbhadra. You have to modify the path as per your 
# folder staructure and data location/path.

#folderA, folderB, folderC, folderD, folderE are python variables.
folderA = "/home/vbhadra/data"
folderB =  "/home/vbhadra/data1"
folderC =  "/home/vbhadra/data2"
folderD =  "/home/vbhadra/data3"
folderE =  "/home/vbhadra/data4"

# This is the function which is called for running the external 
# program read_data_prog.In this example the read_data_prog program 
# is located in the home directory /home/vbhadra/.
def run_mrtrix_program(path, file_name):
	print "Reading data from ", path, file_name, "..."
	call([os.path.expanduser('~/read_data_prog'), os.path.join(path, file_name)])

# Below folders is another python variable. It contains the list of 
# the folders where data is located.
folders = [folderA, folderB, folderC, folderD] 

# The below function list_sp_files() looks into the various folders and 
# find out the data files available there.
# If you deifne your data location correctly above this function will 
# find out the data files for you and call the 
# external program with each data file.
def list_sp_files():
    for folder in folders: #this is a for loop in python
        path = '%s' % (folder)  
	num_files = len(os.listdir(path))  
	print "Total number of data files found " + str(num_files) 
	for i in range(num_files):   
		file_name = os.listdir(path)[i]  
		run_mrtrix_program(path, file_name)  


# You do not have to have main() function in apython 
# script but in some ways it is good to have.
def main(): 
	list_sp_files() 

if __name__ == "__main__":
    main()
