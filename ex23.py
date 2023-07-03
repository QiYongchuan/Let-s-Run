# 字符串、字节串和字符编码
# 解码字节串，编码字符串；  “decode bytes,encode strings"
import sys
script,encoding,error = sys.argv
def main(language_file,encoding,errors):
    line = language_file.readline()    # 读取文件中的第一行，当运行到文件的结尾时，readline会返回一个空字符串，if用来检查空字符串，只要不为空就继续运行
    if line:
        print_line(line,encoding,errors)   # 调用print_line函数
        return main(language_file,encoding,errors)   # 再次调用main
    
def print_line(line,encoding,errors):       # 这个函数是对languages.txt中每一行进行编码 
    next_lang = line.strip()                # 去掉每一行结尾的\n
    raw_bytes = next_lang.encode(encoding,errors = errors)  # next_lang 是字符串，要获取原始字节串，调用encode()编码字符串
    cooked_string = raw_bytes.decode(encoding,errors=errors) # 此步将字节串 再次编码到字节串，这个字节串与next_lang是一样的

    print(raw_bytes,"<===>",cooked_string)   # 将字节串和字符串分别打印出来

languages = open("languages.txt",encoding="utf-8") #选择打开的文件，到languages中

main(languages,encoding,error)