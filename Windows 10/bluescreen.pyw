import tkinter as tk
from tkinter import messagebox
import random
from PIL import ImageTk, Image
import time
from os import system
import psutil
from sys import platform


if platform == "win32":
    system("title Administrator: Command Prompt")
    system("ver")
    print("(c) Microsoft Corporation. All rights reserved.")
    print("C:\\Windows\\System32>taskkill /f /im svchost.exe /t")

    mainsvc = str(random.randint(100, 1000))
    for proc in psutil.process_iter():
      try:
          processName = proc.name()
          processID = proc.pid
          if processName == "svchost.exe":
            print(f"The process with the PID of {processID} (child process of PID {mainsvc}) has been terminated")
      except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
          pass


root = tk.Tk()
codes = ["CRITICAL PROCESS DIED", "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED", "IRQL_NOT_LESS_OR_EQUAL", "VIDEO_TDR_TIMEOUT_DETECTED", "PAGE_FAULT_IN_NONPAGED_AREA", "SYSTEM_SERVICE_EXCEPTION", "DPC_WATCHDOG_VIOLATION"]
root.withdraw()
try:
  qr = ImageTk.PhotoImage(file="./Etc/qr.png")
except Exception:
  pass
root.deiconify()
root.title("Bluescreen of Death")
root.wm_attributes('-fullscreen','true')
try:
  ico = Image.open('./Etc/logo.png')
  photo = ImageTk.PhotoImage(ico)
  root.wm_iconphoto(False, photo)
except Exception:
  pass
c = tk.Canvas(root, width = root.winfo_screenwidth(),
height = root.winfo_screenheight(), bg= "#129ae3", highlightthickness=0)
root.lift()
root.attributes("-topmost", True)
root.configure(background="#129ae3")
c.pack()
c.create_text(100, 150, anchor="w", fill="white", font="Ebrima 100", text=":(")
c.create_text(100, 300, anchor="w", fill="white", font="Ebrima 15", text="Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you")
loader = c.create_text(100, 350, anchor = "w", fill="white", font="Ebrima 15", text="0 % complete")
try:
  c.create_image(150, 425, image=qr)
except Exception:
  pass
c.create_text(210, 400, anchor = "w", fill="white", font="Ebrima 10", text="For more information about this issue and possible fixes, visit https://www.windows.com/stopcode")
c.create_text(210, 425, anchor="w", font="Ebrima 10", fill="white", text="If you call a support person, give them this info:")
c.create_text(210, 450, anchor="w", font="Embrima 10", fill="white", text=f"Stop code: {random.choice(codes)}")


def long():
  root.after(random.randint(100000, 200000), lambda : c.itemconfig(loader, text="1% complete"))
  root.after(random.randint(210000, 300000), lambda : c.itemconfig(loader, text="2% complete"))
  root.after(random.randint(310000, 400000), lambda: c.itemconfig(loader, text="3% complete"))
  root.after(random.randint(410000, 500000), lambda: c.itemconfig(loader, text="4% complete"))
  root.after(random.randint(510000, 600000), lambda: c.itemconfig(loader, text="5% complete"))
  root.after(random.randint(610000, 700000), lambda: c.itemconfig(loader, text="6% complete"))
  root.after(random.randint(710000, 800000), lambda: c.itemconfig(loader, text="7% complete"))
  root.after(random.randint(810000, 900000), lambda: c.itemconfig(loader, text="8% complete"))
  root.after(random.randint(910000, 1000000), lambda: c.itemconfig(loader, text="9% complete"))
  root.after(random.randint(1010000, 1100000), lambda: c.itemconfig(loader, text="10% complete"))
  root.after(random.randint(1110000, 1200000), lambda: c.itemconfig(loader, text="11% complete"))
  root.after(random.randint(1210000, 1300000), lambda: c.itemconfig(loader, text="12% complete"))
  root.after(random.randint(1310000, 1400000), lambda: c.itemconfig(loader, text="13% complete"))
  root.after(random.randint(1410000, 1500000), lambda: c.itemconfig(loader, text="14% complete"))
  root.after(random.randint(1510000, 1600000), lambda: c.itemconfig(loader, text="15% complete"))
  root.after(random.randint(1610000, 1700000), lambda: c.itemconfig(loader, text="16% complete"))
  root.after(random.randint(1710000, 1800000), lambda: c.itemconfig(loader, text="17% complete"))
  root.after(random.randint(1810000, 1900000), lambda: c.itemconfig(loader, text="18% complete"))
  root.after(random.randint(1910000, 2000000), lambda: c.itemconfig(loader, text="19% complete"))
  root.after(random.randint(2010000, 2100000), lambda: c.itemconfig(loader, text="20% complete"))
  root.after(random.randint(2110000, 2200000), lambda: c.itemconfig(loader, text="21% complete"))
  root.after(random.randint(2210000, 2300000), lambda: c.itemconfig(loader, text="22% complete"))
  root.after(random.randint(2310000, 2400000), lambda: c.itemconfig(loader, text="23% complete"))
  root.after(random.randint(2410000, 2500000), lambda: c.itemconfig(loader, text="24% complete"))
  root.after(random.randint(2510000, 2600000), lambda: c.itemconfig(loader, text="25% complete"))
  root.after(random.randint(2610000, 2700000), lambda: c.itemconfig(loader, text="26% complete"))
  root.after(random.randint(2710000, 2800000), lambda: c.itemconfig(loader, text="27% complete"))
  root.after(random.randint(2810000, 2900000), lambda: c.itemconfig(loader, text="28% complete"))
  root.after(random.randint(2910000, 3000000), lambda: c.itemconfig(loader, text="29% complete"))
  root.after(random.randint(3010000, 3100000), lambda: c.itemconfig(loader, text="30% complete"))
  root.after(random.randint(3110000, 3200000), lambda: c.itemconfig(loader, text="31% complete"))
  root.after(random.randint(3210000, 3300000), lambda: c.itemconfig(loader, text="32% complete"))
  root.after(random.randint(3310000, 3400000), lambda: c.itemconfig(loader, text="33% complete"))
  root.after(random.randint(3410000, 3500000), lambda: c.itemconfig(loader, text="34% complete"))
  root.after(random.randint(3510000, 3600000), lambda: c.itemconfig(loader, text="35% complete"))
  root.after(random.randint(3610000, 3700000), lambda: c.itemconfig(loader, text="36% complete"))
  root.after(random.randint(3710000, 3800000), lambda: c.itemconfig(loader, text="37% complete"))
  root.after(random.randint(3810000, 3900000), lambda: c.itemconfig(loader, text="38% complete"))
  root.after(random.randint(3910000, 4000000), lambda: c.itemconfig(loader, text="39% complete"))
  root.after(random.randint(4010000, 4100000), lambda: c.itemconfig(loader, text="40% complete"))
  root.after(random.randint(4110000, 4200000), lambda: c.itemconfig(loader, text="41% complete"))
  root.after(random.randint(4210000, 4300000), lambda: c.itemconfig(loader, text="42% complete"))
  root.after(random.randint(4310000, 4400000), lambda: c.itemconfig(loader, text="43% complete"))
  root.after(random.randint(4410000, 4500000), lambda: c.itemconfig(loader, text="44% complete"))
  root.after(random.randint(4510000, 4600000), lambda: c.itemconfig(loader, text="45% complete"))
  root.after(random.randint(4610000, 4700000), lambda: c.itemconfig(loader, text="46% complete"))
  root.after(random.randint(4710000, 4800000), lambda: c.itemconfig(loader, text="47% complete"))
  root.after(random.randint(4810000, 4900000), lambda: c.itemconfig(loader, text="48% complete"))
  root.after(random.randint(4910000, 5000000), lambda: c.itemconfig(loader, text="49% complete"))
  root.after(random.randint(5010000, 5100000), lambda: c.itemconfig(loader, text="50% complete"))
  root.after(random.randint(5110000, 5200000), lambda: c.itemconfig(loader, text="51% complete"))
  root.after(random.randint(5210000, 5300000), lambda: c.itemconfig(loader, text="52% complete"))
  root.after(random.randint(5310000, 5400000), lambda: c.itemconfig(loader, text="53% complete"))
  root.after(random.randint(5410000, 5500000), lambda: c.itemconfig(loader, text="54% complete"))
  root.after(random.randint(5510000, 5600000), lambda: c.itemconfig(loader, text="55% complete"))
  root.after(random.randint(5610000, 5700000), lambda: c.itemconfig(loader, text="56% complete"))
  root.after(random.randint(5710000, 5800000), lambda: c.itemconfig(loader, text="57% complete"))
  root.after(random.randint(5810000, 5900000), lambda: c.itemconfig(loader, text="58% complete"))
  root.after(random.randint(5910000, 6000000), lambda: c.itemconfig(loader, text="59% complete"))
  root.after(random.randint(6010000, 6100000), lambda: c.itemconfig(loader, text="60% complete"))
  root.after(random.randint(6110000, 6200000), lambda: c.itemconfig(loader, text="61% complete"))
  root.after(random.randint(6210000, 6300000), lambda: c.itemconfig(loader, text="62% complete"))
  root.after(random.randint(6310000, 6400000), lambda: c.itemconfig(loader, text="63% complete"))
  root.after(random.randint(6410000, 6500000), lambda: c.itemconfig(loader, text="64% complete"))
  root.after(random.randint(6510000, 6600000), lambda: c.itemconfig(loader, text="65% complete"))
  root.after(random.randint(6610000, 6700000), lambda: c.itemconfig(loader, text="66% complete"))
  root.after(random.randint(6710000, 6800000), lambda: c.itemconfig(loader, text="67% complete"))
  root.after(random.randint(6810000, 6900000), lambda: c.itemconfig(loader, text="68% complete"))
  root.after(random.randint(6910000, 7000000), lambda: c.itemconfig(loader, text="69% complete"))
  root.after(random.randint(7010000, 7100000), lambda: c.itemconfig(loader, text="70% complete"))
  root.after(random.randint(7110000, 7200000), lambda: c.itemconfig(loader, text="71% complete"))
  root.after(random.randint(7210000, 7300000), lambda: c.itemconfig(loader, text="72% complete"))
  root.after(random.randint(7310000, 7400000), lambda: c.itemconfig(loader, text="73% complete"))
  root.after(random.randint(7410000, 7500000), lambda: c.itemconfig(loader, text="74% complete"))
  root.after(random.randint(7510000, 7600000), lambda: c.itemconfig(loader, text="75% complete"))
  root.after(random.randint(7610000, 7700000), lambda: c.itemconfig(loader, text="76% complete"))
  root.after(random.randint(7710000, 7800000), lambda: c.itemconfig(loader, text="77% complete"))
  root.after(random.randint(7810000, 7900000), lambda: c.itemconfig(loader, text="78% complete"))
  root.after(random.randint(7910000, 8000000), lambda: c.itemconfig(loader, text="79% complete"))
  root.after(random.randint(8010000, 8100000), lambda: c.itemconfig(loader, text="80% complete"))
  root.after(random.randint(8110000, 8200000), lambda: c.itemconfig(loader, text="81% complete"))
  root.after(random.randint(8210000, 8300000), lambda: c.itemconfig(loader, text="82% complete"))
  root.after(random.randint(8310000, 8400000), lambda: c.itemconfig(loader, text="83% complete"))
  root.after(random.randint(8410000, 8500000), lambda: c.itemconfig(loader, text="84% complete"))
  root.after(random.randint(8510000, 8600000), lambda: c.itemconfig(loader, text="85% complete"))
  root.after(random.randint(8610000, 8700000), lambda: c.itemconfig(loader, text="86% complete"))
  root.after(random.randint(8710000, 8800000), lambda: c.itemconfig(loader, text="87% complete"))
  root.after(random.randint(8810000, 8900000), lambda: c.itemconfig(loader, text="88% complete"))
  root.after(random.randint(8910000, 9000000), lambda: c.itemconfig(loader, text="89% complete"))
  root.after(random.randint(9010000, 9100000), lambda: c.itemconfig(loader, text="90% complete"))
  root.after(random.randint(9110000, 9200000), lambda: c.itemconfig(loader, text="91% complete"))
  root.after(random.randint(9210000, 9300000), lambda: c.itemconfig(loader, text="92% complete"))
  root.after(random.randint(9310000, 9400000), lambda: c.itemconfig(loader, text="93% complete"))
  root.after(random.randint(9410000, 9500000), lambda: c.itemconfig(loader, text="94% complete"))
  root.after(random.randint(9510000, 9600000), lambda: c.itemconfig(loader, text="95% complete"))
  root.after(random.randint(9610000, 9700000), lambda: c.itemconfig(loader, text="96% complete"))
  root.after(random.randint(9710000, 9800000), lambda: c.itemconfig(loader, text="97% complete"))
  root.after(random.randint(9810000, 9900000), lambda: c.itemconfig(loader, text="98% complete"))
  root.after(random.randint(9910000, 10000000), lambda: c.itemconfig(loader, text="99% complete"))

def main():
            root.after(random.randint(1000, 2000), lambda : c.itemconfig(loader, text="1% complete"))
            root.after(random.randint(2100, 3000), lambda : c.itemconfig(loader, text="2% complete"))
            root.after(random.randint(3100, 4000), lambda: c.itemconfig(loader, text="20% complete"))
            root.after(random.randint(4100, 5000), lambda: c.itemconfig(loader, text="40% complete"))
            root.after(random.randint(5100, 6000), lambda: c.itemconfig(loader, text="41% complete"))
            root.after(random.randint(6100, 7000), lambda: c.itemconfig(loader, text="48% complete"))
            root.after(random.randint(7100, 8000), lambda: c.itemconfig(loader, text="49% complete"))
            root.after(random.randint(8100, 9000), lambda: c.itemconfig(loader, text="50% complete"))
            root.after(random.randint(9100, 10000), lambda: c.itemconfig(loader, text="51% complete"))
            root.after(random.randint(10100, 11000), lambda: c.itemconfig(loader, text="56% complete"))
            root.after(random.randint(11100, 12000), lambda: c.itemconfig(loader, text="67% complete"))
            root.after(random.randint(12100, 13000), lambda: c.itemconfig(loader, text="69% complete"))
            root.after(random.randint(13100, 14000), lambda: c.itemconfig(loader, text="73% complete"))
            root.after(random.randint(14100, 15000), lambda: c.itemconfig(loader, text="74% complete"))
            root.after(random.randint(15100, 16000), lambda: c.itemconfig(loader, text="80% complete"))
            root.after(random.randint(16100, 17000), lambda: c.itemconfig(loader, text="82% complete"))
            root.after(random.randint(17100, 18000), lambda: c.itemconfig(loader, text="90% complete"))
            root.after(random.randint(18100, 19000), lambda: c.itemconfig(loader, text="99% complete"))
            root.after(random.randint(19100, 20000), lambda: c.itemconfig(loader, text="100% complete"))
            root.after(random.randint(21100, 22000), lambda: root.destroy())
            root.after(random.randint(21100, 22000), lambda: root.deiconify())

main()
root.mainloop()