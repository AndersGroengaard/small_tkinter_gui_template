"""
===============================================================================
|| TKINTER TEMPLATE PROJECT 2023                                             ||
===============================================================================
||
||                                                             ,.,,,*     
||    DONUTMAKER 9000                                     ,,,,,,,,,...,,,*  
||                                                    .,,,,(,,,,,,/,,,,,,* 
||                                                   ..,,,,*///# ,.,.,,,** 
||                                                  ..,,,*,****,,....,,*** 
||                                                  ,,,*,,,,,.....,,*,,*/  
||    Made in Python 3.9                            .,,,,.,,,.,,,,.,,*/*   
||                                                    ,,,,,,,,,,,***/      
||                                                         *               
===============================================================================
""" 
 
import grundfos_library as gl
import tkinter as tk
from tkinter import ttk, W, LEFT, RIGHT
from PIL import ImageTk, Image


# =============================================================================
#  CUSTOM INPUT
# =============================================================================
 
version = "1.1.12-a"
appname = "DonutMaker 9000"
  

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
        tk.Tk.__init__(self)
        
        self.image_file_path = "./imgs/splash.png"                             # Path to the image that we want to use
        self.display_time = kwargs.get("time", 4000)                           # Number of milliseconds the splash screen should be displayed
        
        self.overrideredirect(True)                                            # Removes the top bar where you can normall close and minimise etc...
     
     #   self.wm_attributes('-type', 'splash') 
        self.width = self.winfo_screenwidth()                             
        self.height = self.winfo_screenheight()
                         
        self.image = tk.PhotoImage(file=self.image_file_path)                  # Loading the splash image
        self.x = int((self.width / 2) - (self.image.width() / 2))
        self.y = int((self.height / 2) - (self.image.height() / 2))
        self.image_geometry = '{}x{}+{}+{}'.format(self.image.width() - 5, 
                                                   self.image.height() - 5, 
                                                   self.x, self.y)
        self.geometry(self.image_geometry)
        self.canvas = tk.Canvas(self, width=self.image.width(), 
                                      height=self.image.height())
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')
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
        tk.Tk.__init__(self)
       
        self.app_name = kwargs.get("appname", "Appname")  
        self.version = kwargs.get("versipn", "1.0.0-a")  
        
        self.title_string = self.app_name + " v" + self.version
        # Stuff to configure:
        self.title(self.title_string)                                          # Specifying the title of the window
        self.iconbitmap('./imgs/icon.ico')                                     # Adding our own icon to the app
        self.w = 760                                                           # width for the Tk root
        self.h = 600                                                           # height for the Tk root   
        
        # Calculating frame dimensions
        self.ws = self.winfo_screenwidth()                                     # width of the screen
        self.hs = self.winfo_screenheight()                                    # height of the screen
        self.x = (self.ws / 2) - (self.w / 2)                                  # calculate x starting coordinates... 
        self.y = (self.hs / 2) - (self.h / 2)                                  # ...and y starting coordinates for the Tk root window
        self.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))        # Specifying window dimensions.
        
        self.configure_gui_style()                                             # Initiating our style configuration 
        
        self.create_widgets()
        
        self.define_widget_layout()
        
        
    def configure_gui_style(self):
        self.style = ttk.Style(self)                                           # Create a style
        self.tk.call('source', './azure_theme/azure.tcl')                      # Import the tcl file 
        self.tk.call("set_theme", "light")                                     # Possible values for the azure tcl is either "light" or "dark"
        self.style.configure('.', font=('AU Passata', 12, 'normal'))           # Configuring the normal font 
        self.style.configure('TButton', background=gl.RGBtoHex(gl.Blue_1), 
                             foreground='white', width=10, borderwidth=10,
                             focusthickness=100, 
                             focuscolor=gl.RGBtoHex(gl.Grundfos_lightblue), 
                             font=('AU Passata', 10, 'bold'))
        
        
    def create_widgets(self):
       # ======================================================================
       #  CREATE FRAMES
       # ======================================================================
    
        self.main_frame = ttk.LabelFrame(self, text='Create Custom Product')
        self.main_frame.grid(row=0, column=0, sticky=W, padx=20, pady=20)
      
        class create_description_subframe:
      
            self.descrip_frame = ttk.LabelFrame(self.main_frame, text='Description')
            self.descrip_frame.grid(row=0, column=0, sticky=W, padx=5, pady=2, columnspan=4)
           
            self.descript = "Input volume flow rate, Q, and Head height, H, " \
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
                            "ProductType_Q_Q-value_H_H-value"
                            
            self.descript_label = tk.Label(self.descrip_frame, text= self.descript,
                                   anchor='w', justify=LEFT, font=('AU Passata', 9, 'normal'))
            self.descript_label.grid(row=0, column=0, sticky=W, padx=5, pady=10)
       
        create_description_subframe()
        
        
        
       # ======================================================================
       #  CREATE FRAMES
       # ======================================================================
       
        self.product_label = ttk.Label(self.main_frame, text="Choose Product:", anchor='e', justify=RIGHT,
                                 font=('AU Passata', 10, 'normal'))
 
        self.panel = ttk.Label(self.main_frame) 
        
        self.choice_img_dict = {"Pink Donut":"./imgs/donut_pink.png", 
                                "Green Donut": "./imgs/donut_green.png",
                                "Blue Donut": "./imgs/donut_blue.png",
                                "White Donut": "./imgs/donut_white.png",
                                }                                              # Dictionary for our dropdown choices as keys and present image as value
        
        self.prd_img_width = 300
        self.v = tk.StringVar()
        self.v.trace('w', self.on_field_change)
        self.Product_range = ttk.Combobox(self.main_frame, textvar=self.v, 
                                          values=list(self.choice_img_dict.keys()))
        self.Product_range.current(0)
        
        self.Q_label = ttk.Label(self.main_frame, text="Flow (Q):", anchor='e', 
                                 justify=RIGHT, font=('AU Passata', 10, 'bold'))
        self.Q_value = tk.StringVar()
        self.Q_entry = ttk.Entry(self.main_frame, textvariable=self.Q_value, width=30)
        self.Q_value.set('1')
        self.Q_unit = ttk.Label(self.main_frame, text="[m\u00b3/s]", anchor='w', 
                                justify=LEFT, font=('AU Passata', 10, 'normal'))
        self.H_label = ttk.Label(self.main_frame, text="Head (H):", anchor='e', 
                                 justify=RIGHT, font=('AU Passata', 10, 'bold'))
        self.H_value = tk.StringVar()
        self.H_entry = ttk.Entry(self.main_frame, textvariable=self.H_value, 
                                 width=30)
        self.H_value.set('1.5')
        self.H_unit = ttk.Label(self.main_frame, text="[m]", anchor='w', 
                                justify=LEFT, font=('AU Passata', 10, 'normal'))
         
   
        self.destination_label = ttk.Label(self.main_frame, text="Destination:",
                                           anchor='e', justify=RIGHT,
                                           font=('AU Passata', 10, 'normal'))
        self.destination_value = tk.StringVar()
        self.destination_entry = ttk.Entry(self.main_frame, 
                                           textvariable=self.destination_value, 
                                           width=70)
     
         
        self.main_button = ttk.Button(self.main_frame, text="Create stuff!", 
                                      style="Accent.TButton",
                                      width=50, command=self.button_action)
        
        self.suc_mes = tk.StringVar()
        self.suc_mes.set(' ')
        self.success_message = tk.Label(self.main_frame, textvariable=self.suc_mes,
                                        anchor='w', justify=LEFT,
                                        font=('AU Passata', 10, 'normal'))
    
    def define_widget_layout(self): 
        """
        -----------------------------------------------------------------------
        | Method for defining the widget layouts                              |
        -----------------------------------------------------------------------
        """
        self.panel.grid(row=0, column=4, sticky=W, padx=25, pady=25, rowspan=1)
        self.product_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.Product_range.grid(row=1, column=1, sticky=W, padx=5, pady=30, columnspan=2)
        self.Q_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.Q_entry.grid(row=2, column=1, sticky=W, padx=5, pady=5)
        self.Q_unit.grid(row=2, column=2, sticky=W, padx=5, pady=5)
        self.H_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.H_entry.grid(row=3, column=1, sticky=W, padx=5, pady=5)
        self.H_unit.grid(row=3, column=2, sticky=W, padx=5, pady=5)
        self.destination_label.grid(row=4, column=0, sticky=W, padx=25, pady=25, columnspan=4)
        self.destination_entry.grid(row=4, column=1, sticky=W, padx=25, pady=25, columnspan=4) 
        self.main_button.grid(row=5, column=1, sticky=W, padx=25, pady=25, columnspan=4)
        
        
    def change_theme(self):
        """
        -----------------------------------------------------------------------
        | Method for changing betweeen light and dark theme                   |
        -----------------------------------------------------------------------
        """
        if self.tk.call("ttk::style", "theme", "use") == "azure-dark": 
            self.tk.call("set_theme", "light")                                 # Set light theme
        else:      
            self.tk.call("set_theme", "dark")                                  # Set dark theme
        
        
    def on_field_change(self, index, value, op):
        """
        -----------------------------------------------------------------------
        | Method for changing the displayed image for when the user changes   |
        | the value in the drop down list.                                    |
        -----------------------------------------------------------------------
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
        -----------------------------------------------------------------------
        |  Method for executing an action when the main button is clicked     |
        -----------------------------------------------------------------------
        """
        print("Button execution initiated")
        
        try:
            # < Method for button execution here >
            self.suc_mes.set('Operation succeeded!')
            self.success_message.config(fg='green')
            
        except Exception as e:    
            self.suc_mes.set(e)
            self.success_message.config(fg='red')
        
 
        
# =============================================================================
#  MAIN 
# =============================================================================
        
if __name__ == "__main__":
   
    splash = SplashScreen(time=5000)
    splash.mainloop()
   
    app = MainApplication(version=version, appname=appname)
    app.mainloop()

 
