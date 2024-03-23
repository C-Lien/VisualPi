import tkinter as tk
import math

class PiLineWindow:
    def __init__(self, root):
        self.root = root
        w_width = 1500
        w_height = 800
        self.canvas = tk.Canvas(root, width=w_width, height=w_height)
        self.canvas.pack()
        self.x, self.y = w_width // 2, w_height // 2  # Starting point in middle of canvas
        self.angle = 90  # Starting angle

        self.pi_digits = self.compute_pi()
        # next(self.pi_digits)  # Skip '3' before the decimal point

        self.update_line()

    def compute_pi(self):
        """ A generator function to compute digits of Pi.
        """
        q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
        while True:
            if 4*q+r-t < n*t:
                yield n
                q, r, t, k, n, l = (10 * q, 10 * (r - n * t), t, k,
                                    (10 * (3 * q + r)) // t - 10 * n, l)
            else:
                q, r, t, k, n, l = (q * k, (2 * q + r) * l, t * l, k + 1,
                                    (q * (7 * k + 2) + r * l) // (t * l), l + 2)

    def update_line(self):
        """ Draws line based on Pi digits.
        """
        digit = next(self.pi_digits)

        # digit = digit ^ 2
        # print(digit)

        self.angle += 90 if digit % 2 == 0 else -90

        radian_angle = math.radians(self.angle)
        self.x += math.cos(radian_angle) * 10
        self.y += math.sin(radian_angle) * 10

        self.canvas.create_line(self.x-10*math.cos(radian_angle),
                                self.y-10*math.sin(radian_angle),
                                self.x,
                                self.y)

        self.root.after(10, self.update_line)

root = tk.Tk()
root.title("VisualPi")
app = PiLineWindow(root)
root.mainloop()
