import tkinter as tk
 
class BoroughInformation(tk.Frame):
    def __init__(self, master):
        # Initialize window using the parent's constructor
        tk.Frame.__init__(self,
                          master,
                          width=300,
                          height=200)
        # Set the title
        self.master.title('Borough Information')
        # This allows the size specification to take effect
        self.pack_propagate(0)
        #flexible pack layout manager
        self.pack()
 
        # The greeting selector
        # Use a StringVar to access the selector's value
        self.borough_var = tk.StringVar()
        self.borough = tk.OptionMenu(self,
                                      self.borough_var,
                                      'borough1',
                                      'borough2',
                                      'borough3')
        self.borough_var.set('borough1')
 
        # The go button
        self.go_button = tk.Button(self,
                                   text='Go',
                                   command=self.print_out)
 
        # Put the controls on the form
        self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
        self.borough.pack(fill=tk.X, side=tk.TOP)
 
    def print_out(self):
        #insert code from other python script
        
        print('If you live in %s, you should drive ___!' % (self.borough_var.get().title()))

    def run(self):
        self.mainloop()
 
app = BoroughInformation(tk.Tk())
app.run()
