# 🚨 Не меняйте код вне зеленой зоны!

def is_prime_number(number):
# 🟢 (НАЧАЛО) Напишите ваш код здесь 👇

# 🟢 (КОНЕЦ)

def test_1():
    assert is_prime_number(1) == False
    assert is_prime_number(-1) == False
    assert is_prime_number(-113) == False
    assert is_prime_number(293) == True
    assert is_prime_number(31) == True
    assert is_prime_number(2) == True
    assert is_prime_number(3) == True
    assert is_prime_number(5) == True
    assert is_prime_number(7) == True
    assert is_prime_number(9) == False
    print('Тесты пройдены')

test_1()