# -*- coding: utf-8 -*-
from math import sin, cos, asin, degrees, radians

RADIUS = 6371000


def bounding_box(lat, distance):
    dlat = distance / RADIUS
    dlon = asin(sin(dlat)/cos(radians(lat)))
    return degrees(dlat), degrees(dlon)
