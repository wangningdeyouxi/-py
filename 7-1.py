#编写函数实现串行加密和j解密，循环使用指定密钥，采用简单异或算法
def crypt(source,key):
    from itertools import cycle
    result=''
    temp=cycle(key)
    for ch in source:
        result=result+chr(ord(ch)^ord(next(temp)))
    return result
source='Shangdong Institute of Business and Technology'
key='Wang Ning'
print('Before Encrypted:'+source)
encrypted=crypt(source,key)
print('After Encrypted:'+encrypted)
decrypted=crypt(encrypted,key)
print('After Decrypted:'+decrypted)
