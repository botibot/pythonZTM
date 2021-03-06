#!DRY Do not repeat yourself

#! Positional Parameters and Arguments
# parameters
def say_hello(name, emoji):
    print(f'Helllooooo {name} {emoji}')


#! default parameters are set on the definition of the function
def say_hello2(name='Darth Vader', emoji='ð'):
    print(f'Helllooooo {name} {emoji}')


# arguments --> call or invoke
say_hello('Jorge', 'ðĪŠ ðĐ')
print(say_hello)

#! keyword arguments
# * bad practice?
say_hello(emoji='ðĐ', name='Bibi')
say_hello(name='Bibi', emoji='ðĐ')

say_hello2()
say_hello2('Jorge', 'â')


#!Return
def suma(num1, num2):
    return num1 + num2


print(suma(4, 5))
