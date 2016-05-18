import itertools

# Generators operate on two principles: they produce a value each time a yield statement is encountered, 
# and unless it is iterated over, their code is paused.
# It doesn't matter how many yield statements are used in a generator, 
# the code is still run in normal python ordering. 
# In this case, there is no loop, just a series of yield statements, so each time the generator is advanced, 
# python executes the next line, which is another yield statement.
# What happens with the neighbors generator is this:
#     * Generators always start paused, so calling neighbors(position) returns a generator that hasn't done anything yet.
#     * When it is advanced (next() is called on it), the code is run until the first yield statement. 
#       First x, y = point is executed, then x + 1, y is calculated and yielded. The code pauses again.
#     * When advanced again, the code runs until the next yield statement is encountered. It yields x - 1, y.
#     * etc. until the function completes.
def neighbors(point):
    x, y = point
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1
    yield x + 1, y + 1
    yield x + 1, y - 1
    yield x - 1, y + 1
    yield x - 1, y - 1

def advance( board ):
	newstate = set()


    # map(neighbors, board) produces an iterator for each and every position in the board sequence. 
    # It simply loops over board, calls neighbors on each value, and returns a new sequence of the results. 
    # Each neighbors() function returns a generator.
    # The *parameter syntax expands the parameter sequence into a list of parameters, 
    # as if the function was called with each element in parameter as a separate positional parameter instead.
    # param = [1, 2, 3]; foo(*param) would translate to foo(1, 2, 3).
    # itertools.chain(*map(..)) takes each and every generator produced by the map, 
    # and applies that as a series of positional parameters to itertools.chain(). 
    # Looping over the output of chain means that each and every generator for each and every board position is iterated over once, in order.
    # All the generated positions are added to a set, essentially removing duplicates
	recalc = board | set( itertools.chain(*map(neighbors, board)))
	for point in recalc:
		count = sum((neigh in board) for neigh in neighbors(point))
		if count == 3 or (count ==2 and point in board):
			newstate.add(point)
	return newstate



glider = set([(0,0),(1,0),(2,0),(0,1),(1,2)])
for i in range(5):
	glider = advance(glider)
	print glider
