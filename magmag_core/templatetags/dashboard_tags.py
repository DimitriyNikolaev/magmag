from django import template

from magmag_core.apps.dashboard.nav import get_nodes

register = template.Library()


def dashboard_navigation(parser, token):
    return DashboardNavigationNode()


def getattribute(value, arg):
    """Gets an attribute of an object dynamically from a string name"""
    if hasattr(value, str(arg)):
        return getattr(value, str(arg))
    else:
        return ''




class DashboardNavigationNode(template.Node):

    def render(self, context):
        user = context['user']
        context['nav_items'] = get_nodes(user)
        return ''


register.tag('dashboard_navigation', dashboard_navigation)
register.filter('getattribute', getattribute)
