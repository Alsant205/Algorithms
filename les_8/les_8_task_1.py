"""
1) Определение количества различных подстрок с использованием хеш-функции. Пусть
на вход функции дана строка. Требуется вернуть количество различных подстрок в
этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:
func("papa")
6
func("sova")
9
"""
import hashlib


def hashing(obj):
    sha1 = hashlib.sha1()
    sha1.update(obj.encode('utf-8'))
    res = sha1.hexdigest()
    return res


string = 'papa'

result = []
for n in range(1, len(string)):
    for i in range(len(string)):
        substring = string[i:i + n]
        hash_ = hashing(substring)
        if hash_ not in result and substring != '' and hash_ != hashing(string):
            result.append(hash_)
print(f'итого подстрок: {len(result)}\n', result)
