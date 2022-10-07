# 🚨 Не меняйте код вне зеленой зоны!

def is_prime_number(number):
# 🟢 (НАЧАЛО) Напишите ваш код здесь 👇

# 🟢 (КОНЕЦ)

def test_1():
    assert get_bonuses(1) == 0
    assert get_bonuses(2) == 5
    assert get_bonuses(6) == 30
    assert get_bonuses(5) == 15
    assert get_bonuses(9) == 60
    print('Тесты пройдены')

test_1()