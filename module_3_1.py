calls = 0
def county_calls():
  global calls
  calls += 1



def string_info(string):
    county_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    county_calls()
    return string.lower() in [s.lower() for s in list_to_search]

print(string_info('Intel'))
print(string_info('Nvidia'))
print(is_contains('Tytan', ['TyT', 'tam', 'tYtAN']))
print(is_contains('Radeon', ['Neon', 'radEO']))
print(calls)