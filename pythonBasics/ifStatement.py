#if statemnt

x=5
y=8
z=5
a=3
if x<y:
    print('true')

if z< y > x >a :
    print('it\'s a mess')

if z <= x:
    print('z is less than or equal to x')
if z==x:
    print('they equal each other')

if z!=y:
    print('they\'re aren\'t equal')
#if else

b=5
c=8

if b > c:
    print('x is bigger')
else:
    print('it\'s actually less')

#elif
r,t,e=5,10,22
if r>t:
    print('r is bigger')
elif r<e:
    print('less')
    if r==5:
        print('the val is 10 of course')
else:
    print('íf and elif never ran')