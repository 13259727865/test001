import subprocess,psutil
import time

if __name__ == '__main__':
    bat_path = r"D:\Program Files(x86)\Luxflows\LuxFlow1.2.0_0822\LuxFlow_V1.2.0.0822\LuxFlow.exe"

    process = subprocess.Popen(bat_path,shell=True,encoding="utf-8")


    time.sleep(3)
    print(process.pid)
    print(psutil.Process(process.pid).name())
    print(psutil.Process(process.pid).is_running())
    print(psutil.pid_exists(process.pid))

    # child = subprocess.Popen(['ping','-c','4','www.baidu.com'])
    # print('parent')