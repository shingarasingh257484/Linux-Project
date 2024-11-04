import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Clock")

# Create a label to display the time
label = tk.Label(root, font=("Helvetica", 48), fg="black")
label.pack()

# Start the time update
update_time()

# Run the application
root.mainloop()