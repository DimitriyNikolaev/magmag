__author__ = 'dimitriy'

from django.utils.translation import ugettext_lazy as _

MAGMAG_ORDER_STATUSES = (
    (1, _("Adopted")),
    (2, _("Paid")),
    (3, _("Completion")),
    (4, _("Completed")),
    (5, _("Sent"))
)

MAGMAG_DELIVERY_METHODS = (
    (1, _("Post")),
    (2, _("EMS")),
    (3, _("Pickup")),
    (4, _("Courier"))
)

MAGMAG_DELIVERY_COSTS = {
    1: 350,
    2: 450,
    3: 0,
    4: 300
}