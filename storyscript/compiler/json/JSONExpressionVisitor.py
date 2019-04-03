# -*- coding: utf-8 -*-
from storyscript.compiler.visitors.ExpressionVisitor import ExpressionVisitor


class JSONExpressionVisitor(ExpressionVisitor):
    """
    Serializes an expression as JSON
    """

    def __init__(self, visitor):
        self.visitor = visitor

    _types = {
        'PLUS': 'sum', 'DASH': 'subtraction', 'POWER': 'exponential',
        'MULTIPLIER': 'multiplication', 'BSLASH': 'division',
        'MODULUS': 'modulus',
        'AND': 'and', 'OR': 'or', 'NOT': 'not', 'EQUAL': 'equals',
        'GREATER': 'greater', 'LESSER': 'less',
        'NOT_EQUAL': 'not_equal',
        'GREATER_EQUAL': 'greater_equal',
        'LESSER_EQUAL': 'less_equal'
    }

    def expression_type(self, operator, tree):
        ret = self._types.get(operator, None)
        tree.expect(ret is not None, 'compiler_error_no_operator',
                    operator=operator)
        return ret

    def values(self, tree):
        return self.visitor.values(tree)

    def nary_expression(self, tree, op, values):
        expression = self.expression_type(op.type, tree)
        return {
            '$OBJECT': 'expression',
            'expression': expression,
            'values': values,
        }