import os
import datetime

# 1️⃣ مسیر لاگ‌ها
log_dir = "/tmp/devops_logs"
log_file = os.path.join(log_dir, "system_check.log")

# 2️⃣ بررسی وجود دایرکتوری، در غیر این صورت ساخت
if not os.path.exists(log_dir):
    os.makedirs(log_dir, exist_ok=True)
    print(f"[INFO] مسیر {log_dir} ساخته شد.")
else:
    print(f"[INFO] مسیر {log_dir} از قبل وجود دارد.")

# 3️⃣ تابعی برای نوشتن در لاگ
def write_log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[LOG] {message}")

# 4️⃣ اجرای دستور سیستمی و ثبت خروجی
def run_command(cmd):
    print(f"[RUN] اجرای دستور: {cmd}")
    exit_code = os.system(cmd)
    status = "موفق" if exit_code == 0 else f"ناموفق (exit code: {exit_code})"
    write_log(f"Command: {cmd} → Status: {status}")

# 5️⃣ استفاده از توابع بالا
write_log("شروع عملیات چک سیستم")
run_command("ls -l /etc")
run_command("ping -c 1 google.com")
write_log("پایان عملیات چک سیستم")

print(f"[INFO] همه‌ی لاگ‌ها در {log_file} ذخیره شدند.")
