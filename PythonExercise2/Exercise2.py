rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'

rhyme_new = rhyme.strip().lower().split()

count = 0

for i in rhyme_new:
    gonona = rhyme_new.count(i)
    if gonona > count:
        count = gonona
        print('Count of "',i,'"is', gonona)
