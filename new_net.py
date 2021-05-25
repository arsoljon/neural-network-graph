'''
x_input, x_hidden & x_output are the resepective columns
y_input, y_hidden & y_output hold the respective nodes for each column. 
y_label_loc is reserved for the y value of the titles of each column
circle_size is the diameter of each node. 
'''

class New_net:
    def __init__(self, x_i, y_i, x_h, y_h, x_o, y_o):       
        self.x_input = x_i
        self.y_input = y_i
        self.x_hidden = x_h
        self.y_hidden = y_h
        self.x_output = x_o
        self.y_output = y_o
        self.y_label_loc = 50
        self.circle_size = 80
      
        
    def draw_net(self):
        self.move_nodes()
        self.move_layers()
        self.draw_weights()
        self.draw_nodes()
        self.write_labels()

    
    def move_nodes(self):
        #nodes area for selection of each layer. 
        area_input = [self.x_input-(self.circle_size), self.x_input+(self.circle_size)]
        area_hidden = [self.x_hidden-(self.circle_size/2), self.x_hidden+(self.circle_size/2)]
        area_output = [self.x_output-(self.circle_size/2), self.x_output+(self.circle_size/2)]
        if mousePressed:
            if mouseX > area_input[0] and mouseX < area_input[1]: 
                self.create_space(self.y_input)
            elif mouseX > area_hidden[0] and mouseX < area_hidden[1]:
                self.create_space(self.y_hidden)
            elif mouseX > area_output[0] and mouseX < area_output[1]:
                self.create_space(self.y_output)
           
    
    def create_space(self, y_nodes):
        speed_of_change = 1
        change = map(mouseY, height, 0, -speed_of_change, speed_of_change)
        mid_index = len(y_nodes)/2
        self.set_y_labels(y_nodes, change)
        if (len(y_nodes) % 2) == 0: 
            if len(y_nodes) >= 2:
                for i in range(len(y_nodes)):
                    #mid_index must be altered by 0.5 in c to compensate 
                    # for no node existing in the middle. 
                    c = change * ((mid_index - 0.5) - i)
                    if i < mid_index:
                        y_nodes[i] += c
                    else:
                        y_nodes[i] += c
        else:
            if len(y_nodes) > 1:
                for i in range(len(y_nodes)):
                    c = change * (mid_index - i)
                    if i < mid_index:
                        y_nodes[i] += c
                    elif i > mid_index:
                        y_nodes[i] += c
    
    def set_y_labels(self, y_nodes, change):
        if y_nodes == self.y_input:
            if y_nodes[0] < self.y_hidden[0] and y_nodes[0] < self.y_output[0]:
                self.y_label_loc += change
        elif y_nodes == self.y_hidden:
            if y_nodes[0] < self.y_input[0] and y_nodes[0] < self.y_output[0]:
                self.y_label_loc += change
        elif y_nodes == self.y_output:
            if y_nodes[0] < self.y_hidden[0] and y_nodes[0] < self.y_input[0]:
                self.y_label_loc += change
                
    def move_layers(self):
        #Label area for selection of each layer. 
        area_input = [self.x_input-(self.circle_size), self.x_input+(self.circle_size)]
        area_hidden = [self.x_hidden-(self.circle_size/2), self.x_hidden+(self.circle_size/2)]
        area_output = [self.x_output-(self.circle_size/2), self.x_output+(self.circle_size/2)]
        if mousePressed:
            if mouseX > area_input[0] and mouseX < area_input[1]:
                self.x_input = mouseX
            elif mouseX > area_hidden[0] and mouseX < area_hidden[1]:
                self.x_hidden = mouseX
            elif mouseX > area_output[0] and mouseX < area_output[1]:
                self.x_output = mouseX
        
    def drawArrow(self, cx, cy, nx, ny):
        strokeWeight(2)
        stroke(1)
        a_len = 8
        line(cx,cy,nx, ny)
        strokeWeight(4)
        line(nx, ny, nx - a_len - 2, ny - a_len)
        line(nx, ny, nx - a_len - 2, ny + a_len)
        
    def draw_nodes(self):
        for i in range(len(self.y_input)):
            fill("#E4DBFF")
            strokeWeight(1)
            stroke(100)
            ellipse(self.x_input, self.y_input[i], self.circle_size, self.circle_size)
        for i in range(len(self.y_hidden)):
            fill("#EA62FF")
            stroke(100)
            ellipse(self.x_hidden, self.y_hidden[i], self.circle_size, self.circle_size)
        for i in range(len(self.y_output)):
            fill("#FF4848")
            stroke(100)
            ellipse(self.x_output, self.y_output[i], self.circle_size, self.circle_size)

    def draw_weights(self):
        for i in range(len(self.y_input)):
            for j in range(len(self.y_hidden)):
                self.drawArrow(self.x_input + (self.circle_size / 2), self.y_input[i], self.x_hidden - (self.circle_size / 2), self.y_hidden[j])
                
        for i in range(len(self.y_hidden)):
            for j in range(len(self.y_output)):
                self.drawArrow(self.x_hidden + (self.circle_size / 2), self.y_hidden[i], self.x_output - (self.circle_size / 2), self.y_output[j])

        
    def write_labels(self):
        #headers
        const = loadFont("SourceCodePro-Semibold-48.vlw")
        textFont(const, 32)
        y_text = 50
        fill(1)
        
        text("Input", self.x_input - 50, self.y_label_loc)
        text("Hidden", self.x_hidden - 50, self.y_label_loc)
        text("Output", self.x_output - 50, self.y_label_loc)
        
        #node labels
        
        fill(1)
        big_text = self.circle_size / 4.5
        small_text = big_text * 0.9
        x_change = 33
        y_change = 5
        x_for_subscripts = [self.x_input + (self.circle_size / 3) - 7, self.x_hidden + (self.circle_size / 3) + 5, self.x_output + (self.circle_size / 3) + 3]
        for i in range(len(self.y_input)):
            if i == (len(self.y_input) - 1):
                textSize(big_text)
                text("input", self.x_input - x_change, self.y_input[i] + y_change)
                textSize(small_text)
                text("n", x_for_subscripts[0], self.y_input[i] + (y_change *2) )
            else:
                textSize(big_text)
                text("input", self.x_input - x_change, self.y_input[i] + y_change)
                textSize(small_text)
                text("{0}".format(i + 1), x_for_subscripts[0], self.y_input[i] + (y_change *2) )                

        
        for i in range(len(self.y_hidden)):
            if i == (len(self.y_hidden) - 1):
                textSize(big_text)
                text("hidden", self.x_hidden - x_change, self.y_hidden[i] + y_change)
                textSize(small_text)
                text("n", x_for_subscripts[1], self.y_hidden[i] + (y_change *2) )
            else:
                textSize(big_text)
                text("hidden", self.x_hidden - x_change, self.y_hidden[i] + y_change)
                textSize(small_text)
                text("{0}".format(i + 1), x_for_subscripts[1], self.y_hidden[i] + (y_change *2) )                
        
        for i in range(len(self.y_output)):
            textSize(big_text)
            text("output", self.x_output - x_change, self.y_output[i] + y_change)
            textSize(small_text)
            text("{0}".format(i + 1), x_for_subscripts[2] , self.y_output[i] + (y_change *2) )
            
        #ellipses punctuation 
        if len(self.y_input) > 1:
            last_loc = self.y_input[len(self.y_input)-1]
            second_to_last_loc = ((self.y_input[len(self.y_input)-1] - self.y_input[len(self.y_input)-2]) / 2)
            y_ellip = last_loc - second_to_last_loc + 3
            x_ellip = self.x_input - (self.circle_size / 6)
            textSize(big_text)
            text("...", x_ellip, y_ellip)
        if len(self.y_hidden) > 1:
            last_loc = self.y_hidden[len(self.y_hidden)-1]
            second_to_last_loc = ((self.y_hidden[len(self.y_hidden)-1] - self.y_hidden[len(self.y_hidden)-2]) / 2)
            y_ellip = last_loc - second_to_last_loc + 3
            x_ellip = self.x_hidden - (self.circle_size / 6)
            textSize(big_text)
            text("...", x_ellip, y_ellip)
            
        
