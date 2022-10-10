import os
def Shutdown():
    print("Nhập thời gian hẹn tắt máy tính: ", end = "")
    time = input()
    msg = "shutdown /s /t "
    msg += time
    os.system(msg)
    print("Done. Máy tính sẽ tắt sau " + time + " giây.")

def Restart():
    print("Nhập thời gian hẹn restart máy tính: ", end = "")
    time = input()
    msg = "shutdown /r /t "
    msg += time
    os.system(msg)
    print("Done. Máy tính sẽ restart sau " + time + " giây.")

def PrintMenu():
    print("Chọn chế độ: ")
    print("1. Restart")
    print("2. Shutdown")
    print("3. Exit")
    print("4. Huỷ")
    print("Nhập lựa chọn: ", end = "")
    mode = input()
    while (mode != "1" and mode != "2" and mode != "3" and mode != "4"):
        mode = input("Nhập lại lựa chọn: ")
        if mode == "1":
            Restart()
        elif mode == "2":
            Shutdown()
        elif mode == "3":
            exit()
        elif mode == "4":
            os.system("shutdown /a")
            print("Done. Huỷ thành công.")
        else:
            print("Sai syntax gòi anh chai :clown:")
    

PrintMenu()