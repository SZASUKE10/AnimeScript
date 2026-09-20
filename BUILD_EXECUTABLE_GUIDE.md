# 🚀 How to Create and Publish Executables

This guide explains how to turn the TAS GUI into a standalone `.exe` (Windows), `.app` (macOS), or binary (Linux) and publish it to your GitHub Releases.

---

## 📦 Option A: Automatic Builds via GitHub Actions (Recommended)

I've already created a GitHub Actions workflow for you! Here's how to use it:

### Step 1: Create a Release on GitHub
1. Go to your repository on GitHub
2. Click **"Releases"** in the right sidebar
3. Click **"Draft a new release"**
4. Fill in:
   - **Tag version**: `v1.0.0` (or whatever version you want)
   - **Release title**: `TAS GUI v1.0.0`
   - **Description**: Add release notes
5. Click **"Publish release"** (NOT "Save draft")

### Step 2: Wait for Automatic Build
- GitHub Actions will automatically trigger the build workflow
- Go to **Actions** tab → Click **"Build Executables"** workflow
- Wait ~5-10 minutes for all three builds (Windows, macOS, Linux)

### Step 3: Download Your Executables
Once the workflow completes:
- Return to your **Releases** page
- You'll see three files attached:
  - `TAS_GUI_Windows.exe` - For Windows users
  - `TAS_GUI_MacOS.zip` - For macOS users (contains .app)
  - `TAS_GUI_Linux.zip` - For Linux users (contains binary)

✅ **Done!** Users can now download and run without installing Python.

---

## 💻 Option B: Manual Build (Local Machine)

If you prefer to build locally:

### Prerequisites
```bash
pip install pyinstaller customtkinter packaging pillow numpy opencv-python-headless
```

### Windows
```bash
cd /workspace
pyinstaller --noconfirm --onefile --windowed --name "TAS_GUI" --add-data "src/ui;src/ui" src/ui/app.py
```
Output: `dist/TAS_GUI.exe`

### macOS
```bash
cd /workspace
pyinstaller --noconfirm --onefile --windowed --name "TAS_GUI" --add-data "src/ui:src/ui" src/ui/app.py
zip -r TAS_GUI_MacOS.zip dist/TAS_GUI.app
```
Output: `TAS_GUI_MacOS.zip`

### Linux
```bash
cd /workspace
pyinstaller --noconfirm --onefile --windowed --name "TAS_GUI" --add-data "src/ui:src/ui" src/ui/app.py
zip -j TAS_GUI_Linux.zip dist/TAS_GUI
```
Output: `TAS_GUI_Linux.zip`

### Upload to Releases Manually
1. Go to **Releases** → **Draft a new release**
2. Fill in version info
3. Drag and drop your `.exe` or `.zip` files into the "Attach binaries" section
4. Click **Publish release**

---

## ⚠️ Important Notes

### File Size
- The executable will be **~150-300 MB** because it bundles Python + all dependencies
- This is normal and expected
- Models are NOT included (they download on first use to keep size small)

### Antivirus False Positives
- PyInstaller executables sometimes trigger antivirus warnings
- This is a false positive (common with Python apps)
- Users may need to add an exception or download from trusted source

### First Run Behavior
- On first launch, the app will create necessary folders
- Models download automatically when first selected (from free sources)
- No internet = no model downloads, but app still opens

### Platform Specifics
- **Windows**: `.exe` runs directly, may show SmartScreen warning (click "More info" → "Run anyway")
- **macOS**: May show "App can't be opened" → Right-click → Open → Confirm
- **Linux**: May need `chmod +x TAS_GUI` before running

---

## 🔧 Troubleshooting

### Build Fails with "Module not found"
```bash
pip install --upgrade pyinstaller customtkinter
```

### Executable Crashes Immediately
- Check if all dependencies are installed before building
- Try building with `--debug=all` flag to see errors
- Ensure you're building on the same platform you're deploying to

### GitHub Actions Workflow Doesn't Trigger
- Make sure you clicked **"Publish release"** not "Save draft"
- Check **Settings** → **Actions** → Enable workflows if disabled
- Verify `.github/workflows/build_executables.yml` exists

---

## 📝 What Users Need to Know

Include this in your release notes:

```markdown
## Downloads
- **Windows**: Download `TAS_GUI_Windows.exe` and run directly
- **macOS**: Download `TAS_GUI_MacOS.zip`, extract, and open `TAS_GUI.app`
- **Linux**: Download `TAS_GUI_Linux.zip`, extract, run `./TAS_GUI`

## Requirements
- No Python installation needed!
- Internet connection required for first-time model downloads
- NVIDIA GPU recommended for best performance (AMD/Intel supported)

## First Launch
- App will create config folder in your user directory
- Models download automatically when selected (free, no paywall)
- Expect 100MB-2GB model downloads depending on features used
```

---

## ✅ Checklist Before Publishing

- [ ] Test the executable on a clean machine (without Python installed)
- [ ] Verify all UI features work correctly
- [ ] Confirm models download properly on first use
- [ ] Check file size is reasonable (<500MB ideal)
- [ ] Write clear release notes with usage instructions
- [ ] Tag version appropriately (semantic versioning: `vMAJOR.MINOR.PATCH`)

---

**Need help?** Check the GitHub Actions logs if builds fail, or test locally first before publishing.
