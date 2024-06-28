import os
import random
import string
import requests
import pyfiglet
import time
import os

# Set text color to green
os.system("tput setaf 6")

# Set text style to live type
figlet_text = pyfiglet.figlet_format("Alone Stand Larka", font="slant")
for char in figlet_text:
    print(char, end="", flush=True)
    time.sleep(0.005)
print()

def generate_report(mobile_number):
    report = f"Watsapp Ban Report of scammer and drugs Dealer\nMobile Number: {mobile_number}\nReason: Scamming and drug dealing"
    with open(f"/sdcard/Download/{mobile_number}.txt", "w") as f:
        f.write(report)
    print(f"Report generated and saved to /sdcard/Download/{mobile_number}.txt")

def create_text_files(n):
    folder_name = "Text_Files"
    os.makedirs(f"/sdcard/Download/{folder_name}", exist_ok=True)
    for i in range(n):
        filename = f"file_{i+1}.txt"
        with open(f"/sdcard/Download/{folder_name}/{filename}", "w") as f:
            words = [" ".join(random.choice(string.ascii_lowercase) for _ in range(10)) for _ in range(100)]
            f.write("\n".join(words))
    print(f"{n} text files created in /sdcard/Download/{folder_name}")

def download_images(n):
    folder_name = "Images"
    os.makedirs(f"/sdcard/Download/{folder_name}", exist_ok=True)
    for i in range(n):
        url = f"https://picsum.photos/200/300?random={i}"
        response = requests.get(url)
        with open(f"/sdcard/Download/{folder_name}/image_{i+1}.jpg", "wb") as f:
            f.write(response.content)
    print(f"{n} images downloaded and saved to /sdcard/Download/{folder_name}")

def main():
    print("Select an option:")
    print("1. Generate Report")
    print("2. Create Text Files")
    print("3. Download Images")
    option = input("Enter your choice: ")

    if option == "1":
        mobile_number = input("Enter mobile number with country code: ")
        generate_report(mobile_number)
    elif option == "2":
        n = int(input("How many files do you want to create? "))
        create_text_files(n)
    elif option == "3":
        n = int(input("How many images do you want to download? "))
        download_images(n)
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()