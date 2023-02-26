import numpy as np

# FONTS: Lucida Grande, Tahoma, Geneva, Verdana, sans-serif

# Offical Grundfos colours

Corporate_blue = 1/255*(np.array([17, 73, 123]))
Blue_1         = 1/255*(np.array([10, 44, 74]))
Blue_2         = 1/255*(np.array([52, 100, 143]))
Blue_3         = 1/255*(np.array([0, 104, 180]))
Blue_4         = 1/255*(np.array([0, 158, 227]))

Black          = 1/255*(np.array([0, 0, 0]))
Grey_1         = 1/255*(np.array([51, 51, 51]))
Grey_2         = 1/255*(np.array([153, 153, 153]))
Grey_3         = 1/255*(np.array([201, 201, 201]))
Grey_4         = 1/255*(np.array([214, 214, 214]))
Grey_5         = 1/255*(np.array([222, 222, 222]))
Grey_6         = 1/255*(np.array([242, 242, 242]))
Grey_7         = 1/255*(np.array([249, 249, 249]))
White          = 1/255*(np.array([255, 255, 255]))

Green_2        = 1/255*(np.array([74, 162, 4]))
Red            = 1/255*(np.array([221, 0, 40]))
Red_close      = 1/255*(np.array([232, 17, 35]))
Red_close_press= 1/255*(np.array([241, 112, 122]))
Yel_min        = 1/255*(np.array([255, 189, 68]))
Yel_min_press  = 1/255*(np.array([255, 208, 121]))
Orange         = 1/255*(np.array([244, 149, 0]))

#######
Corporate_blue_light = 1/255*(np.array([22, 97, 165]))
Corporate_blue_light2 = 1/255*(np.array([28, 121, 206]))
Grundfos_lightblue = 1/255*(np.array([0, 158, 227]))
Grundfos_bluegrey = 1/255*(np.array([157, 180, 200]))
Grundfos_grey_highlight = 1/255*(np.array([100, 100, 100]))
Grundfos_grey = 1/255*(np.array([80, 80, 80]))
Grundfos_lightgrey = 1/255*(np.array([116, 116, 116]))
pump_red = 1/255*(np.array([162, 72, 79]))

gui_blue = 1/255*(np.array([65, 109, 149]))
gui_lightgrey = 1/255*(np.array([180, 180, 180]))
gui_darkgrey = 1/255*(np.array([60, 60, 60]))
gui_ultradarkgrey = 1/255*(np.array([40, 40, 40]))


#######

green_screen = 1/255*(np.array([112, 173, 71]))



# =============================================================================
#  Converting to hex
# =============================================================================
def RGBtoHex(vals, rgbtype=1):
    """
    CONVERT RGB COLOR TO HEX COLOR
    :param vals: An RGB/RGBA tuple
    :param rgbtype:  Valid valus are: 1 - Inputs are in the range 0 to 1
                                      256 - Inputs are in the range 0 to 255
    :return: A hex string in the form '#RRGGBB' or '#RRGGBBAA'
    """
    if len(vals)!=3 and len(vals)!=4:
        raise Exception("RGB or RGBA inputs to RGBtoHex must have three or four elements!")
    if rgbtype!=1 and rgbtype!=256:
        raise Exception("rgbtype must be 1 or 256!")
    if rgbtype==1:
        vals = [255*x for x in vals]  #Convert from 0-1 RGB/RGBA to 0-255 RGB/RGBA
    return '#' + ''.join(['{:02X}'.format(int(round(x))) for x in vals])