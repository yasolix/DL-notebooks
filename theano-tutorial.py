import numpy
from theano import function
import theano.tensor as T

x = T.dscalar('x')
y = T.dscalar('y')

z = x + y

f = function([x, y], z)

f(2,3)
