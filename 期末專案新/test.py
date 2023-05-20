
import re
import textwrap as tw
import tkinter as tk




def Organize_line(list, width):
    new_list = ''
    total_space = 0
    for x in list:
        for y in x:
            if re.search(u'[\u4e00-\u9fff]', y):
                total_space += 2
            else:
                total_space += 1
    print(total_space)
    if total_space < width:
            
        for i in list:
            new_list += i
        list = new_list
        return list                
    
    max = len(list) 
    line = 0
    line_size = [0] * max
    while line < max:
        for char in list[line]:
            if re.search(u'[\u4e00-\u9fff]', char):
                line_size[line] += 2
                total_space += 2
            else:
                line_size[line] += 1
                total_space += 1
        line += 1
    

    line = 0
    next_line = 1
    print(list[next_line][1:])
    avg = int(total_space/max)
    print(line_size)
    enough = True
    while next_line < max:
        if enough == False:
            i = line
            temp_line = ''
            while i < len(list):
                temp_line += list[i]
                i+= 1
            list[line-1] += temp_line
            print(list)
        dif = width - line_size[line] 
        
        print(dif)
        if dif > 0:
            while dif > 0:
                if re.search(u'[\u4e00-\u9fff]', list[next_line][0]):
                    list[line] += list[next_line][0]
                    list[next_line] = list[next_line][1:]
                    line_size[next_line] -= 2
                    line_size[line] += 2
                    dif -= 2
                    print(list)
                    if line_size[next_line] == 0:
                        enough = False
                        break
                else:
                    list[line] += list[next_line][0]
                    list[next_line] = list[next_line][1:]
                    line_size[next_line] -= 1
                    line_size[line] += 2
                    dif -= 1
                    print(list)
                    if line_size[next_line] == 0:
                        enough = False
                        break                    
        line+=1
        next_line+=1
        
    for x in list:
        if x == '':
            list.remove(x)
    return list
    
line = '病毒感染寄主會引發免疫致病性(immunopathogenesis),下列何項因子最有可能造成第四型過敏及發炎反應(type IV hypersensitivity and inflammation)?'

q = Organize_line(tw.wrap(line, width = 33, break_on_hyphens=False, replace_whitespace = False), 100)

print(q)

# gui = tk.Tk()

# q = tk.Label(text = q[0], font=( 'ariel' ,14, 'bold' ))
# q.place(x=60, y=50)

# gui.mainloop()