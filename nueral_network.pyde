add_library('pdf')
'''
Visualization of a basic neural net. 
Use 'input_count', 'hidden_count' & 'output_count' in the setup function to change
the amount of nodes respectively. 
However, there is a limit to the amount of nodes 
before they overlap the title of the columns. 
'''

from data import * 
from new_net import New_net as nn

def setup():
    size(900, 700)
    background("#DBFFFF")
    # These 3 counts dictate the amount of nodes per respective column.
    input_count = 3
    hidden_count = 4
    output_count = 2
    # Setting the coordinates for each node in their respective column.  
    x_input = float(width/5)
    y_input = []
    for i in range(input_count):
        new_y = 0 + (float(height/(input_count + 1)) * (i + 1))
        y_input.append(new_y)
    x_hidden = float(width/2)
    y_hidden = []
    for i in range(hidden_count):
        new_y = 0 + (float(height/(hidden_count + 1)) * (i + 1))
        y_hidden.append(new_y)
    x_output = float(0 + ((width/5)*4))
    y_output = []
    for i in range(output_count):
        new_y = 0 + (float(height/(output_count + 1)) * (i + 1))
        y_output.append(new_y)
    #y_output = float(height/2)
    global net
    net = nn(x_input, y_input, x_hidden, y_hidden, x_output, y_output)


def draw():
    background("#DBFFFF")
    net.draw_net()
    stroke(3)
    line(100, 100, 100, 100)
    #saveFrame("net-######.pdf")


        

    
