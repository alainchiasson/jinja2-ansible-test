#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'b_filter': self.b_filter
        }

    def b_filter(self, a_variable, another_variable, yet_another_variable):
        a_new_variable = a_variable + ' - ' + another_variable + ' - ' + yet_another_variable
        return a_new_variable
