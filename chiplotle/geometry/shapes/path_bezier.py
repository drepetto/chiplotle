from chiplotle.geometry.core.path import Path
from chiplotle.tools.mathtools.bezier_interpolation import bezier_interpolation

def path_bezier(control_points, weight=1, interpolation_count=50):
    """
    Rational Bezier curve.
    """
    ## cycle weights... 
    if isinstance(weight, (list, tuple)):
        w_len = len(weight)
        p_len = len(control_points)
        weight = weight * (p_len // w_len) + weight[: p_len % w_len]
        
    plot_points = bezier_interpolation(control_points,
                                       interpolation_count,
                                       weight)
    return Path(plot_points)


## RUN DEMO CODE

if __name__ == '__main__':
    from chiplotle.tools import io
    from chiplotle.geometry.shapes.group import group
    from chiplotle.geometry.shapes.cross import cross
    from chiplotle.geometry.transforms.offset import offset

    t_base = 4000
    points = [(-t_base/2,0),(0,t_base*0.8660),(t_base/2,0)]

    ## a list containing different sets of weights for the middle point
    weights = [[1,1,1],[1,2,1],[1,0.5,1],[1,0,1],[1,-0.5,1]]

    c = group([])
    ## draws a cross at each control point
    for i in points:
       r = cross(100,100)
       offset(r, i)
       c.append(r)

    ## draws the rational bezier curve for each weight set
    for w in weights:
       b = path_bezier(points, weight=w)
       c.append(b)

    io.view(c)

