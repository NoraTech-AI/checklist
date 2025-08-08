# Automation venv
import os
import subprocess
import sys

# لیست پکیج‌هایی که میخوای پیش‌فرض نصب بشن
DEFAULT_PACKAGES = ["requests", "numpy"]

def create_venv():
    if not os.path.exists("venv"):
        print("📦 Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", "venv"])
    else:
        print("✅ Virtual environment already exists.")

def activate_venv():
    if os.name == "nt":  # ویندوز
        activate_script = r"venv\Scripts\activate"
    else:  # لینوکس / مک
        activate_script = "source venv/bin/activate"
    print(f"⚡ To activate venv run: {activate_script}")

def install_packages(packages):
    print(f"📦 Installing packages: {', '.join(packages)}")
    subprocess.run(["venv/bin/pip", "install"] + packages)
    subprocess.run(["venv/bin/pip", "freeze"], stdout=open("requirements.txt", "w"))
    print("✅ Packages installed and requirements.txt created.")

if __name__ == "__main__":
    create_venv()
    activate_venv()
    install_packages(DEFAULT_PACKAGES)
    print("🎯 Setup complete!")
