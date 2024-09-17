#!/usr/bin env python3
import tkinter as tk
from tkinter import ttk
import subprocess
import threading

class SpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Speed Test")
        self.root.geometry("300x150")
        self.create_widgets()

    def create_widgets(self):
        # Create and place widgets
        self.label = ttk.Label(self.root, text="Press 'Start Test' to measure speed.")
        self.label.pack(pady=10)

        self.start_button = ttk.Button(self.root, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=5)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack(pady=10)

    def start_test(self):
        # Disable the button while the test is running
        self.start_button.config(state="disabled")
        self.result_label.config(text="Testing...")
        # Run the speed test in a separate thread
        threading.Thread(target=self.run_speedtest).start()

    def run_speedtest(self):
        # Execute the speedtest command
        result = subprocess.run(['speedtest-cli', '--simple'], capture_output=True, text=True)
        output = result.stdout.strip()

        # Update the result label with the test results
        self.root.after(0, self.update_result, output)

    def update_result(self, output):
        self.result_label.config(text=output)
        self.start_button.config(state="normal")

def main():
    root = tk.Tk()
    app = SpeedTestApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
