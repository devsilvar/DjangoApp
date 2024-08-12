from django import template


register = template.Library()


def cut(values, args):
    return values.replace(args, '')



register.filter('cut' , cut)