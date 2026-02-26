# Fractal-Funky
An excuse to practice using a closure as a factory function, while thinking about fractals I think I heard in an episode  of The Rest Is Science Podcast. Or maybe it was Chocolate. Fractal Chocolate?

## Modules

`fractal.py` contains the factory function `fractal_factory`. This is a closure and factory function, for creating other functions used to find the areas of abstracted fractal shapes.

The Fractal Factory function requires as inputs, a function for calculating an area, and several default arguments. Fractal Factory returns a pair of new functions.

The first function creates a sequence of tuples, representing the areas of abstract fractals. For example, look at the following sequence:

`(1, 1.0), (4, 0.25), (12, 0.0625)`

The root shape has an area of 1.0 units squared. At the next fractal level, are 4 shapes each of area 0.25 units^2, and at the 3rd level are 12 shapes each with the related area given.

The second function finds the total sum of area that such a sequence would have, again in units^2.

The arguments passed to the `fractal_factory` function

Each pair of functions created from one call to `fractal_factory` are guaranteed to accept the same positional arguments, same keyword arguments, and have the same default values. This is as a balance between flexible usage (not having to remake the area finding functions every time inputs change, or tediously repeat arguments), and sameness of function behaviour for correctness and reliability.

Default values are set when calling `fractal_factory`. They remain in place for the lifetime of the pair of functions which are returned.

The only fixed value that cannot be changed is the function argument for the area formula.
