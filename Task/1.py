user_age = 20
is_premium = True
is_suspended = False

can = (user_age >= 18 ) and is_premium and (not is_suspended)
print(can)