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
 
import numpy as np
import tkinter as tk
from tkinter import ttk, W, LEFT, RIGHT, BOTTOM, TOP
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
 
import AUlibrary as AU
# =============================================================================
#  CUSTOM INPUT
# =============================================================================
 
version = "1.1.12-a"
appname = "DonutMaker 9000"
  

# =============================================================================
#  Miscellaneous Functions
# =============================================================================

def calculate_torus(n_pts, c, a):
    """
    ---------------------------------------------------------------------------
    | Caculate the points that make up a donut/torus                          |
    ---------------------------------------------------------------------------
    |  INPUTS:
    |     n_pts (int) : Number of points to plot
    |     c (float) : 
    |     a (float) : 
    |_________________________________________________________________________|
    """  
    U = np.linspace(0, 2*np.pi, n_pts)
    V = np.linspace(0, 2*np.pi, n_pts)
    U, V = np.meshgrid(U, V)
    X = (c+a*np.cos(V))*np.cos(U)
    Y = (c+a*np.cos(V))*np.sin(U)
    Z = a*np.sin(V)
    
    return X, Y, Z  


def add_donut_plot(widget=None):
    """
    ---------------------------------------------------------------------------
    | Plots a donut. Well technically its a torus, but donut sounds better.   |
    | If a tkinter widget is supplied as input, it will be packed onto        |
    | that widget. If nothing is supplied it will plot as normally.           |
    ---------------------------------------------------------------------------
    """
    x, y, z = calculate_torus(100, 1, 1)
    
    fig = plt.Figure(figsize=(3,3), dpi=100)
    ax = fig.add_subplot(projection='3d')
    if widget != None:
        figcanvas = FigureCanvasTkAgg(fig, widget)
    ax.plot_surface(x, y, z, antialiased=True, color=AU.AUpink)
    ax.set_title('Donut Plot') 
    ax.set_aspect('equal', adjustable='box')
 #   ax.patch.set_alpha(0.5)
    
    if widget == None:
        plt.show()
    else:
        return figcanvas, ax
    
    
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
        self.image_geometry = '{}x{}+{}+{}'.format(self.image.width() , 
                                                   self.image.height() , 
                                                   self.x, self.y)
        self.geometry(self.image_geometry)
        self.canvas = tk.Canvas(self, width=self.image.width(), 
                                      height=self.image.height(),
                                      highlightthickness=0)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')
        self.after(self.display_time, self.destroy)                            # Destroy window after time as expired
       
        self.update()
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
        self.w = 600                                                           # width for the Tk root
        self.h = 780                                                           # height for the Tk root   
        
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
        """
        -----------------------------------------------------------------------
        |  Method for configuring the overall style of the gui                |
        -----------------------------------------------------------------------
        """
        self.style = ttk.Style(self)                                           # Create a style
        self.tk.call('source', './azure_theme/azure.tcl')                      # Import the tcl file 
        self.tk.call("set_theme", "light")                                     # Possible values for the azure tcl is either "light" or "dark"
        self.style.configure('.', font=('AU Passata', 12, 'normal'))           # Configuring the normal font 
        self.style.configure('TButton', background=AU.RGBtoHex(AU.AUblue1), 
                             foreground='white', width=10, borderwidth=10,
                             focusthickness=100, 
                             focuscolor=AU.RGBtoHex(AU.AUlightblue), 
                             font=('AU Passata', 10, 'bold'))
        
        
    def create_widgets(self):
       # ======================================================================
       #  CREATE FRAMES
       # ======================================================================
    
        self.switch = ttk.Checkbutton(
            self, text="Theme", style="Switch.TCheckbutton", command=self.change_theme
        )
    
    
        self.display_frame = ttk.LabelFrame(self, text='Custom Donut')
  
      
        self.topframe = ttk.Frame(self.display_frame)

        self.panel = ttk.Label(self.topframe) 

        self.figcanvas, self.ax = add_donut_plot(self.topframe)
 
        
        self.widget_main_frame = ttk.Frame(self)
        self.product_parm_frame = ttk.LabelFrame(self.widget_main_frame, 
                                                 text='Product Parameters')    # Frame for the product parameters
        self.donut_parm_frame = ttk.LabelFrame(self.widget_main_frame, 
                                               text='Donut Parameters')        # Frame for the product parameters
        
        self.product_label = ttk.Label(self.product_parm_frame, 
                                       text="Choose Product:", 
                                       anchor='e', justify=RIGHT,
                                       font=('AU Passata', 10, 'normal')
                                       )

        
        self.choice_img_dict = {"Pink Donut":"./imgs/donut_pink.png", 
                                "Green Donut": "./imgs/donut_green.png",
                                "Blue Donut": "./imgs/donut_blue.png",
                                "White Donut": "./imgs/donut_white.png",
                                }                                              # Dictionary for our dropdown choices as keys and present image as value
        
        self.prd_img_width = 200
        self.v = tk.StringVar()
        self.v.trace('w', self.on_field_change)
        self.Product_range = ttk.Combobox(self.product_parm_frame, textvar=self.v, 
                                          values=list(self.choice_img_dict.keys()))
        self.Product_range.current(0)
        
        self.c_label = ttk.Label(self.donut_parm_frame, text="c :", anchor='e', 
                                 justify=RIGHT, font=('AU Passata', 10, 'bold'))
        self.c_value = tk.StringVar()
        self.c_spinbox = ttk.Spinbox(self.donut_parm_frame, from_=0, to=100, increment=0.1, state="readonly")
        self.c_spinbox.insert(0, 0.5)     
        self.c_value.set(1.0)

        self.a_label = ttk.Label(self.donut_parm_frame, text="c :", anchor='e', 
                                 justify=RIGHT, font=('AU Passata', 10, 'bold'))
        self.a_value = tk.StringVar()
        self.a_spinbox = ttk.Spinbox(self.donut_parm_frame, from_=0, to=100, increment=0.1, state="readonly")
        self.a_spinbox.insert(0, 0.5)     
        self.a_value.set(1.0)
      
        self.main_button = ttk.Button(self.widget_main_frame, text="Update Donut!", 
                                      style="Accent.TButton",
                                      width=50, command=self.button_action)
 
  
    
    def define_widget_layout(self): 
        """
        -----------------------------------------------------------------------
        | Method for defining the widget layouts                              |
        -----------------------------------------------------------------------
        """
        self.switch.pack( side = TOP, pady=25 )                                # Child of self 
        
        self.display_frame.pack( side = TOP )                                  # Child of self 
        self.topframe.pack( side = TOP )                                       # Child of self.display_frame

        self.panel.pack( side = LEFT )                                         # Child of self.topframe which is a child of self.display_frame
        self.figcanvas.get_tk_widget().pack( side = LEFT)                      # Child of self.topframe which is a child of self.display_frame
        self.widget_main_frame.pack( side = TOP )                              # Child of self 
        self.product_parm_frame.pack( side = TOP, fill=tk.BOTH, pady=15)       # Child of self.widget_main_frame
        self.donut_parm_frame.pack( side = TOP, fill=tk.BOTH , pady=15)        # Child of self.widget_main_frame
        
        self.product_label.pack( side = LEFT, padx=25, pady=25)                # Child of self.product_parm_frame
        self.Product_range.pack( side = LEFT, padx=25, pady=25)                # Child of self.product_parm_frame
        
        self.c_label.pack( side = LEFT, padx=15, pady=25)                      # Child of self.donut_parm_frame
        self.c_spinbox.pack( side = LEFT, padx=15, pady=25)                    # Child of self.donut_parm_frame
        self.a_label.pack( side = LEFT, padx=15, pady=25)                      # Child of self.donut_parm_frame
        self.a_spinbox.pack( side = LEFT, padx=15, pady=25)                    # Child of self.donut_parm_frame
 
        self.main_button.pack(  padx=25, pady=25, side = BOTTOM) 
 
        
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
                                                        Image.Resampling.LANCZOS))
        self.panel.configure(image=img2)
        self.panel.image = img2
        
        
    def update_donut_plot(self):
        
        colorchoice = self.Product_range.get()
        
        if colorchoice.startswith("Pink"):
            plotcolor = AU.AUpink
        elif colorchoice.startswith("Green"):
            plotcolor = AU.AUgreen
        elif colorchoice.startswith("Blue"):   
            plotcolor = AU.AUlightblue
        elif colorchoice.startswith("White"):
            plotcolor = AU.AUgrey
        else:
            plotcolor = AU.taskegul
        
        
        a = float(self.a_spinbox.get())
        c = float(self.c_spinbox.get())
        x, y, z = calculate_torus(100, a, c)
        self.ax.clear()                                                        # clear axes from previous plot
        self.ax.plot_surface(x, y, z, antialiased=True, color=plotcolor)
        self.ax.set_title('Donut Plot') 
        self.ax.set_aspect('equal', adjustable='box')
        self.figcanvas.draw()
        
        
    def button_action(self):
        """
        -----------------------------------------------------------------------
        |  Method for executing an action when the main button is clicked     |
        -----------------------------------------------------------------------
        """
        print("Button execution initiated")
        
        try:
            # < Method for button execution here >
            self.update_donut_plot()
                
      #      self.suc_mes.set('Operation succeeded!')
      #      self.success_message.config(fg='green')
            
        except Exception as e:    
            print(e)
       #     self.suc_mes.set(e)
       #     self.success_message.config(fg='red')
        
 
        
# =============================================================================
#  MAIN 
# =============================================================================
        
if __name__ == "__main__":
   
    splash = SplashScreen(time=5000)
    splash.mainloop()
   
    app = MainApplication(version=version, appname=appname)
    app.mainloop()

 
