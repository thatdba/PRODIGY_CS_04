import tkinter as tk
import logging

class Keylogger:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Keylogger")
        self.text = tk.Text(self.root, wrap="word", height=10, width=40)
        self.text.pack()
        self.start_button = tk.Button(self.root, text="Start Logging", command=self.start_logging)
        self.start_button.pack()
        self.stop_button = tk.Button(self.root, text="Stop Logging", command=self.stop_logging, state=tk.DISABLED)
        self.stop_button.pack()
        self.log_file = "keylog.txt"
        self.logger = logging.getLogger("Keylogger")
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(self.log_file)
        self.logger.addHandler(handler)
        self.is_logging = False

    def start_logging(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.root.bind("<Key>", self.log_key)
        self.is_logging = True

    def stop_logging(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.root.unbind("<Key>")
        self.is_logging = False

    def log_key(self, event):
        key = event.char
        if key:
            self.logger.info(f"Key pressed: {key}")
            self.text.insert(tk.END, f"Key pressed: {key}\n")

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.root.mainloop()
