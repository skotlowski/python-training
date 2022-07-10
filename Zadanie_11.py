import re
from pprint import pprint
# moj_pierwszy_regex = re.compile(r"\d\d\d")
# print(moj_pierwszy_regex.search("Moja liczba12 1234321 jest 666!"))
#
# telefon_regex = re.compile('\d\d\d-\d\d\d-\d\d\d')
# print(telefon_regex.search('Moj nr telefonu to 661-402-123'))
#
# telefon_regex = re.compile('(\d\d\d)-(\d\d\d)-(\d\d\d)')
# mo = telefon_regex.search('Moj nr telefonu to 661-402-123')
# print(mo.group(3))

# telefon_regex = re.compile(r'(\d\d)-(\d\d\d)-(\d\d\d)')
# mo = telefon_regex.search('Moj nr telefonu to 48-612-213')
# print(mo.group(2))
# print(mo.group(3))
#
# numer_identyfikacyjny = re.compile(r'\d{11}') # ma sie pojawic liczba 11 razy
#
# hero_regex = re.compile(r'Batman|Superman')
# print(hero_regex.search("Batman jest silniejszy niz Superman"))
#
# bat_regex = re.compile(r"Bat(man|mobile|copter|bat)")
# print(bat_regex.search("Kupiłem sobie wczoraj Batmobile."))
#
# niem_regex = re.compile(r"Niem(iec|ka|ców)")
# print(niem_regex.search("Zdanie o Niemiec"))
#
# bat_regex = re.compile(r"Bat(wo)?man")
# print(bat_regex.search("Any Batman?"))

# tel_regex = re.compile(r"(\d{2}-)?\d{3}-\d{3}-\d{3}")
# print(tel_regex.search("Numer telefonu 123-123-121"))

# nr = 'jakis string 123-123-123'
#
#
# numer_telefonu = []
#
# for item in nr:
#     if item.isdigit() or item == '-':
#         numer_telefonu.append(item)
#         if len(numer_telefonu) == 9:
#             break
#
# print(''.join(numer_telefonu))
#
# bat_regax = re.compile(r"Bat(wo)*man") # * oznacza, ze grupa jest opcjonalna i moze wystapic wiele razy w tym miejscu
# print(bat_regax.search('Batwowowowowoman Batman Batwoman'))
#
# bat_regax = re.compile(r"Bat(wo)+man") # + grupa (wo) musi wystapic jeden raz lub wiecej
# print(bat_regax.search('Batman Batman Batwoman'))
#
# bat_regax = re.compile(r"(Ha){3,5}")
# print(bat_regax.search(('HaHaHa')))
#
# bat_regax = re.compile(r"(Ha){3,}")
# print(bat_regax.search(('HaHaHaHaHaHaHa')))
#
# bat_regax = re.compile(r"(Ha){,8}")
# print(bat_regax.search(('dsd')))
#
# bat_regax = re.compile(r'(\w){3,6}')
# print(bat_regax.search('asdf gfdsg fsfds'))
#
# regex = re.compile(r'\S\W{4,6}\D')
# print(bat_regax.search('Abcdsa lub cos'))

# text = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'
#
# regex = re.compile(r'\d{1,2}\s\w{4,8}')
# pprint(regex.findall(text))
#
# samogloski = re.compile(r'[aeiouAEIOU]')
# pprint(samogloski.findall('To jest przykladowy TEKST!!'))
# samogloski = re.compile(r'[d-eF-G1-6]')
# pprint(samogloski.findall('To jest przykladowy TEKST!!'))
# samogloski = re.compile(r'[^aeiouAEIOU]') # negacja ^

imie_nazwisko = 'Jan Kowalski'
wiek = '22'
kod_poczt = '12-123'
haslo = 'abcdeffkfues2'

name_regex = re.compile(r'\w{4,}\s\w{4,}')
print(name_regex.search(imie_nazwisko))

wiek_regex = re.compile(r'\d{1,3}')
print(wiek_regex.search(wiek))

kod_regex = re.compile(r'\d{2}-\d{3}')
print(kod_regex.search(kod_poczt))

haslo_regex = re.compile(r'\w{8,}')
print(haslo_regex.search(haslo))
