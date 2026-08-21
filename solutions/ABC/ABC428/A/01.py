s, a, b, x = map(int, input().split(' '))

total_run = 0
total_time = 0

while total_time < x:
    if x - total_time >= a:
        total_run += s * a
        total_time += a
        if x - total_time >= b:
            total_time += b
        else:
            total_time = x
    else:
        total_run += s * (x - total_time)
        total_time = x
    
print(total_run)