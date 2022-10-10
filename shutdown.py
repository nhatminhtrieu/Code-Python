import os
print("Nhập thời gian hẹn tắt máy tính: ", end = "")
time = input()
msg = "shutdown /s /t "
msg += time
os.system(msg)
print("Done. Máy tính sẽ tắt sau " + time + " giây.")