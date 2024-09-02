
import tkinter as tk
from tkinter import messagebox
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
import threading


class TrayApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tkinter App")
        self.root.geometry("300x200")
        
        self.root.protocol("WM_DELETE_WINDOW", self.minimize_to_tray)
        
        label = tk.Label(self.root, text="Hello! Minimize me to tray.")
        label.pack(pady=20)

        show_button = tk.Button(self.root, text="Show Message", command=self.show_message)
        show_button.pack(pady=10)

        # To keep the icon accessible from the system tray
        self.icon_thread = threading.Thread(target=self.create_tray_icon)
        self.icon_thread.start()

    def show_message(self):
        messagebox.showinfo("Information", "This is a Tkinter app minimized to tray!")

    def minimize_to_tray(self):
        self.root.withdraw()  # Hide the window

    def restore_window(self, icon, item):
        print(threading.current_thread().name)
        self.root.deiconify()  # Restore the window

    def quit_app(self, icon, item):
        icon.stop()
        self.root.quit()

    def create_image(self, width, height, color1, color2):
        # Create an image with a simple drawing (a red dot)
        image = Image.new('RGB', (width, height), color1)
        dc = ImageDraw.Draw(image)
        dc.ellipse((width // 4, height // 4, 3 * width // 4, 3 * height // 4), fill=color2)
        return image

    def create_tray_icon(self):
        image = self.create_image(64, 64, 'black', 'red')
        menu = Menu(
            MenuItem('Restore', self.restore_window),
            MenuItem('Quit', self.quit_app)
        )
        icon = Icon("TkinterApp", image, "TkinterApp", menu)
        icon.run()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = TrayApp()
    app.run()
