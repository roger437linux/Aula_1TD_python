frase = input('\nDigite uma frase: ')
ch = '\u35a6'
for i in range(len(frase)+4):
    print(ch, end='')
print(f'\n{ch} {frase} {ch}')
for i in range(len(frase)+4):
    print(ch, end='')