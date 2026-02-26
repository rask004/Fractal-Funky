from fractal import fractal_factory

# generic help for how fractal_factory works
help(fractal_factory)

print("Using area formula for a square of side length X")
# area formula needed for fractal_factory
def square_area(side_length:float) -> float:
    return side_length * side_length

# assume the fractal pattern uses squares, and by default all 4 corners are available for the
#   first iteration of fractals
# creates one function for creating a sequence representing the fractals, and another for finding
#   the area sum
print("Creating fractal_sequence and fractal_sum functions with following defaults:")
print("\tSide length change between iterations = 1/2")
print("\tNumber of Iterations = 1")
print("\tDecimal Precision = 10 units\n")
make_square_fractals, square_fractal_sum = fractal_factory(square_area, 4)

# help will always show the generic help text for each function
help(make_square_fractals)
help(square_fractal_sum)

# make a sequence, starting with a square side length of 1, scaling by half the length with each level, for 5 levels
# Note that this assumes ALL available corners at each level will be filled with a new fractal.
fractals = make_square_fractals(1, change_fraction=0.5, iterations=5)
print("square fractal pattern: ", fractals)

# find only the area sum for the above sequence
total = square_fractal_sum(1, change_fraction=0.5, iterations=5)
print("sum of area = ", total, "units")

print('\n')

# A sequence with 16 iterations, start side length of 5.0 units.
#   Use decimal precision of 20 places for more accuracy
fractals = make_square_fractals(5.0, change_fraction=0.5, iterations=16, precision=20)
print("square fractal pattern with more iterations: ", fractals)
total = square_fractal_sum(5.0, change_fraction=0.5, iterations=16, precision=20)
print("sum of area = ", total, "units")

print('\n')

# 10 iterations, start side length of 2 units, scaling by 1/4, But this time there are initially just 2 fractals,
#   And from then on each iteration has only one fractal.
fractals = make_square_fractals(2, change_fraction=0.25, iterations=10, initial_subfractal_count=2, repeating_subfractal_count=1)
print("another square fractal pattern: ", fractals)
total = square_fractal_sum(2, change_fraction=0.25, initial_subfractal_count=2, repeating_subfractal_count=1, iterations=10)
print("sum of area = ", total, "units")
