from storyscript.compiler.semantics.functions.Function import Function, \
        MutationFunction
from storyscript.compiler.semantics.symbols.Symbols import Symbol
from storyscript.compiler.semantics.types.Types import AnyType, IntType, \
        StringType


def test_function__to_str():
    fn = Function('foo', {}, AnyType.instance())
    assert str(fn) == 'Function(foo)'


def test_function_pretty():
    fn = Function('foo', {}, AnyType.instance())
    assert fn.pretty() == 'foo()'


def test_function_pretty_a():
    args = {'a': Symbol('a', IntType.instance())}
    fn = Function('foo', args, AnyType.instance())
    assert fn.pretty() == 'foo(a:`int`)'


def test_function_pretty_b():
    args = {'a': Symbol('a', IntType.instance()),
            'b': Symbol('b', StringType.instance())}
    fn = Function('foo', args, AnyType.instance())
    assert fn.pretty() == 'foo(a:`int` b:`string`)'


def test_mutation__to_str():
    fn = MutationFunction('foo', {}, AnyType.instance())
    assert str(fn) == 'Mutation(foo)'


def test_mutation_pretty():
    fn = MutationFunction('foo', {}, AnyType.instance())
    assert fn.pretty() == 'foo'


def test_mutation_pretty_a():
    args = {'a': Symbol('a', IntType.instance())}
    fn = MutationFunction('foo', args, AnyType.instance())
    assert fn.pretty() == 'foo a:`int`'


def test_mutation_pretty_b():
    args = {'a': Symbol('a', IntType.instance()),
            'b': Symbol('b', StringType.instance())}
    fn = MutationFunction('foo', args, AnyType.instance())
    assert fn.pretty() == 'foo a:`int` b:`string`'
