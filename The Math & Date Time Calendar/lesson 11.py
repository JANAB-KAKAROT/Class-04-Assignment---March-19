# 📅✨ The Math & DateTime Calendar — by Kako 💻
# Let's explore Python time, date, calendar, math, and some NaN magic 🧙

import time
import datetime
import calendar
import math
import numpy as np

# ⏱️ 1. Tick Intervals — Kitna time ho gaya?
tick = time.time()
print("⏰ Tick (Seconds since Epoch):", tick)

# 📍 2. Epoch — Start of Time (1 Jan 1970 se shuruaat hui thi bhai 😄)
epoch = datetime.datetime(1970, 1, 1)
print("📆 Epoch time:", epoch)

# 🔁 3. Epoch used in Python — Convert ticks to proper date
converted_time = datetime.datetime.fromtimestamp(tick)
print("📥 Converted Time from Epoch:", converted_time)

# 📸 4. Getting the Current Time — Abhi ka waqt kya hai?
now = datetime.datetime.now()
print("🕒 Current DateTime:", now)

# 🎨 5. Formatted Time — Zyada achi tarah dikhate hain
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("🗓️ Formatted Time:", formatted_now)

# 🗓️ 6. The Calendar — Poore mahine ka calendar chahiye?
year = 2025
month = 4
print(f"\n📅 Calendar for {month}/{year}:\n")
print(calendar.month(year, month))

# 🔢 7. Getting the Calendar for a Month — Already done upar 😎

# ⏳ 8. The Date Time — Khaas date banana ho toh
specific_date = datetime.datetime(2025, 4, 13, 1, 30, 29)
print("🎯 Specific DateTime:", specific_date)

# 🖌️ 9. strftime() Method — Sundar format mein convert karein
formatted_specific = specific_date.strftime("%A, %d %B %Y, %I:%M:%S %p")
print("🧾 Formatted Specific Date:", formatted_specific)

# 🧠 10. Python Math Module — Thoda hisaab kitaab bhi ho jaye
print("\n📚 Python Math Time:")
print("π (pi):", math.pi)
print("cos(0):", math.cos(0))
print("e^2:", math.exp(2))
print("log(10):", math.log(10))
print("√16:", math.sqrt(16))

# 😵‍💫 11. Working with NaN — Jab value hi nahi hai, NaN ban jaata hai
nan_val = float('nan')
print("\n❓ Is nan_val NaN? (math):", math.isnan(nan_val))

nan_val_np = np.nan
print("🤖 Is nan_val_np NaN? (numpy):", np.isnan(nan_val_np))

