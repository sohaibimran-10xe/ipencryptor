# import tkinter as tk
# from tkinter import filedialog, messagebox

# def copy_and_paste_to_new_file(src_file, dest_file, new_file):
#     # Open and read the content from the source file
#     with open(src_file, 'r') as src:
#         src_content = src.read()
    
#     # Open and read the existing content from the destination file
#     with open(dest_file, 'r') as dest:
#         dest_content = dest.read()

#     # Write the source content first, then append the destination content to a new file
#     with open(new_file, 'w') as new_f:
#         new_f.write(src_content +'\n' + dest_content + '\n' + '`pragma protect end')

# # Example usage
# src_file = 'encryptionkey.txt'
# dest_file = 'MySimpleDesign.v'
# new_file = 'MySimpleDesign_e.v'  # This is the newly created file

# copy_and_paste_to_new_file(src_file, dest_file, new_file)



# def copy_and_paste_at_beginning(src_file, dest_file):
#     # Open and read the content from the source file
#     with open(src_file, 'r') as src:
#         src_content = src.read()
    
#     # Open and read the existing content from the destination file
#     with open(dest_file, 'r') as dest:
#         dest_content = dest.read()

#     # Write the source content first, then append the original destination content
#     with open(dest_file, 'w') as dest:
#         dest.write(src_content + dest_content)


import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import sys

def copy_and_paste_to_new_files(src_files, keyfile):
    for src_file in src_files:
        # Open and read the content of the current source file
        with open(src_file, 'r') as src:
            src_content = src.read()

        # Open and read the key file
        with open(keyfile, 'r') as src:
            keycontent = src.read()
        
        global interm_files
        
        # Create a new file name by appending "_e" before the file extension
        file_parts = src_file.rsplit('.', 1)  # Splitting file name and extension
        new_file = f"{file_parts[0]}_e.{file_parts[1]}" if len(file_parts) > 1 else src_file + "_e"

        

        # Write the content to the new file
        with open(new_file, 'w') as new_f:
            new_f.write(keycontent + "\n" + src_content + "\n" + "`pragma protect end")

        # Notify the user of each file saved
        messagebox.showinfo("Success", f"File saved as {new_file}")
        interm_files.append(new_file)


def select_source_files():
    # Open file dialog to select multiple source files
    files = filedialog.askopenfilenames(title="Select Source Files", filetypes=[("All Files", "*.*")])
    if files:
        src_label.config(text="\n".join(files))
        global src_files
        src_files = files

def process_files():
    keyfile = "./encryptionkey.txt"
    if not src_files:
        messagebox.showerror("Error", "Please select source files.")
    else:
        copy_and_paste_to_new_files(src_files, keyfile)

def open_terminal_and_run_command():
    
     # Get the path where the executable or script is located
    if getattr(sys, 'frozen', False):  # If the application is running as a PyInstaller executable
        script_dir = os.path.dirname(sys.executable)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))    

    global final_files
    interm_files

    for interm_file in interm_files:
            
        # Create a new file name by appending "_e" before the file extension
        file_parts = interm_file.rsplit('.', 1)  # Splitting file name and extension
        new_file = f"{file_parts[0]}_protected.{file_parts[1]}" if len(file_parts) > 1 else interm_file + "_proctected"

        
        # Open a terminal and run the specified command
        command = f'ipecrypt --infile '+ interm_file  +' --outfile ' + new_file
        
        if os.name == 'nt':  # If the system is Windows
            subprocess.run(f'start cmd /K "{command}"', shell=True, cwd=script_dir)
        else:  # For macOS/Linux
            subprocess.run(f'x-terminal-emulator -e "{command}"', shell=True, cwd=script_dir)
        
        final_files.append(new_file)


def ammend_file():
    
    for final_file in final_files:

        # Read the file content
        with open(final_file, 'r') as file:
            lines = file.readlines()

        # Update the required lines
        for i, line in enumerate(lines):
            if line.startswith('`pragma protect encrypt_agent='):
                lines[i] = '`pragma protect encrypt_agent="10xEngineers"\n'
            elif line.startswith('`pragma protect encrypt_agent_info='):
                lines[i] = '`pragma protect encrypt_agent_info="10xEngineers"\n'

        # Write the updated content back to the file
        with open(final_file, 'w') as file:
            file.writelines(lines)

        # Notify the user of each file saved
        messagebox.showinfo("Success", f"File saved as {final_file}")

# Initialize GUI
root = tk.Tk()
root.title("File Content Processor")

src_files = []
interm_files = []
final_files = []
# Select Source Files Button
tk.Button(root, text="Select Source Files", command=select_source_files).pack(pady=10)
src_label = tk.Label(root, text="No source files selected")
src_label.pack()

# Process Button
tk.Button(root, text="Process Files and Save", command=process_files).pack(pady=10)

# Open Terminal and Run Command Button
tk.Button(root, text="Open Terminal and Run ipecrypt", command=open_terminal_and_run_command).pack(pady=20)

# Ammend The File with 10xEngineers
tk.Button(root, text="Ammend IPEncrypt to 10xE", command=ammend_file).pack(pady=20)

# Run the GUI loop
root.mainloop()

