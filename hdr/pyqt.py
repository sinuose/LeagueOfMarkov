from hdr.lolapi import *

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont, QPainter, QColor
from PyQt5.QtCore import Qt, QTimer

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Overlay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.showFullScreen()

        # Main Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Overlay Text
        self.label = QLabel("League Overlay - Loading...", self)
        self.label.setStyleSheet("color: white; font-size: 28px; font-weight: bold;")
        self.label.setFont(QFont("Arial", 24))
        self.label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        layout.addWidget(self.label)

        # Mini-map Plot (Positioned on Bottom-Right Corner)
        self.plot_canvas = LivePlot()
        self.plot_canvas.setFixedSize(400, 400)  # Mini-map size
        layout.addWidget(self.plot_canvas)

        # # Timer for Real-Time Updates
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.update_stats)
        # self.timer.start(1000)  # Update every second


class LivePlot(FigureCanvas):
    """A Matplotlib figure integrated into PyQt5 for real-time mini-map plotting."""
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.setStyleSheet("background:transparent;")
        self.ax.set_facecolor((0, 0, 0, 0))  # Fully transparent background
        self.ax.set_xlim(0, 15000)  # Map X range (game units)
        self.ax.set_ylim(0, 15000)  # Map Y range (game units)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_frame_on(False)
        self.scatter = self.ax.scatter([], [])  # Empty scatter plot for live updates

    def update_plot(self, positions):
        """Updates the mini-map plot with real-time positions."""
        x, y = zip(*positions) if positions else ([], [])
        self.scatter.set_offsets(np.column_stack([x, y]))
        self.draw()