# 🪟 WINDOWS SETUP GUIDE

This guide walks Windows users through setting up and running the Maze Game for the first time.

---

## Step 1: Download Python (if you don't have it)

1. Go to https://www.python.org/downloads/
2. Click the **yellow "Download Python"** button (get version 3.10 or newer)
3. Run the installer
4. **IMPORTANT:** Check the box that says **"Add Python to PATH"**
5. Click "Install Now"

---

## Step 2: Verify Python is Installed

1. Press **Windows Key + R**
2. Type `cmd` and press Enter (this opens Command Prompt)
3. Type this and press Enter:
   ```
   python --version
   ```
4. You should see something like: `Python 3.10.5`

If you get an error, go back to Step 1 and make sure you checked "Add Python to PATH"

---

## Step 3: Download the Game Files

1. Download the maze-game files (your teacher will provide these)
2. Create a new folder on your Desktop called `maze-game`
3. Put all the game files in that folder:
   - `main.py`
   - `config.py`
   - `entities.py`
   - `game.py`
   - `renderer.py`
   - `requirements.txt`
   - `README.md`

---

## Step 4: Install Pygame (One Time Only)

1. Press **Windows Key + R**
2. Type `cmd` and press Enter
3. Copy and paste this command:
   ```
   pip install pygame
   ```
4. Press Enter and wait for it to finish (you'll see "Successfully installed pygame")

**That's it!** You only need to do this once per computer.

---

## Step 5: Run the Game

1. Press **Windows Key + R**
2. Type `cmd` and press Enter
3. Type this command to go to your game folder:
   ```
   cd Desktop\maze-game
   ```
4. Type this to run the game:
   ```
   python main.py
   ```
5. The game window should open! 🎮

---

## Step 6: Playing the Game

- Use **Arrow Keys** to move
- Collect all the **gold coins**
- Avoid the **colored enemies**
- **Close the window** to exit

---

## Running the Game Later

Every time you want to play:

1. Press **Windows Key + R**
2. Type `cmd`
3. Type: `cd Desktop\maze-game`
4. Type: `python main.py`

---

## Customizing in VS Code

1. Open **VS Code**
2. Click **File → Open Folder**
3. Select your `maze-game` folder
4. Click on `config.py` to edit colors and game settings
5. Make changes and save (Ctrl + S)
6. Run the game to see your changes!

---

## Common Problems & Solutions

### Problem: `python command not found`

**Solution:** You need to install Python. Go back to Step 1.

### Problem: `No module named 'pygame'`

**Solution:** You skipped Step 4. Run:
```
pip install pygame
```

### Problem: Can't find the maze-game folder in Command Prompt

**Solution:** Make sure you use the correct path. If your folder is on Desktop:
```
cd Desktop\maze-game
```

Or if it's in Documents:
```
cd Documents\maze-game
```

### Problem: Game runs but I see a black window

**Solution:** Try waiting 5 seconds. If nothing appears:
1. Close the window
2. Make sure all 6 files are in the same folder
3. Try again

---

## Need Help?

- Check the `README.md` file for more detailed info
- Ask your teacher or classmates
- Search for the error message in Google
- Try printing messages with `print()` to debug

---

**You're ready to go! Good luck! 🎮✨**
