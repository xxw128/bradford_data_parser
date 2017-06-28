import os
import pandas as pd

# Define file names
fprefix = '20170627Bradford' #insert file prefix here, without .txt
f_in = fprefix + '.txt'
f_out =fprefix + '_output.csv'

# Check to see if target file already exists
if os.path.isfile(f_out):
    raise RuntimeError('Output file ', f_out, 'already exists.')

# Clean data format, convert to .csv
with open(f_in, 'r') as f_in, open(f_out, 'w') as f_out:
    for line in f_in:
        if not line.startswith('_'):
            line = ','.join(line.split()) + '\n'
            f_out.write(line)

data = pd.read_csv('20170627Bradford_output.csv', skiprows=7)
data
