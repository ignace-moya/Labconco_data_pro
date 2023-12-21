# -*- coding: utf-8 -*-
"""Labconco_data_processing.py
	by Ignace Moya
	2023 Dec 20

"""

import re
## In the Example folder there are three data sets that can be processed,
## Enter the file location for one of the three data sets (enable "location"),
## load the file (enable "load_file" and load-file.read())
#location = "/2023_dec12_w12_p1_2.TXT"
#location = "/2023_dec12_w12_p2_1.TXT"
#location = "/2023_dec12_w12_p3_1.TXT"
#load_file = open(location, "r")
#text = load_file.read()

## Make sure to enter the file location for saving the plotted data,
## see the second last line

## This is a demo data set for test purposes
text = ":<PROG=2 SEG=1H TRM= 299 SYS=-38 PRB1=-30 PRB2=-33 PRB3=+ 0 VAC=9999> :<PROG=2 SEG=1H TRM= 299 SYS=-37 PRB1=-30 PRB2=-33 PRB3=+ 0 VAC=9999>"
#print(text)

#Extract each parameter data from the text
pattern_PROG = r"(STNDBY|\d+)(?=\s*SEG)"
match_PROG = re.findall(pattern_PROG, text)
print ('PROG data total =', len(match_PROG), '\n PROG number:', match_PROG)

pattern_SEG = r"(\d+\w*|=\s?)(?=\s*TRM)"
match_SEG = re.findall(pattern_SEG, text)
print ('SEG data total =', len(match_SEG), '\n SEG values:', match_SEG)

pattern_TRM = r"(\d+|INDF)(?=\s*SYS)"
match_TRM = re.findall(pattern_TRM, text)
print ('TRM data total =', len(match_TRM), '\n TRM values:', match_TRM)

pattern_SYS = r"([+-]?\s?\d+)(?=\s*PRB1)" #r"SYS=([+-]?\d+)"
match_SYS = re.findall(pattern_SYS, text)
print ('SYS data total =', len(match_SYS), '\n SYS values:', match_SYS)

pattern_PRB1 = r"([+-]?\s?\d+)(?=\s*PRB2)" # r"PRB1=([+-]?\s?\d+)"
match_PRB1 = re.findall(pattern_PRB1, text)
print ('PRB1 data total =', len(match_PRB1), '\n PRB1 values:', match_PRB1)

pattern_PRB2 = r"PRB2=([+-]?\s?\d+)"
match_PRB2 = re.findall(pattern_PRB2, text)
print ('PRB2 data total =', len(match_PRB2), '\n PRB2 values:', match_PRB2)

pattern_VAC = r"VAC=(\s?\d+)"
match_VAC = re.findall(pattern_VAC, text)
print ('VAC data total =', len(match_VAC), '\n VAC values:', match_VAC)

### Remove space between +/-ve sign and number ####
Temp = []
for gap in match_SYS:
  temperature = gap.replace(" ", "")
  Temp.append(int(temperature))
print ('SYS data total:', len(Temp), '\n', Temp)  #checking to see if spaces were removed
#Temp.clear() #To reset the dicitonary for Temp

PRB1_int = []
for gap in match_PRB1:
  match_PRB1_s = gap.replace(" ", "")
  PRB1_int.append(int(match_PRB1_s))
print ('PRB1 data total:', len(PRB1_int), '\n', PRB1_int)  #checking to see if spaces were removed

### Remove space between +/-ve sign and number ####
PRB2_int = []
for gap in match_PRB2:
  match_PRB2_s = gap.replace(" ", "")
  PRB2_int.append(int(match_PRB2_s))
print ('PRB2 data total:', len(PRB2_int), '\n', PRB2_int) #checking to see if spaces were removed

Prog = []
for values in match_PROG:
  try:
    program = int(values)
    # print (numbers) #internal check
    Prog.append(program)
  except ValueError:
    Prog.append(values)
print ("Program No.:", Prog)
#Prog.clear() #To reset the dictionary for Prog

SEG =[]
for values in match_SEG:
  SEG.append(values)
print ("Segment step:", SEG)
#SEG.clear() #To reset the dictionary for SEG

TRM =[]
for values in match_TRM:
  try:
    numbers = int(values)
    TRM.append(numbers)
  except ValueError:
    TRM.append(values)
print ("Time remaining:", TRM)
#TRM.clear() #To reset the dictionary for TRM

VAC =[]
for values in match_VAC:
  numbers = int(values)
  VAC.append(numbers)
print ("Vac pressures:", VAC)
#VAC.clear() #To reset the dictionary for VAC

print ('Checking list PRB1_int', type(PRB1_int), 'temperature =', PRB1_int[2])

import pandas as pd
import os
## This is a check point, to ensure that the number of rows remain constant within the dataframe ###
initial = 1
prog_number = Prog[3]
final = min(len(Temp), len(PRB1_int), len(PRB2_int), len(TRM), len(VAC), len(SEG)) #determine which list has the minimum count
print ('minimum value in the set is', final)
# compile the dataframe, which will be used for plotting out the graph
df_compile = pd.DataFrame(
    {'PROG': Prog[initial:final], 'SEG': SEG[initial:final], 'TRM': TRM[initial:final],'SYS': Temp[initial:final],
     'VAC': VAC[initial:final], 'PRB1': PRB1_int[initial:final], 'PRB2': PRB2_int[initial:final]})

file_path_csv_info = '/content/drive/MyDrive/Colab Notebooks/lyo_program_{}.csv'.format(prog_number)
print('file name to be saved:', file_path_csv_info)
df_compile.to_csv(file_path_csv_info, sep=',')
if (not os.path.isfile(file_path_csv_info)):
    print("Error: <%s> file not found" %(file_path_csv_info))
else:
    print("File <%s> successfully saved!" %(file_path_csv_info))

print('Checking data to see if columns are present \n',
      df_compile['PROG'].head(4),'\n \n', df_compile['TRM'].head(4),
      '\n\n', df_compile['SYS'].head(4), '\n\n', df_compile['PRB1'].head(4))
print ('\n', 'Program No:', df_compile['PROG'][0])
print ('list of Column names:', df_compile.columns)
print ('initial and final counts:', initial, 'to', len(df_compile['TRM']))
print ('index number:', df_compile.index)
print ("Checking the index of dataframe form 0 to 19", df_compile.head(20).index.tolist())
print ("Checking the max and min values for the pressure", 'min =', min(df_compile['VAC']), 'max=',max(df_compile['VAC']))

import seaborn as sns
import matplotlib.pyplot as plt

total = final #total length the data set determined from minimum count from the data set
initial = 1
x_values = df_compile[initial:total].index.tolist() #Lyo takes readings every 10 seconds, so one requires the total number of counts
y_data01 = 'SYS'
y_data02 = 'PRB2'
y_data03 = 'PRB1'
y_VAC = 'VAC'

# Create a basic line plot
ax1 = sns.lineplot(x = x_values, y = df_compile[y_data01][initial:total], linestyle='dashed', label = y_data01)
sns.lineplot(x = x_values, y = df_compile[y_data02][initial:total], linestyle='solid', label = y_data02)
sns.lineplot(x = x_values, y = df_compile[y_data03][initial:total], linestyle='solid', label = y_data03)
#Secondary axis for pressure
ax2 = plt.gca().twinx()
sns.lineplot(x= x_values, y= df_compile[y_VAC][initial:total], ax=ax2,linestyle='solid', color='blue', label = y_VAC)

# Set labels, legend location, x&y limits, and graph theme

plt.title('System and Sample Temperatures for Program {}'.format(Prog[initial]))
ax1.set_ylabel('Temperature (Celsius)')
ax1.set_ylim(-45, 25) # y-axis start and end values for the temperature
ax1.legend(loc='center right', bbox_to_anchor=(1, 0.1)) # plot legend x,y location from 0 to 1
ax1.set_xlabel('Time (x10 sec)')
plt.xlim(0, total) # x-axis start and end values
ax2.set_ylabel("Pressure (mTorr)", color='blue')
ax2.set_ylim(0, 3000) ## Setting the pressure limits
ax2.legend(loc='lower right', bbox_to_anchor=(1, 0.2)) # plot legend x,y location from 0 to 1
sns.set_theme(style="darkgrid")

# Show the plot
plt.show()
file_location = '/lyo_fig_program_{}.png'.format(prog_number)
plt.savefig(file_location, format='png',dpi=150)