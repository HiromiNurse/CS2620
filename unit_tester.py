import unittest
from image_functions import *


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.image1 = WorkingImage("color.jpg")

    def test_cor_grey(self):
        self.image1.corrected_greyscale()
        self.image1.save("corrected_greyscale")

    def test_grey(self):
        self.image1.greyscale()
        self.image1.save("greyscale")

    def test_red_isolation(self):
        self.image1.isolateRed()
        self.image1.save("redscale")

    def test_green_isolation(self):
        self.image1.isolateGreen()
        self.image1.save("greenscale")

    def test_blue_isolation(self):
        self.image1.isolateBlue()
        self.image1.save("bluescale")

    def test_mirror1(self):
        self.image1.rightToLeftMirror()
        self.image1.save("RtoLmirror")

    def test_mirror2(self):
        self.image1.leftToRightMirror()
        self.image1.save("LtoRmirror")

    def test_mirror3(self):
        self.image1.topToBottomMirro()
        self.image1.save("TtoBmirror")

    def test_mirror4(self):
        self.image1.bottomToTopMirror()
        self.image1.save("BtoTmirror")

    def test_mirror5(self):
        self.image1.topToBottomDiagonalMirror()
        self.image1.save("TtoBdmirror")

    def test_mirror6(self):
        self.image1.bottomToTopDiagonalMirror()
        self.image1.save("BtoTdmirror")

    def test_flipx(self):
        self.image1.flipXAxis()
        self.image1.save("xflip")

    def test_flipy(self): # didnt work
        self.image1.flipYAxis()
        self.image1.save("fylip")

    def test_flipd(self): # didnt work
        self.image1.flipDiagonal()
        self.image1.save("dflip")
        
    def test_invert(self):
        self.image1.invertColors()
        self.image1.save("color_invert")
        
    def test_rotate_clock(self):
        self.image1.rotate90Clockwise()
        self.image1.save("clockwise_90")
        
    def test_rotate_counter(self):
        self.image1.rotate90CounterClockiwse()
        self.image1.save("counter_90")
        
    def test_rotate_enlarge(self):
        self.image1.rotateAndEnlarge(45)
        self.image1.save("bigger_rotate")
        
    def test_rotate_smaller(self):
        self.image1.rotateAndCrop(45)
        self.image1.save("smaller_rotate")
        
    def test_rotate_about_center(self):
        self.image1.rotateAboutCenter(45)
        self.image1.save("center_rotate")
        
    def test_rotate_about_point(self):
        self.image1.rotateAboutCenter(45)
        self.image1.save("center_rotate")

    def test_translation(self):
        self.image1.arbitraryTranslation(100, 100)
        self.image1.save("translation")

    def test_transformation(self):
        self.image1.arbitraryTransformation(1, 1, "width", 0, 1, "height")
        self.image1.save("transformation")
        
    def test_scale(self):
        self.image1.scale(2)
        self.image1.save("scaled")

    def blur(self):
        self.image1.blur(10, 5)
        self.image1.save("blurry")

    def blurnopad(self):
        self.image1.blurNoPadding(10, 5)
        self.image1.save("blurry no pad")
        
    
    
if __name__ == '__main__':
    unittest.main()
