y = 0.5
h = 0.2
min = 0
max = 2
t = min
n = int(max/h)
    f = (m.sin(2*t)-2*t*y)/t**2
    return h*f
for i in range(n):

    k1 = function(y, t, h)
    k2 = function(y+(k1/2),t+(h/2), h)
    k3 = function(y+(k2/2), t+(h/2), h)
    t += h
    k4 = function(y+(k3/2), t, h)
    y = y + (k1+2*k2+2*k3+k4)/6
    print("Iteration ",i,":",k1,k2,k3,k4,y)
