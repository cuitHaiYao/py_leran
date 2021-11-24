import hashlib
# 加密 手机号后六位
import uuid

SALT = 'SAFDSAFADS,(#336,.!F332'
def generate_pwd(str1):
    obj = hashlib.md5(SALT.encode('utf-8'))
    obj.update(str1.encode('utf-8'))
    return obj.hexdigest()
def uuidget():
    print(uuid.uuid4().__str__())
if __name__ == '__main__':
     str1 = generate_pwd("50c152c4c7f74a16b3743906f86c895e")
     by = bytes(str1, 'UTF-8')
     by.hex()
     print(by.hex())

    # uuidget()