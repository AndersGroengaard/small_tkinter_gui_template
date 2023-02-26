# ============================================================================= 
# from tkinter import Tk, RIGHT, BOTH, RAISED, Text, TOP, BOTH, X, N, LEFT, W, E, S
# import os
# #import create_cad
# import grundfos_library as gl
# =============================================================================


import tkinter as tk
from tkinter import ttk, W, LEFT, RIGHT
from PIL import ImageTk, Image

# =============================================================================
#  Splash Screen
# =============================================================================

class SplashScreen(tk.Tk):
    """
    ===========================================================================
    ||  Class for instantiating a splash screen                              ||
    ===========================================================================
    ||   INPUT:                                                              ||
    ||      time (int) (optional) : Specify the amount milliseconds the      ||
    ||                              splash screen should be displayed for    ||
    ||                                                                       ||
    ||=======================================================================||
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.image_file_path = "./imgs/splash.PNG"                             # Path to the image that we want to use
        self.display_time = kwargs.get("time", 4000)                           # Number of milliseconds the splash screen should be displayed
        
        self.overrideredirect(True)                                            # Removes the top bar where you can normall close and minimise etc...
        width = self.winfo_screenwidth()                      
        height = self.winfo_screenheight()
                         
        image = tk.PhotoImage(file=self.image_file_path)                       # Loading the splash image
        x = int((width / 2) - (image.width() / 2))
        y = int((height / 2) - (image.height() / 2))
        geometry = '{}x{}+{}+{}'.format(image.width() - 5, image.height() - 5, x, y)
        self.geometry(geometry)
        canvas = tk.Canvas(self, width=image.width(), height=image.height())
        canvas.pack()
        canvas.create_image(0, 0, image=image, anchor='sw')
        self.after(self.display_time, self.destroy)                            # Destroy window after time as expired
       

# =============================================================================
#  CONFIGURE MAIN FRAME AND STYLES
# =============================================================================

 

class MainApplication(tk.Tk):
    """
    ===========================================================================
    ||  Class for configuring our main application window and styles         ||
    ===========================================================================
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
       
        self.title('DataFlow 2023 v.0.1')                                      # Specifying the title of the window
        self.iconbitmap('./imgs/icon.ico')                                     # Adding our own icon to the app
        w = 760                                                                # width for the Tk root
        h = 600                                                                # height for the Tk root      
        ws = self.winfo_screenwidth()                                          # width of the screen
        hs = self.winfo_screenheight()                                         # height of the screen
        x = (ws / 2) - (w / 2)                                                 # calculate x starting coordinates... 
        y = (hs / 2) - (h / 2)                                                 # ...and y starting coordinates for the Tk root window
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))                            # Specifying window dimensions.
     
        
       # ======================================================================
       #  CREATE FRAMES
       # ======================================================================
    
        CAD_config_frame = ttk.LabelFrame(self, text='Create Custom Product')
        CAD_config_frame.grid(row=0, column=0, sticky=W, padx=5, pady=2)
      
        descrip_frame = ttk.LabelFrame(CAD_config_frame, text='Description')
        descrip_frame.grid(row=0, column=0, sticky=W, padx=5, pady=2, columnspan=4)
       
        
        descript_text = tk.Label(descrip_frame, text="Input volume flow rate, Q, and Head height, H, " \
                                                     "\nand create one ore more corresponding CAD-files "\
                                                     "based on the scaling laws, " \
                                                     "\nusing the UMS-20-20 centrifugal pump as a base\n" \
                                                     "\n" \
                                                     "Input a either a single value in Q and H or a \n" \
                                                     "series of values to create multiple products, eg.\n" \
                                                     "Q: 1, 2, 4 \n" \
                                                     "H: 1.5, 2.5, 5\n" \
                                                     "\n" \
                                                     "Output CAD-files are saved in a folder with the format:\n" \
                                                     "ProductType_Q_Q-value_H_H-value",
                               anchor='w', justify=LEFT, font=('AU Passata', 9, 'normal'))
        descript_text.grid(row=0, column=0, sticky=W, padx=5, pady=10)
       
       # ======================================================================
       #  CREATE FRAMES
       # ======================================================================
       
        product_label = ttk.Label(CAD_config_frame, text="Choose Product:", anchor='e', justify=RIGHT,
                                 font=('AU Passata', 10, 'normal'))
      
# =============================================================================
#         product_image = Image.open("./imgs/donut_cycles.png")
#         
#         scaling = self.prd_img_width / product_image.size[0]
#         img = ImageTk.PhotoImage(product_image.resize((self.prd_img_width, 
#                                                        int(product_image.size[1] * scaling)), 
#                                                       Image.ANTIALIAS))
# =============================================================================

        self.panel = ttk.Label(CAD_config_frame)#, image=img)
        
        self.choice_img_dict = {"Product A":"./imgs/donut_cycles.png", 
                                "Product B": "./imgs/glass_w_rain.png"}
        
        self.prd_img_width = 300
        self.v = tk.StringVar()
        self.v.trace('w', self.on_field_change)
        self.Product_range = ttk.Combobox(CAD_config_frame, textvar=self.v, values=list(self.choice_img_dict.keys()))
        self.Product_range.current(0)
        

# =============================================================================
#          
#         
#         Q_label = ttk.Label(CAD_config_frame, text="Flow (Q):", anchor='e', justify=RIGHT, font=('AU Passata', 10, 'bold'))
#         Q_value = tk.StringVar()
#         Q_entry = ttk.Entry(CAD_config_frame, textvariable=Q_value, width=30)
#         Q_value.set('1')
#         Q_unit = ttk.Label(CAD_config_frame, text="[m\u00b3/s]", anchor='w', justify=LEFT, font=('AU Passata', 10, 'normal'))
#         H_label = ttk.Label(CAD_config_frame, text="Head (H):", anchor='e', justify=RIGHT, font=('AU Passata', 10, 'bold'))
#         H_value = tk.StringVar()
#         H_entry = ttk.Entry(CAD_config_frame, textvariable=H_value, width=30)
#         H_value.set('1.5')
#         H_unit = ttk.Label(CAD_config_frame, text="[m]", anchor='w', justify=LEFT, font=('AU Passata', 10, 'normal'))
#          
#       #  cwd = os.getcwd()
#         destination_label = ttk.Label(CAD_config_frame, text="Destination:", anchor='e', justify=RIGHT,
#                                        font=('AU Passata', 10, 'normal'))
#         destination_value = tk.StringVar()
#         destination_entry = ttk.Entry(CAD_config_frame, textvariable=destination_value, width=70)
#       #  destination_value.set(cwd + "\\Instantiated_products\\")
#          
#         suc_mes = tk.StringVar()
#         suc_mes.set(' ')
#         success_message = tk.Label(CAD_config_frame, textvariable=suc_mes, anchor='w', justify=LEFT,
#                                      font=('AU Passata', 10, 'normal'))
# =============================================================================
        # 
 
        self.panel.grid(row=0, column=4, sticky=W, padx=0, pady=0, rowspan=1)
        product_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.Product_range.grid(row=1, column=1, sticky=W, padx=5, pady=30, columnspan=2)
# =============================================================================
#         Q_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)
#         Q_entry.grid(row=2, column=1, sticky=W, padx=5, pady=5)
#         Q_unit.grid(row=2, column=2, sticky=W, padx=5, pady=5)
#         H_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)
#         H_entry.grid(row=3, column=1, sticky=W, padx=5, pady=5)
#         H_unit.grid(row=3, column=2, sticky=W, padx=5, pady=5)
#         destination_label.grid(row=4, column=0, sticky=W, padx=3, pady=25, columnspan=4)
#         destination_entry.grid(row=4, column=1, sticky=W, padx=3, pady=25, columnspan=4)
# =============================================================================
        create_CAD = ttk.Button(CAD_config_frame, text="Create CAD-files", width=50, command=self.button_action)
        create_CAD.grid(row=5, column=0, sticky=W, padx=5, pady=25, columnspan=4)
        
    def on_field_change(self, index, value, op):
        """
        Method for changing the displayed image for when the user changes
        the value in the drop down list.
        """
        print("Field change -> Changing image")
        
        choice = self.Product_range.get()
        chosen_img = self.choice_img_dict.get(choice)
        product_image = Image.open(chosen_img)
        scaling = self.prd_img_width / product_image.size[0]
        img2 = ImageTk.PhotoImage(product_image.resize((self.prd_img_width, 
                                                        int(product_image.size[1] * scaling)), 
                                                       Image.ANTIALIAS))
        self.panel.configure(image=img2)
        self.panel.image = img2
        
 
        

    def button_action(self):
        """
        Method for executing an action when the main button is clicked
        """
        print("Hello!")
        
        
# =============================================================================
#  MAIN 
# =============================================================================
        
if __name__ == "__main__":
   
   # splash = SplashScreen()
   # splash.mainloop()
   
    app = MainApplication()
    app.mainloop()


 
# 
# style = ttk.Style(root)  # Create a style
# #root.tk.call('source', './gui/azure/azure.tcl')  # Import the tcl file
# #style.theme_use('azure')  # Set the theme with the theme_use method
# 
# style.configure('.', font=('AU Passata', 12, 'normal'))
# style.configure('TButton', background=gl.RGBtoHex(gl.Blue_1), foreground='white', width=10, borderwidth=10,
#                 focusthickness=100, focuscolor=gl.RGBtoHex(gl.Grundfos_lightblue), font=('AU Passata', 10, 'bold'))
# 
# style = ttk.Style()
# style.configure("", foreground="red")
# 
# # ======================================================================================================================
# #  CREATE FRAMES
# # ======================================================================================================================
# 
# CAD_config_frame = ttk.LabelFrame(root, text='Create Custom Product')
# CAD_config_frame.grid(row=0, column=0, sticky=W, padx=5, pady=2)
# 
# descrip_frame = ttk.LabelFrame(CAD_config_frame, text='Description')
# descrip_frame.grid(row=0, column=0, sticky=W, padx=5, pady=2, columnspan=4)
 
# 
# # ======================================================================================================================
# #  CREATING CONTENTS IN CAD CREATION FRAME
# # ======================================================================================================================
# 
# product_label = ttk.Label(CAD_config_frame, text="Choose Product:", anchor='e', justify=RIGHT,
#                           font=('AU Passata', 10, 'normal'))
# 
# product_image = Image.open("./gui/donut_cycles.png")
# scaling = 300 / product_image.size[0]
# img = ImageTk.PhotoImage(product_image.resize((300, int(product_image.size[1] * scaling)), Image.ANTIALIAS))
# panel = ttk.Label(CAD_config_frame, image=img)
# 
# 
# def on_field_change(index, value, op):
#     if Product_range.get() == "Product A":
#         product_image = Image.open("./imgs/donut_cycles.png")
#         scaling = 300 / product_image.size[0]
#         img2 = ImageTk.PhotoImage(product_image.resize((300, int(product_image.size[1] * scaling)), Image.ANTIALIAS))
#         panel.configure(image=img2)
#         panel.image = img2
#     elif Product_range.get() == "Product B":
#         product_image = Image.open("./imgs/glass_w_rain.png")
#         scaling = 300 / product_image.size[0]
#         img2 = ImageTk.PhotoImage(product_image.resize((300, int(product_image.size[1] * scaling)), Image.ANTIALIAS))
#         panel.configure(image=img2)
#         panel.image = img2
# 
# #
# v = tk.StringVar()
# v.trace('w', on_field_change)
# Product_range = ttk.Combobox(CAD_config_frame, textvar=v, values=["Product A", "Product B"])
# # Product_range = ttk.Combobox(CAD_config_frame, textvar=v, values=["Product A", "Product B"])
# Product_range.current(0)
# 
# Q_label = ttk.Label(CAD_config_frame, text="Flow (Q):", anchor='e', justify=RIGHT, font=('AU Passata', 10, 'bold'))
# Q_value = tk.StringVar()
# Q_entry = ttk.Entry(CAD_config_frame, textvariable=Q_value, width=30)
# Q_value.set('1')
# Q_unit = ttk.Label(CAD_config_frame, text="[m\u00b3/s]", anchor='w', justify=LEFT, font=('AU Passata', 10, 'normal'))
# H_label = ttk.Label(CAD_config_frame, text="Head (H):", anchor='e', justify=RIGHT, font=('AU Passata', 10, 'bold'))
# H_value = tk.StringVar()
# H_entry = ttk.Entry(CAD_config_frame, textvariable=H_value, width=30)
# H_value.set('1.5')
# H_unit = ttk.Label(CAD_config_frame, text="[m]", anchor='w', justify=LEFT, font=('AU Passata', 10, 'normal'))
# 
# cwd = os.getcwd()
# destination_label = ttk.Label(CAD_config_frame, text="Destination:", anchor='e', justify=RIGHT,
#                               font=('AU Passata', 10, 'normal'))
# destination_value = tk.StringVar()
# destination_entry = ttk.Entry(CAD_config_frame, textvariable=destination_value, width=70)
# destination_value.set(cwd + "\\Instantiated_products\\")
# 
# suc_mes = tk.StringVar()
# suc_mes.set(' ')
# success_message = tk.Label(CAD_config_frame, textvariable=suc_mes, anchor='w', justify=LEFT,
#                             font=('AU Passata', 10, 'normal'))
# 
# 
# def instantiate_cad_files():
#     Q_values = [float(x) for x in Q_value.get().split(",")]
#     H_values = [float(x) for x in H_value.get().split(",")]
#     if len(Q_values) != len(H_values):
#         suc_mes.set('Error: Q and H series need to be of equal length!')
#         success_message.config(fg='red')
#     else:
#         if Product_range.get() == "Product A":
#             product = 'template_product_A'
#         elif Product_range.get() == "Product B":
#             product = 'template_product_B'
#         for i in range(len(Q_values)):
#             try:
#                 print("Button clicked!")
#                # create_cad.create_cad_file(H_values[i], Q_values[i], product, destination_value.get())
#             except FileExistsError:
#                 suc_mes.set('Error: Configuration already exists: '+ Product_range.get() +', Q: '+Q_value.get()[i]+ ', H: '+ H_value.get()[i])
#                 success_message.config(fg='red')
# 
#         suc_mes.set('CAD-files created!')
#         success_message.config(fg='green')
# 
# 
# create_CAD = ttk.Button(CAD_config_frame, text="Create CAD-files", width=50, command=instantiate_cad_files)
# 
# panel.grid(row=0, column=4, sticky=W, padx=0, pady=0, rowspan=1)
# product_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Product_range.grid(row=1, column=1, sticky=W, padx=5, pady=30, columnspan=2)
# Q_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Q_entry.grid(row=2, column=1, sticky=W, padx=5, pady=5)
# Q_unit.grid(row=2, column=2, sticky=W, padx=5, pady=5)
# H_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)
# H_entry.grid(row=3, column=1, sticky=W, padx=5, pady=5)
# H_unit.grid(row=3, column=2, sticky=W, padx=5, pady=5)
# destination_label.grid(row=4, column=0, sticky=W, padx=3, pady=25, columnspan=4)
# destination_entry.grid(row=4, column=1, sticky=W, padx=3, pady=25, columnspan=4)
# create_CAD.grid(row=5, column=0, sticky=W, padx=5, pady=25, columnspan=4)
# success_message.grid(row=5, column=4, sticky=W, padx=5, pady=5, columnspan=4)
# root.mainloop()
# =============================================================================

