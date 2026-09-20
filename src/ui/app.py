"""
The Anime Scripter - Dark Monotone GUI
A modern desktop UI for AI video enhancement toolkit
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import os
import sys
import json
import logging
from pathlib import Path

# Configure customtkinter appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class TASGUI(ctk.CTk):
    """Main GUI Application for The Anime Scripter"""
    
    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.title("The Anime Scripter - AI Video Enhancement Toolkit")
        self.geometry("1200x800")
        self.minsize(1000, 700)
        
        # State variables
        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.is_processing = False
        self.process_thread = None
        self.glow_enabled = tk.BooleanVar(value=False)
        
        # Processing options
        self.interpolate_var = tk.BooleanVar(value=False)
        self.upscale_var = tk.BooleanVar(value=False)
        self.dedup_var = tk.BooleanVar(value=False)
        self.restore_var = tk.BooleanVar(value=False)
        self.depth_var = tk.BooleanVar(value=False)
        self.segment_var = tk.BooleanVar(value=False)
        self.stabilize_var = tk.BooleanVar(value=False)
        self.motion_blur_var = tk.BooleanVar(value=False)
        self.obj_detect_var = tk.BooleanVar(value=False)
        
        # Method selections
        self.interpolate_method = tk.StringVar(value="rife4.25")
        self.interpolate_factor = tk.DoubleVar(value=2.0)
        self.upscale_method = tk.StringVar(value="shufflecugan")
        self.upscale_factor = tk.IntVar(value=2)
        self.dedup_method = tk.StringVar(value="ssim")
        self.dedup_sens = tk.DoubleVar(value=35.0)
        self.restore_methods = tk.StringVar(value="anime1080fixer")
        self.depth_method = tk.StringVar(value="small_v2")
        self.segment_method = tk.StringVar(value="anime")
        self.stabilize_method = tk.StringVar(value="classic")
        self.moblur_method = tk.StringVar(value="rife4.25")
        self.moblur_strength = tk.StringVar(value="gaussian_sym")
        self.obj_detect_method = tk.StringVar(value="yolov9_small-directml")
        
        # Performance options
        self.decode_method = tk.StringVar(value="cpu")
        self.half_precision = tk.BooleanVar(value=True)
        self.compile_mode = tk.StringVar(value="default")
        
        # Preview options
        self.preview_var = tk.BooleanVar(value=False)
        self.preview_port = tk.IntVar(value=5000)
        
        # Build UI
        self._create_layout()
        self._apply_styles()
