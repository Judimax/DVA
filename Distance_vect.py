from try_this import* 
def DVA(source_ltr,dest_ltr):
        print(type(source_ltr))
        if source_ltr == dest_ltr:
            return 0
        
        else:
            blue = 9999
            red = 9999
            yellow = 9999
            green = 9999
            print(str(source_ltr))
            if source_ltr.values.l_value != 0:
                print(type(source_ltr.left))
                blue =source_ltr.values.l_value + DVA(source_ltr.left,dest_ltr)
            if source_ltr.values.r_value != 0:
                red =source_ltr.values.r_value + DVA(source_ltr.right,dest_ltr)
            if source_ltr.values.u_value != 0:
                yellow =source_ltr.values.r_value + DVA(source_ltr.up,dest_ltr)
            if source_ltr.values.d_value != 0:
                green =source_ltr.values.r_value + DVA(source_ltr.down,dest_ltr)

                answer = min(blue,red,yellow,green)

            return answer

def values():
    
    class values:

        def __init__(self):

                self.l_value = 0
                self.r_value = 0
                self.u._value = 0
                self.d_value =0
    return values
