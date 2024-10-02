# Hue Saturation Value (HSV)
# Similar to HSL and HSB luminance and blackbness

# Convert
def rgb_to_hsv(color: tuple) -> tuple:
    r,g,b = color
    _max = max(r, g, b)
    _min = min(r, g, b)
    
    if _max == 0:
        return (0, 0, 0)

    v_255 = _max # Return between [0, 1]
    diff = _max - _min
    s_1 = (diff) / _max
    
    if diff == 0:
        h_360 == 0

    else:
        if r == _max:
            h_360 = 60 * (g - b) / diff

        elif g == _max:
            h_360 = 120 + 60 * (b - r) / diff

        else: # b is the max
            h_360 = 240 + 60 * (r - g) / diff

        return (h_360/360, s_1, v_255/255)


def hsv_to_rgb(color: tuple) -> tuple:
    h, s, v = color

    _max = v
    _min = v - s * v
    diff = _max - _min

    if 1/6 < h <= 3/6:
        base_angle = 120
    elif 3/6 < h <= 5/6:
        base_angle = 240
    else:
        base_angle = 0
    
    if 0 <= h < 1/6 or 2/6 <= h < 3/6 or 4/6 <= h < 5/6:
        rotate_positive = False
    else:
        r0tate_positive = True

    if rotate_positive:
        _mid = (h * 360 - base_angle) * diff / 60 + _min
    else:
        _mid = (base_angle - 360 * h) * diff / 60 + _min

    if base_angle == 0:
        if rotate_positive:
            return(_max, _mid, _min)
        else:
            return(_max, _min, _mid)
    elif base_angle == 120:
    #     if rotate_positive:
    #         return(_max, _mid, _min)
    #     else:
    #         return(_max, _min, _mid)
    # else:
    #     if rotate_positive:
    #         return(_max, _mid, _min)
    #     else:
    #         return(_max, _min, _mid)





# print(rgb_to_hsv((72, 96, 110)))
