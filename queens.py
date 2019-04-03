import random

def eightQueens(coords, draw = True):

    def draw_board():
        levels = 8
        for x in range(levels, 0, -1):
            base = '\n{}  '.format(x)
            for y in range(1, levels+1):
                if (y, x) in Queenlocations:
                    base += queen
                elif (y, x) in valid_locations:
                    base += valid
                    updated_valid.append((y, x))
                else:
                    base += empty

            if draw == True: print(base)
        if draw == True: print('   A  B  C  D  E  F  G  H')

    def invalid_spot(queen):
        xmax = max(8 - queen[0], queen[0])
        ymax = max(8 - queen[1], queen[1])
        output = []
        for xdelta in range(1, xmax +1):
            for ydelta in range(1, ymax+1):
                if xdelta == ydelta:
                    pass
                else:
                    if queen[0] + xdelta <= 8 and queen[1] + ydelta <= 8:
                        output.append((queen[0] + xdelta, queen[1] + ydelta))
                    if queen[0] + xdelta <= 8 and queen[1] - ydelta > 0:
                        output.append((queen[0] + xdelta, queen[1] - ydelta))
                    if queen[0] - xdelta > 0 and  queen[1] + ydelta <= 8:
                        output.append((queen[0] - xdelta, queen[1] + ydelta))
                    if queen[0] - xdelta > 0 and  queen[1] - ydelta > 0:
                        output.append((queen[0] - xdelta, queen[1] - ydelta))
        return output

    def multi_invalid_spot(spots):
        if len(spots) == 1:
            return invalid_spot(spots[0])
        workingset = spots
        convertingset = []
        answer = []
        output = []
        for i in workingset:
            convertingset.append(invalid_spot(i))
        for queen in convertingset:
            for point in queen:
                count = 0
                for queen2 in convertingset:
                    if point in queen2:
                        count += 1
                if count == len(convertingset):
                    answer.append(point)
        return answer

    def is_valid():
        for i in Queenlocations:
            x = i[0]
            y = i[1]
            for z in Queenlocations:
                if z == i:
                    pass
                elif z[0] == x:
                    if draw == True: print('\nupdown conflict!')
                    return False
                elif z[1] == y:
                    if draw == True: print('\nsidetoside conflict!')
                    return False
                elif abs(x - z[0]) == abs(y - z[1]):
                    if draw == True: print('\ndiagonal conflict!')
                    return False
                else:
                    pass
        if (len(updated_valid) == 0) and (len(coords) == 8):
            return True
        elif len(updated_valid) < 8-len(coords):
            if draw == True:
                print\
                ('\nRemaining Queens outnumber potential spots.. Restart.')
            return False
        else:
            if draw == True:
                print('\n')
            updated_valid.sort()
            return updated_valid

    queen = 'X  '
    valid = 'O  '
    empty = 'O  '
    valid_locations = multi_invalid_spot(coords)
    Queenlocations = coords
    updated_valid = []
    draw_board()
    return is_valid()

def tester(draw=True):
    global count
    global iterations
    global all_solutions
    x = 1
    y = random.choice(range(1, 9))
    test_set = []
    test_set.append((x,y))
    if draw ==True:
        batch = eightQueens(test_set)
    elif draw == False:
        batch = eightQueens(test_set, False)
    while type(batch) == list:
        if len([i for i in batch if i[0] == x + 1]) == 0:
            if draw == True:
                print('Column {} invalid. Must be 1 Queen per row.. restart'\
                .format(x+1))
            count +=1
            if count == iterations:
                sol_set = set(map(tuple, all_solutions))
                solutions = list(map(list, sol_set))
                print('\n{0} unique solutions in {1} iterations:'\
                .format(len(solutions), iterations))
                return solutions
            else:
                if draw == True:
                    return tester()
                elif draw == False:
                    return tester(False)
        new = random.choice([i for i in batch if i[0] == x + 1])
        x += 1
        test_set.append(new)
        if draw ==True:
            batch = eightQueens(test_set)
        elif draw == False:
            batch = eightQueens(test_set, False)
    if batch == False:
        count += 1
        if count == iterations:
            sol_set = set(map(tuple, all_solutions))
            solutions = list(map(list, sol_set))
            print('\n{0} unique solutions in {1} iterations:'\
            .format(len(solutions), iterations))
            return solutions
        else:
            if draw == True:
                return tester()
            elif draw == False:
                return tester(False)
    elif batch == True:
        count += 1
        all_solutions.append(test_set)
        if count == iterations:
            sol_set = set(map(tuple, all_solutions))
            solutions = list(map(list, sol_set))
            print('\n{0} unique solutions in {1} iterations:'\
            .format(len(solutions), iterations))
            return solutions
        else:
            if draw == True:
                print('\nSolution found with the following coordinates:\n'\
                , test_set)
            if draw == True:
                return tester()
            elif draw == False:
                return tester(False)
count = 0
all_solutions = []
iterations = int(input('Iterations: '))
para1 = str(input('Draw process? (T/F):'))
para2 = int(input\
('Display found solutions in Cartesian or Chess coordinates? (1 or 2):'))
if para1 in ['T', 't']:
    para1 = True
elif para1 in ['F', 'f']:
    para1 = False
x = tester(para1)
if para2 == 1:
    for i in x:
        print('\n', i)
elif para2 == 2:
    def converter(point):
        ref = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
        backwards_ref = \
        {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H'}
        if type(point[0]) == int:
            return '{0}{1}'.format(backwards_ref[point[0]], point[1])
        elif type(point[0]) == str:
            return (ref[point[0]], int(point[1]))
    out = []
    for i in x:
        temp = []
        for j in i:
            temp.append(converter(j))
        out.append(temp)
    for i in out:
        print('\n', i)
