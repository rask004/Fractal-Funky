from collections import namedtuple
from decimal import Decimal, getcontext
from typing import Callable

__all__ = ["fractal_factory",]

default_precision = getcontext().prec

fractal_item = namedtuple("fractal", ["count", "area_per_fractal"])

# closure factory pattern, this way we don't have to keep passing lots of tedious arguments as inputs
def fractal_factory(area_formula:Callable[..., float], default_initial_subfractal_count:int, default_repeating_subfractal_count:int=0, default_change_fraction:float=0.5, default_iterations:int=1, default_precision=10) -> tuple[Callable[..., tuple[tuple[int, float], ...]], Callable[..., float]]:
    """factory method, to create both a fractal sequence function and a fractal summing function.

    area_formula:   function accepting an arbitrary number of float arguments, and
            returning a float result. Calculates the area of a shape.
    subfractal count:   how many sub-shapes to create for each fractal iteration.

    Return Value:   2 functions,  to produce a sequence of tuples, which represent repreating fractals."""

    c_frac_ = default_change_fraction
    iters_= default_iterations
    prec_ = default_precision
    init_subfrac_ = default_initial_subfractal_count
    rep_subfrac_ = default_repeating_subfractal_count
    if not 0 < default_repeating_subfractal_count < default_initial_subfractal_count:
        rep_subfrac_ = default_initial_subfractal_count - 1


    def fractal_sequence(*args:float, change_fraction:float=c_frac_, iterations:int=iters_, initial_subfractal_count=init_subfrac_, repeating_subfractal_count=rep_subfrac_, precision=prec_) -> tuple[tuple[int, float], ...]:
        """creates sequence of numeric tuples representing fractal shapes.

        *args:  Arguments needed to calculate the area of the shape.
                Assumes the correct arguments needed for an area formula function.
        change_fraction:    multiplier for each area arguments, applied with
                successive iterations. Must be a positive fraction.
        iterations:     number of fractal iterations to complete. must be a
                positive integer.
        precision: decimal precision to use.

        Return Value:   tuple, containing tuples in this format: (count:int, fractal_area:float)"""

        old_precision = getcontext().prec
        getcontext().prec = precision

        fractals = [fractal_item(1, area_formula(*args)),]
        factor = Decimal(change_fraction)
        fractal_count = initial_subfractal_count
        next_args = [Decimal(a) * factor for a in args]

        for _ in range(1, iterations):
            args_ = tuple([float(a) for a in next_args])
            new_fractals = fractal_item(fractal_count, area_formula(*args_))
            fractals.append(new_fractals)
            fractal_count *= repeating_subfractal_count
            next_args = [Decimal(a) * factor for a in next_args]

        getcontext().prec = old_precision

        return tuple(fractals)

    def fractal_area_total(*args:float, change_fraction:float=0.5, iterations:int=1, initial_subfractal_count=init_subfrac_, repeating_subfractal_count=rep_subfrac_, precision=12) -> float:
        """finds the total area covered by a fractal sequence.

        *args:  Arguments needed to calculate the area of the shape.
                Assumes the correct arguments needed for an area formula function.
        change_fraction:    multiplier for each area arguments, applied with
                successive iterations. Must be a positive fraction.
        iterations:     number of fractal iterations to complete. must be a
                positive integer.

        precision: decimal precision to use.

        Return Value:   float, total area of fractal."""
        sequence = fractal_sequence(*args, change_fraction=change_fraction, iterations=iterations, initial_subfractal_count=initial_subfractal_count, repeating_subfractal_count=repeating_subfractal_count, precision=precision)
        total = sum([item[0] * item[1] for item in sequence])

        return total

    return (fractal_sequence, fractal_area_total)
