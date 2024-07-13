import tkinter as tk
from datetime import datetime, timedelta

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("300x150")
        self.running = False
        self.start_time = None
        self.elapsed_time = timedelta()

        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def update_time(self):
        if self.running:
            current_time = datetime.now()
            self.elapsed_time = current_time - self.start_time
            time_str = str(self.elapsed_time).split('.')[0]  # Remove microseconds
            self.label.config(text=time_str)
            self.root.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = datetime.now() - self.elapsed_time
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.stop()
        self.elapsed_time = timedelta()
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()

