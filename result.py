queue = list()
while True:
    try:
        command, val = input().split()
        print(command, val)
        queue.append(val)
        print('ok')
    except ValueError:
        command = input()
        if command[0] == 'pop':
            if queue: print(queue.pop(0))
            else: print('error')
        elif command[0] == 'front':
            if queue: print(queue[0])
            else: print('error')
        elif command[0] == 'size': print(len(queue))
        elif command[0] == 'clear':
            stack = list()
            print('ok')
        elif command[0] == 'exit':
            print('bye')
            break

'''
pop
size
push 1
size
push 2
size
push 3
size
exit
'''