# 🔧 Why Your EXE Isn't Showing in Releases (And How to Fix It)

## ❌ The Problem

You created a release but no EXE appeared. This happens because:

1. **GitHub Actions needs time** - Builds take 5-15 minutes depending on queue
2. **Draft releases don't trigger builds** - Only **published** releases trigger the workflow
3. **Workflow might have errors** - Check the Actions tab for failures

---

## ✅ Step-by-Step Solution

### Step 1: Verify Your Release is PUBLISHED (Not Draft)

1. Go to your GitHub repo → **Releases**
2. If you see "Draft" next to your release:
   - Click **"Edit"**
   - Scroll down and click **"Publish release"** (green button)
   - ⚠️ **Important**: "Save draft" does NOT trigger the build!

### Step 2: Check if the Workflow Started

1. Go to your GitHub repo → **Actions** tab
2. Look for **"Build Executables"** workflow
3. You should see a run with your release tag (e.g., `v1.0.0`)
4. Status should be:
   - 🟡 **Yellow** = Running (wait 5-15 minutes)
   - 🟢 **Green** = Success (EXE should be attached)
   - 🔴 **Red** = Failed (click to see error)

### Step 3: If Workflow Failed

Click the failed workflow run and check the error. Common issues:

#### Issue A: `src/ui/app.py` not found
```
Error: File src/ui/app.py not found
```
**Fix**: Make sure the UI file exists at exactly `src/ui/app.py` in your repo.

#### Issue B: PyInstaller import errors
```
ImportError: No module named 'tkinter'
```
**Fix**: Already fixed in the workflow - I added `--hidden-import` flags. Delete the old release and create a new one.

#### Issue C: Upload permission error
```
Error: Resource not accessible by integration
```
**Fix**: Go to repo **Settings** → **Actions** → **General** → Ensure "Read and write permissions" is enabled for workflows.

### Step 4: Create a Fresh Release (If Needed)

If your current release is stuck:

1. Go to **Releases**
2. Delete the problematic release (don't worry, tags stay)
3. Create a new release:
   ```
   Tag: v1.0.1 (increment version)
   Title: TAS GUI v1.0.1
   Description: Fixed build issues
   ```
4. **Click "Publish release"** immediately (not "Save draft")

---

## 🕐 Expected Timeline

| Step | Time |
|------|------|
| Release published → Workflow starts | 30-60 seconds |
| Windows build | 3-5 minutes |
| macOS build | 4-7 minutes |
| Linux build | 2-4 minutes |
| Upload to release | 1-2 minutes |
| **Total** | **8-15 minutes** |

---

## 🎯 Quick Checklist

Before creating a release, verify:

- [ ] `src/ui/app.py` exists in your repository
- [ ] You're using tag format `v1.0.0` (with 'v' prefix)
- [ ] You click **"Publish release"** not "Save draft"
- [ ] Repository has Actions enabled (Settings → Actions)
- [ ] Workflow permissions are set to Read/Write

---

## 📍 Where to Find the EXE After Build

Once the workflow succeeds (green checkmark):

1. Go to **Releases**
2. Click your release tag (e.g., `v1.0.0`)
3. Scroll to **"Assets"** section at the bottom
4. Download:
   - `TAS_GUI_Windows.exe` (Windows)
   - `TAS_GUI_MacOS.zip` (macOS)
   - `TAS_GUI_Linux.zip` (Linux)

---

## 🆘 Still Not Working?

### Manual Build Alternative

If GitHub Actions keeps failing, build locally:

**Windows:**
```bash
cd /workspace
pip install pyinstaller customtkinter packaging pillow numpy opencv-python-headless
pyinstaller --noconfirm --onefile --windowed --name "TAS_GUI" --add-data "src/ui;src/ui" --hidden-import=tkinter --hidden-import=PIL src/ui/app.py
```

Your EXE will be in `dist/TAS_GUI.exe` - upload it manually to your release!

**macOS/Linux:**
```bash
cd /workspace
pip install pyinstaller customtkinter packaging pillow numpy opencv-python-headless
pyinstaller --noconfirm --onefile --windowed --name "TAS_GUI" --add-data "src/ui:src/ui" --hidden-import=tkinter --hidden-import=PIL src/ui/app.py
zip -rj TAS_GUI.zip dist/TAS_GUI.app  # macOS
# or
zip -j TAS_GUI.zip dist/TAS_GUI  # Linux
```

---

## 💡 Pro Tips

1. **Test with a draft first**: Create a draft release, then check Actions tab to ensure workflow is configured correctly before publishing
2. **Watch the build**: Keep the Actions tab open to see real-time progress
3. **Check logs**: If it fails, expand each step to see detailed error messages
4. **Version tags matter**: Use semantic versioning (`v1.0.0`, `v1.0.1`, etc.)

---

## 📞 Need More Help?

If you're still stuck, reply with:
1. Screenshot of your Releases page
2. Screenshot of the Actions tab showing the workflow status
3. Any error messages from the workflow logs

I'll help you debug the specific issue!
