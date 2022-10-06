# 🚨 Не меняйте код вне зеленой зоны!
guests = []

def invite_friends(friends):
	friends.append(f'Всего гостей приглашено: {len(friends)}')
	print(*friends, sep=' приглашен!\n')

# 🟢 (НАЧАЛО) Напишите ваш код здесь 👇

# 🟢 (КОНЕЦ)

invite_friends(guests)
