#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

import os
from builtins import input
from builtins import range
from builtins import int
from future import standard_library

standard_library.install_aliases()
from chiplotle import *
from chiplotle.hpgl.commands import *
import chiplotle.tools.io as io
import random
import argparse

parser = argparse.ArgumentParser(
    description="Draw random shapes and lines",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument("--output", type=str, help="Path to output file")
parser.add_argument("--view", action="store_true", help="Show plot as well as output?")
parser.add_argument(
    "-n", "--pen-count", type=int, default=1, help="How many pens to use?"
)


def main(args, width=30000, height=20000, left=0, right=30000, bottom=0, top=20000):
    pen_count = args.pen_count

    print("width: %d height: %d" % (width, height))

    # start in a random spot
    plot = abstract_masterpiece(top, bottom, left, right, height, width, pen_count)
    if args.output is None or args.view:
        io.view(plot)
    if args.output is not None:
        output_name, extension = os.path.splitext(args.output)
        io.export(plot, output_name, fmt=extension[1:])


def abstract_masterpiece(top, bottom, left, right, height, width, pen_count):
    plot = [PA([random_point(top, bottom, left, right)])]
    pen_id = 1
    while True:
        plot.append(SP(pen_id))
        gesture_id = random.randint(0, 5)

        if gesture_id == 0:
            feature = random_circle()
        elif gesture_id == 1:
            feature = random_rect()
        elif gesture_id == 2:
            feature = random_filled_rect()
        elif gesture_id == 3:
            feature = random_line(top, bottom, left, right)
        elif gesture_id == 4:
            feature = random_shape(top, bottom, left, right, width, height)
        else:
            feature = random_pen_move(top, bottom, left, right)
        plot.extend(feature)

        pen_id = randomly_switch_pen(pen_id)
        if pen_id == pen_count + 1:
            break
    plot.append(SP(0))
    return plot


def random_shape(top, bottom, left, right, width, height):
    feature = []
    print("draw an abstract shape!")
    polygon_edges = random.randint(2, 4)
    print("polygon_edges: ", polygon_edges)
    firstX = random.randint(left, right)
    firstY = random.randint(bottom, top)
    feature.append(PA([(firstX, firstY)]))
    feature.append(PD())
    xRange = width / 5
    yRange = height / 5
    for i in range(polygon_edges):
        feature.append(
            PR(
                [
                    (
                        random.randint(int(-xRange), int(xRange)),
                        random.randint(int(-yRange), int(yRange)),
                    )
                ]
            )
        )
    feature.append(PA([(firstX, firstY)]))
    feature.append(PU())
    return feature


def random_line(top, bottom, left, right):
    feature = []
    print("draw a crazy line!")
    feature.append(PD())
    feature.append(PA([random_point(top, bottom, left, right)]))
    feature.append(PU())
    return feature


def random_filled_rect():
    feature = []
    print("filled rect!")
    ft = random.randint(1, 8)
    if ft == 1 or ft == 2:
        ft = 1
    if ft == 3 or ft == 4 or ft == 5:
        ft = 3
    if ft == 6 or ft == 7 or ft == 8:
        ft = 4
    space = random.randint(10, 100)
    angle = random.randint(0, 3) * 45
    print("fill type: %d space: %d angle: %d" % (ft, space, angle))
    feature.append(hpgl.RR(random_point(2000, 10, 10, 2000)))
    feature.append(hpgl.FT(ft, space, angle))
    return feature


def random_rect():
    feature = []
    print("rect!")
    feature.append(hpgl.ER(random_point(5000, 10, 10, 5000)))
    return feature


def random_circle():
    feature = []
    print("circle!")
    feature.append(hpgl.CI(random.randint(10, 5000), random.randint(1, 180)))
    return feature


def random_point(top, bottom, left, right):
    return random.randint(left, right), random.randint(bottom, top)


def random_pen_move(top, bottom, left, right):
    feature = []
    print("just jump around!")
    feature.append(PA([random_point(top, bottom, left, right)]))
    return feature


def randomly_switch_pen(pen_id, probability=0.25):
    assert probability <= 1.0
    if random.random() < probability:
        pen_id += 1
    return pen_id


if __name__ == "__main__":
    main(parser.parse_args())
