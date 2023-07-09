# 读写文件 （二） 设置一个数据记录器
import sys
import os
# from Crypto.Cipher import AES   两个外部加密库  弃用
# from cryptography.fernet import Fernet
import hashlib
from sys import argv
from datetime import date, datetime


current_date = date.today().isoformat()
current_datetime_s = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# 登录功能
# print(sys.version)
# print("可执行文件路经：>>", sys.executable)  # sys.executable会打印Python解释器的可执行文件路径
# print("搜索路径:>>", sys.path)       # sys.path会打印Python模块搜索路径。


def encrypt_password(password):
    # 使用SHA-256哈希算法对密码进行加密
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# 获取用户输入的密码


def set_password():
    password = input("设置你的密码Enter your password: ")
    # 加密密码
    hashed_password = encrypt_password(password)

    # 将加密后的密码写入文件  v0 是将密码单独存储在一个文件夹中
    # with open('password.txt', 'w') as file:
    #     file.write(hashed_password)

    # 将加密后的密码写入到加密文件的第一行中，使用w，如果重写，意味着这个文件夹也将重写了
    with open('Privatedirly.bin', 'wb') as file:
        file.write(hashed_password.encode('utf-8'))
        file.write(b'\n')  # 添加换行符，每次写入后换行  =>写入换行符是因为要把密码写到第一行，读写时只读第一行内容，
        # 真正的内容是以二进制写到下一行的，避免写入后的内容混入到密码中


def login():
    # 判断是否是第一次登录（检查password.txt是否存在）
    try:
        with open('Privatedirly.bin', 'rb') as file:
            stored_password = file.readline().strip().decode('utf-8')
            print(stored_password)
            # 获取用户输入的密码
            password = input("输入你的密码进行判断Enter your password: ")

            # 加密输入的密码
            hashed_password = encrypt_password(password)

            # 比较输入的密码和存储的密码
            if hashed_password == stored_password:
                print("Login successful!")
                save()
                return True
            else:
                print("Login failed.")
                return False

    except FileNotFoundError:
        # 第一次登录，设置密码并保存文件
        set_password()
        print("Password set.You can now log in")
        return


def number(lines, filename):

    # 读取已有记录的数量，如果文件不存在，则默认为0
    try:
        with open(filename, 'r') as file:
            count = len(file.readlines())
    except FileNotFoundError:
        count = 0

    # 获取当前日期和时间并格式化为字符串
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 自动编号
    count += 1
    record = f"{count}. {current_datetime} - {lines}"
    return record


def number2(lines, filename):  # 因为第二个文件是二进制的文件，编号无法根据长度来算
    # 读取已有记录的数量，如果文件不存在，则默认为0
    try:
        with open(filename, 'rb') as file:
            data = file.read()
            count = data.count(b'\n')
        return count
    except FileNotFoundError:
        count = 0

     # 自动编号
    count += 1
    # 获取当前日期和时间并格式化为字符串

    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    record = f"{count}. {current_datetime} - {lines}"
    return record


def darily():
    filename = "date.txt"

    print(f"This is QYC code datebase: {filename}.")
    print("If you don't want that, hit CTRLL-C (^C).")
    print("If you want that, hit ENTER.\n")

    input("?\n")

    print(f"Opening your database in {current_date}....")

    txt = open(filename)

    print(f"Here's your file {filename}")
    print(txt.read())

    target = open(filename, '+a')

    print("Write your record:\n")
    lines = input(">> ")

    # 写入文件
    with open('date.txt', 'a') as file:
        file.write(number(lines, 'date.txt') + '\n')

    txt = open(filename)

    print(f"Here is your file {filename}:")
    print(txt.read())


def private(privateMessage):
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    filename = "Privatedirly.bin"
    print(f"这是你的私密日记本: {filename}.")

    input("?\n")

    print(f"现在的时间是 {current_date}....")

    # 将privateMessage 进行编号 即调用函数number

    # numberMess = number2(privateMessage, 'Privatedirly.bin')
    TimeMessage = f"{current_datetime} => [ {privateMessage}]"

    bitext = TimeMessage.encode('utf-8')  # 将字符串编码为二进制形式
    with open('Privatedirly.bin', 'ab') as file:
        file.write(bitext + b"\n")    # 每次写完换行

    print("写入完成！")

    #  开始读文件
    with open('Privatedirly.bin', 'rb') as file:
        binary_data = file.read()

        # 将二进制数据解码为字符串
        text = binary_data.decode('utf-8')
        print("这是你私密文件的内容", text)


def save():
    print("请选择私密存储#1,还是非私密存储#2")
    choice = int(input(">> "))
    if choice == 1:
        privateMessage = input(">>请输入你的内容： ")
        private(privateMessage)
    elif choice == 2:
        darily()


login()


#  一次曾经的尝试：为内容加密，因为库的引入的原因，第一次尝试失败；  第二次尝试，更换库之后，成功，但是在升级过程中，想将密码和文件都放在一起，失败了，改为存二进制了。

# 另一个库   现在遇到了一点问题，内容加密尝试暂时放弃，改为存储为二进制的形式吧。

# def private(privateMessage):

#    # 生成密钥
#     key = Fernet.generate_key()

#     # 加密函数
#     plaintext = privateMessage

#     def encrypt(key, plaintext):
#         f = Fernet(key)
#         ciphertext = f.encrypt(plaintext.encode('utf-8'))
#         return ciphertext

#     # 解密函数

#     def decrypt(key, ciphertext):
#         f = Fernet(key)
#         plaintext = f.decrypt(ciphertext).decode('utf-8')
#         return plaintext

#     # 加密并写入文件

#     ciphertext = encrypt(key, plaintext)
#     with open('Privatedirly.bin', 'ab') as file:
#         file.write(ciphertext)

#     # 从文件中读取并解密
#     with open('Privatedirly.bin', 'rb') as file:
#         ciphertext = file.read()
#     # 解密文件
#     plaintext = decrypt(key, ciphertext)
#     print(plaintext)


# # 加密函数

# def encrypt_message(key, message):
#     iv = os.urandom(16)
#     encryptor = AES.new(key, AES.MODE_CBC, iv)

#     # 将iv作为头部写入输出消息
#     encrypted_message = iv + encryptor.encrypt(message.encode())
#     return encrypted_message


# # 设置密钥和消息
# key = b'MySuperSecretKey'
# message = "This is my secret message."

# # 加密消息
# encrypted_message = encrypt_message(key, message)

# # 将加密后的消息写入文件
# with open('encrypted_message.txt', 'wb') as file:
#     file.write(encrypted_message)


# script , filename =argv
