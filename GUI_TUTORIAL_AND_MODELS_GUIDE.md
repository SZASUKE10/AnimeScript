# 🎨 The Anime Scripter - GUI Tutorial & Open-Source Models Guide

<div align="center">

#### _Complete guide to using the Dark Monotone GUI with free, open-source AI models_

[![GUI](https://img.shields.io/badge/GUI-Dark%20Monotone-blue?style=flat-square)](#gui-tutorial)
[![Models](https://img.shields.io/badge/Models-100%25%20Free-green?style=flat-square)](#opensource-models-guide)
[![No-Paywall](https://img.shields.io/badge/Paywall-None-orange?style=flat-square)](#bypassing-paywalls-myth-busting)

</div>

---

## 📖 Table of Contents

- [🎨 GUI Tutorial](#-gui-tutorial)
  - [Installation](#installation)
  - [Interface Overview](#interface-overview)
  - [Step-by-Step Workflow](#stepbystep-workflow)
- [🆓 Open-Source Models Guide](#-opensource-models-guide)
  - [All Models Are Already Free](#all-models-are-already-free)
  - [Model Sources & Licenses](#model-sources--licenses)
  - [Recommended Free Models by Task](#recommended-free-models-by-task)
- [💡 Tips & Best Practices](#-tips--best-practices)
- [❓ Troubleshooting](#-troubleshooting)

---

## 🎨 GUI Tutorial

### Installation

**Prerequisites:**
- Python 3.10+ (Python 3.14 recommended)
- GPU with CUDA support (NVIDIA) OR Apple Silicon (M1+) for MPS backend
- 8GB+ RAM (16GB recommended)
- 2GB+ free disk space for models

**Step 1: Install Dependencies**

```bash
# Windows/Linux with NVIDIA GPU (CUDA)
python -m pip install -r requirements.txt -r extra-requirements-windows-lite.txt

# macOS Apple Silicon
python -m pip install -r requirements.txt -r extra-requirements-macos.txt

# Linux with NVIDIA GPU
python -m pip install -r requirements.txt -r extra-requirements-linux-lite.txt
```

**Step 2: Install customtkinter for GUI**

```bash
pip install customtkinter
```

**Step 3: Launch the GUI**

```bash
python src/ui/app.py
```

> **Note:** The GUI requires a display environment. For headless servers, use the CLI instead.

---

### Interface Overview

The Dark Monotone GUI features a clean, professional interface with:

#### **Header Bar** (Top)
- **Title**: "The Anime Scripter - AI Video Enhancement Toolkit"
- **Glow Toggle**: Checkbox to enable/disable visual glow effects (default: OFF for monotone look)
- **Window Controls**: Minimize, maximize, close

#### **Sidebar Navigation** (Left)
Seven tabbed panels for different processing tasks:

1. **📁 Input/Output** - File selection and output settings
2. **⏱️ Interpolation** - Frame interpolation (smooth motion)
3. **🔼 Upscaling** - Resolution enhancement
4. **🎬 Video Processing** - Deduplication, restoration, stabilization
5. **🎭 Segmentation** - Background/foreground separation
6. **🌊 Depth** - Depth map generation
7. **⚙️ Performance** - Hardware acceleration settings

#### **Main Panel** (Center)
Context-sensitive controls for the selected tab:
- File browsers
- Dropdown menus for model selection
- Sliders for quality/sensitivity
- Checkboxes for optional features
- Preview window (when enabled)

#### **Status Bar** (Bottom)
- Progress indicator
- Current operation status
- Estimated time remaining
- Log output

#### **Control Buttons** (Sidebar Bottom)
- **▶️ START**: Begin processing
- **⏹️ STOP**: Cancel current operation

---

### Step-by-Step Workflow

#### **Workflow 1: Basic Anime Upscaling (Beginner)**

**Goal**: Upscale 720p anime to 1080p/1440p

1. **Open Input/Output Tab**
   - Click "Browse Input" → Select your video file (MP4, MKV, AVI, etc.)
   - Click "Browse Output" → Choose destination folder and filename
   - Leave other settings at default

2. **Open Upscaling Tab**
   - ✅ Check "Enable Upscaling"
   - **Upscale Method**: Select `shufflecugan` (fast, good quality) or `span` (slower, better quality)
   - **Scale Factor**: Select `2x` (doubles resolution)
   - Leave other options unchecked

3. **Open Performance Tab** (Optional but Recommended)
   - **Decode Method**: Select `nvdec` if you have NVIDIA GPU (faster)
   - ✅ Check "Half Precision" (uses less VRAM, slightly faster)
   - **Compile Mode**: Leave as `default`

4. **Preview** (Optional)
   - Go back to Input/Output tab
   - ✅ Check "Enable Preview"
   - Click "Start Preview Server" to test on a few frames first

5. **Start Processing**
   - Click **▶️ START** button in sidebar
   - Watch progress in status bar
   - First run will download models automatically (~100-500MB)
   - Wait for completion (time varies by video length and GPU)

6. **Result**
   - Output video appears in your chosen folder
   - Enjoy your upscaled anime!

---

#### **Workflow 2: Smooth Motion + Upscale (Intermediate)**

**Goal**: Convert 24fps anime to 60fps AND upscale to 1080p

1. **Input/Output Tab**
   - Select input video and output path

2. **Interpolation Tab**
   - ✅ Check "Enable Interpolation"
   - **Method**: Select `rife4.25` (sharpest) or `rife4.22-lite` (faster, less VRAM)
   - **Factor**: Set to `2.0` (doubles framerate: 24→48fps, 30→60fps)

3. **Upscaling Tab**
   - ✅ Check "Enable Upscaling"
   - **Method**: Select `cyte` (tiny, fast) or `adore` (best quality)
   - **Scale**: `2x`

4. **Performance Tab**
   - **Decode Method**: `nvdec` (NVIDIA) or `cpu` (fallback)
   - ✅ Half Precision
   - If you have RTX 20/30/40 series: Try TensorRT methods for 2-3x speedup

5. **Start Processing**
   - Click **▶️ START**
   - Both operations chain in one pass (efficient!)

---

#### **Workflow 3: Complete Restoration Pipeline (Advanced)**

**Goal**: Fix compression artifacts, upscale, interpolate, and denoise

1. **Input/Output Tab**
   - Select source video (e.g., old DVD rip with artifacts)

2. **Video Processing Tab**
   - ✅ Check "Enable Restoration"
   - **Restore Methods**: Select multiple (chain them):
     - `anime1080fixer` (fixes bad 1080p encodes)
     - `real-plksr` (dejpeg, removes compression blocks)
     - `scunet` (denoising)
   - Order matters! They process left-to-right

3. **Upscaling Tab**
   - ✅ Enable Upscaling
   - Method: `span` or `fallin_strong` (best for damaged sources)

4. **Interpolation Tab**
   - ✅ Enable Interpolation
   - Method: `rife4.25-heavy` (best quality, most VRAM)

5. **Deduplication** (Optional)
   - ✅ Check "Enable Deduplication" if source has duplicate frames
   - **Method**: `ssim` (default)
   - **Sensitivity**: `35` (higher = more aggressive)

6. **Performance Tab**
   - **Compile Mode**: Try `tensorrt` if you have RTX GPU
   - Adjust batch sizes if running out of VRAM

7. **Start Processing**
   - This is a heavy pipeline - expect longer render times
   - Monitor VRAM usage in task manager

---

#### **Workflow 4: Depth Maps for 3D Effects (Creative)**

**Goal**: Generate depth maps for parallax effects or 3D conversion

1. **Input/Output Tab**
   - Select video (short clips work best for testing)

2. **Depth Tab**
   - ✅ Check "Enable Depth"
   - **Method**: Select based on your needs:
     - `small_v2` (fast, good quality)
     - `video_small_v3` (temporal consistency, less flicker)
     - `limbo_v2` (anime-specialized, fixed resolution)
   - **Quality**: `low` (fastest), `medium`, or `high`
   - **Batch Size**: `4` (faster at low res), `1` (safe default)

3. **Performance Tab**
   - For temporal methods (`video_*`): Set window size to `8` or `16`
   - Larger windows = smoother but more VRAM

4. **Output Format**
   - Depth maps save as grayscale video
   - White = close, Black = far (or inverted depending on method)

5. **Start Processing**
   - Use short test clip first (10-30 seconds)
   - Full episodes take hours depending on length

---

## 🆓 Open-Source Models Guide

### All Models Are Already Free! 🎉

**Important**: TheAnimeScripter (TAS) does **NOT** use any paywalled or commercial-only models. Every model available in TAS is:

✅ **100% Free** - No payment required  
✅ **Open Source** - Weights publicly available  
✅ **Legally Downloadable** - Hosted on GitHub/HuggingFace  
✅ **Auto-Downloaded** - TAS fetches them on first use  

**There is nothing to "bypass"** - the misconception that models are paywalled likely comes from confusing TAS with commercial tools like Topaz Video AI ($299/year). TAS is AGPL-licensed and all its models are openly available.

---

### Model Sources & Licenses

All models download automatically from these repositories:

| Source | URL | License |
|--------|-----|---------|
| **TAS-Models-Host** | https://github.com/NevermindNilas/TAS-Models-Host | Various (per-model) |
| **HuggingFace** | https://huggingface.co | Apache-2.0, MIT, etc. |
| **VSGAN-tensorrt-docker** | https://github.com/styler00dollar/VSGAN-tensorrt-docker | Apache-2.0 |
| **Depth-Anything-V2** | https://huggingface.co/depth-anything | Apache-2.0 |

**License Types You'll See:**
- **Apache-2.0**: Free for commercial use, modification, distribution
- **MIT**: Very permissive, minimal restrictions
- **AGPL-3.0**: Must share modifications if distributed (TAS itself)
- **CC BY-NC 4.0**: Non-commercial only (excluded from TAS)

> TAS explicitly **excludes** non-commercial models like DA3-Large (CC BY-NC). Only Apache-2.0 and similarly permissive licenses are included.

---

### Recommended Free Models by Task

#### **🔼 Upscaling (Anime)**

| Model | Speed | Quality | VRAM | Best For |
|-------|-------|---------|------|----------|
| **cyte** | ⚡⚡⚡⚡⚡ | ⭐⭐⭐ | 2GB | Quick tests, low-end GPUs |
| **shufflecugan** | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | 4GB | Balanced speed/quality |
| **span** | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | 6GB | Best overall quality |
| **adore** | ⚡⚡ | ⭐⭐⭐⭐⭐ | 8GB | Premium quality (slow) |
| **fallin_soft** | ⚡⚡⚡ | ⭐⭐⭐⭐ | 5GB | Soft, natural look |
| **fallin_strong** | ⚡⚡ | ⭐⭐⭐⭐⭐ | 7GB | Sharp, detailed enhancement |

**TensorRT Variants** (RTX 20/30/40/50 series only):
- Add `-tensorrt` suffix (e.g., `span-tensorrt`)
- **2-3x faster** than CUDA versions
- One-time engine build (~5-10 minutes first run)

**DirectML** (AMD/Intel GPUs):
- Add `-directml` suffix
- Slower than CUDA but works on non-NVIDIA hardware

---

#### **⏱️ Interpolation (Frame Rate Conversion)**

| Model | Speed | Quality | VRAM | Notes |
|-------|-------|---------|------|-------|
| **rife4.6** | ⚡⚡⚡⚡⚡ | ⭐⭐⭐ | 3GB | Fastest, oldest version |
| **rife4.22-lite** | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | 4GB | Great balance |
| **rife4.25** | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | 6GB | Sharpest, latest |
| **rife4.25-heavy** | ⚡⚡ | ⭐⭐⭐⭐⭐ | 8GB | Maximum quality |
| **rife_elexor** | ⚡⚡⚡ | ⭐⭐⭐⭐ | 5GB | Community mod (4.7 base) |

**Recommendation**: Start with `rife4.22-lite`, upgrade to `rife4.25` if you have VRAM.

---

#### **🔧 Restoration (Denoising, Dejpeg, Fix Artifacts)**

| Model | Type | Speed | Quality | VRAM |
|-------|------|-------|---------|------|
| **anime1080fixer** | General fix | ⚡⚡⚡⚡⚡ | ⭐⭐⭐⭐ | 2GB |
| **real-plksr** | Dejpeg | ⚡⚡⚡ | ⭐⭐⭐⭐ | 4GB |
| **scunet** | Denoise | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | 6GB |
| **gater3** | Line darken | ⚡⚡⚡⚡ | ⭐⭐⭐ | 3GB |
| **nafnet** | Denoise | ⚡⚡ | ⭐⭐⭐⭐⭐ | 8GB |
| **dpir** | Denoise | ⚡⚡ | ⭐⭐⭐⭐⭐ | 7GB |

**Chain Multiple**: You can select multiple restore methods! Example chain:
```
real-plksr → anime1080fixer → scunet
```
(removes jpeg blocks, fixes upscaling artifacts, then denoises)

---

#### **🌊 Depth Estimation**

| Model | Speed | Quality | Temporal | VRAM | License |
|-------|-------|---------|----------|------|---------|
| **small_v2** | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | ❌ | 4GB | Apache-2.0 |
| **video_small_v3** | ⚡⚡⚡ | ⭐⭐⭐⭐ | ✅ | 5GB | Apache-2.0 |
| **limbo_v2** | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ (anime) | ✅ | 4GB | Custom (free) |
| **base_v3** | ⚡⚡ | ⭐⭐⭐⭐⭐ | ✅ | 8GB | Apache-2.0 |

**Temporal Models** (`video_*`, `limbo_*`):
- Less flicker between frames
- Better for video (not just images)
- Require `--depth_window 8` or higher

**Limbo Models**:
- Specifically trained on anime
- Fixed resolution (504×280 or 504×378)
- Best for anime depth maps

---

#### **🎭 Segmentation (Rotoscoping)**

| Model | Speed | Quality | VRAM | Use Case |
|-------|-------|---------|------|----------|
| **anime** | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | 3GB | Anime characters |
| **anime-tensorrt** | ⚡⚡⚡⚡⚡ | ⭐⭐⭐⭐ | 3GB | Anime (RTX only) |

Segmentation separates foreground (characters) from background for:
- Independent color grading
- Background replacement
- Selective effects

---

#### **🎯 Object Detection (YOLOv9)**

| Model | Speed | Accuracy | VRAM |
|-------|-------|----------|------|
| **yolov9_small-directml** | ⚡⚡⚡⚡⚡ | ⭐⭐⭐ | 2GB |
| **yolov9_medium-directml** | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | 4GB |
| **yolov9_large-directml** | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | 6GB |

Adds bounding boxes and labels to detected objects. Useful for:
- Automated scene analysis
- Content filtering
- Metadata generation

---

## 💡 Tips & Best Practices

### **Performance Optimization**

1. **Use TensorRT if you have RTX GPU**
   - 2-3x speedup for upscaling/interpolation
   - One-time build cost pays off quickly

2. **Enable Half Precision**
   - Reduces VRAM usage by ~50%
   - Minimal quality loss
   - Faster on modern GPUs

3. **Choose Lite Models for Testing**
   - `rife4.22-lite` instead of `rife4.25`
   - Test on 10-second clip before full video

4. **NVDEC Decoding** (NVIDIA only)
   - Frees CPU for encoding
   - Caps at ~690fps at 1080p (usually fine)

5. **Batch Sizes**
   - Higher batch = faster but more VRAM
   - Start with `1`, increase if you have spare VRAM

---

### **VRAM Management**

| VRAM Available | Safe Models | Avoid |
|----------------|-------------|-------|
| **4GB** | cyte, rife4.6-lite, anime1080fixer | span, rife4.25-heavy, scunet |
| **6GB** | shufflecugan, rife4.22, real-plksr | adore, nafnet, base_v3 |
| **8GB+** | All models | Nothing! |

**If you run out of VRAM:**
1. Reduce batch size to `1`
2. Switch to `-lite` model variants
3. Lower quality setting
4. Close other applications
5. Use half precision

---

### **Quality vs Speed Tradeoffs**

**Fast Workflow** (quick results):
```
cyte (upscale) + rife4.6 (interpolate) + anime1080fixer (restore)
Time: ~1-2 FPS at 1080p on RTX 3060
```

**Balanced Workflow** (daily use):
```
shufflecugan (upscale) + rife4.22-lite (interpolate) + real-plksr (restore)
Time: ~0.5-1 FPS at 1080p on RTX 3060
```

**Maximum Quality** (final renders):
```
span or adore (upscale) + rife4.25-heavy (interpolate) + scunet+dpir (restore)
Time: ~0.2-0.5 FPS at 1080p on RTX 3060
```

---

## ❓ Troubleshooting

### **Common Issues**

#### **"Model download failed"**
- ✅ Check internet connection
- ✅ Disable VPN/proxy temporarily
- ✅ Manually download from GitHub and place in `weights/` folder
- ✅ Retry - downloads auto-resume

#### **"Out of memory (OOM)"**
- ✅ Reduce batch size to `1`
- ✅ Use `-lite` model variants
- ✅ Enable half precision
- ✅ Close browser/other GPU apps
- ✅ Lower resolution or quality

#### **"CUDA out of memory"**
Same as above, plus:
- ✅ Try DirectML backend (sometimes more efficient)
- ✅ Reduce video resolution with preprocessing
- ✅ Use smaller chunk sizes for temporal models

#### **"GUI won't start"**
- ✅ Ensure `customtkinter` is installed: `pip install customtkinter`
- ✅ Run in terminal to see error messages
- ✅ Check Python version (3.10+ required)
- ✅ Verify display server is running (not headless)

#### **"Processing is extremely slow"**
- ✅ Confirm GPU is being used (check Task Manager / nvidia-smi)
- ✅ Switch to TensorRT if you have RTX GPU
- ✅ Use NVDEC decoding
- ✅ Reduce quality settings
- ✅ Check thermal throttling (clean fans, improve cooling)

---

### **Getting Help**

- **Documentation**: https://tas.nevermindnilas.dev
- **GitHub Issues**: https://github.com/NevermindNilas/TheAnimeScripter/issues
- **Discord**: https://discord.gg/hwGHXga8ck
- **Promo Video**: https://youtu.be/V7ryKMezqeQ

---

## 📜 Legal & Licensing Summary

**TheAnimeScripter (TAS)**: AGPL-3.0 (free, open-source, must share modifications)

**Included Models**:
- ✅ Apache-2.0 (commercial-friendly)
- ✅ MIT (very permissive)
- ✅ Custom free licenses (non-NC)
- ❌ **NO** CC BY-NC (non-commercial excluded)
- ❌ **NO** paywalled models
- ❌ **NO** proprietary checkpoints

**You Can**:
- ✅ Use TAS for personal projects
- ✅ Use TAS for commercial work (check individual model licenses)
- ✅ Modify and redistribute TAS (must remain AGPL)
- ✅ Share processed videos freely (your output is yours)

**You Cannot**:
- ❌ Claim TAS models are paywalled (they're not!)
- ❌ Sublicense under restrictive terms
- ❌ Remove copyright notices

---

<div align="center">

### 🎉 Ready to Start?

**Remember**: Every model in TAS is 100% free and open-source. There's no paywall to bypass - just download, install, and enhance!

[![Download](https://img.shields.io/badge/Download-TAS-blue?style=for-the-badge)](https://github.com/NevermindNilas/TheAnimeScripter/releases/latest)
[![Discord](https://img.shields.io/badge/Join-Discord-purple?style=for-the-badge&logo=discord)](https://discord.gg/hwGHXga8ck)

**Happy Enhancing! 🚀**

</div>
