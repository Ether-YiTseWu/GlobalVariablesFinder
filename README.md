# GlobalVariablesFinder
Use python shell and ctags command line tool to list all the global variables in the .c files

## Usage
### Environment
- OS : Ubuntu (or Linux-Based)
- python libraries : subprocess, argparse, csv
- tool : ctags

### Command
- python finder.py -f "your folder name"

### Result
- A CSV file named report.csv
| ITEM | Variable Name | In Which Program |
| :-----| ----: | :----: |
| 0 | temp | swap.c |
| 1 | count | countNum.c |
