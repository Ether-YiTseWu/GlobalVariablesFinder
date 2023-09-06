import subprocess
import argparse
import csv


### Log
print("Processing...")


### Arg parse
parser = argparse.ArgumentParser()
parser.add_argument('-f', type = str, help='folder')
args = parser.parse_args()


### Find .c and .h
print("Finding .c and .h...")
folder = args.f
cmd_findSrc = "find " + folder + " -name \"*.c\""
src_c_list = str(subprocess.Popen(cmd_findSrc, shell=True, stdout=subprocess.PIPE).communicate()[0]).split("\n")
cmd_findSrc = "find " + folder + " -name \"*.h\""
src_h_list = str(subprocess.Popen(cmd_findSrc, shell=True, stdout=subprocess.PIPE).communicate()[0]).split("\n")


### Generate global variable List
print("Finding Global Variables...")
cmd_generateGlobalVariable = "ctags -x --sort=yes --c-kinds=v "
variableName = []
variablePath = []
for src in src_c_list:
    variable_list = str(subprocess.Popen(cmd_generateGlobalVariable + src, shell=True, stdout=subprocess.PIPE).communicate()[0]).split("\n")
    for variable_data in variable_list:
        try:
            variable_data = variable_data.split()
            variableName.append(variable_data[0])
            variablePath.append(variable_data[3])
        except:
            pass
for src in src_h_list:
    variable_list = str(subprocess.Popen(cmd_generateGlobalVariable + src, shell=True, stdout=subprocess.PIPE).communicate()[0]).split("\n")
    for variable_data in variable_list:
        try:
            variable_data = variable_data.split()
            variableName.append(variable_data[0])
            variablePath.append(variable_data[3])
        except:
            pass


### CSV writting
print("CSV Writting...")
with open('report.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ITEM', 'Variable Name', 'In Which Program'])
    for i in range(len(variableName)):
        writer.writerow([i, variableName[i], variablePath[i]])
       
### Log
print("Done")

