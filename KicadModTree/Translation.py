'''
kicad-footprint-generator is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

kicad-footprint-generator is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with kicad-footprint-generator. If not, see < http://www.gnu.org/licenses/ >.

(C) 2016 by Thomas Pointhuber, <thomas.pointhuber@gmx.at>
'''

from .Point import *
from .Node import Node


class Translation(Node):
    '''
    Apply translation to the child tree
    '''
    def __init__(self, x, y):
        Node.__init__(self)

        # translation information
        self.offset_x = x
        self.offset_y = y


    def getRealPosition(self, coordinate):
        parsed_coordinate = Point(coordinate)

        # calculate translation
        translation_coordinate = {'x': parsed_coordinate.x + self.offset_x
                                 ,'y': parsed_coordinate.y + self.offset_y
                                 ,'r': parsed_coordinate.r}

        if not self._parent:
            return translation_coordinate
        else:
            return self._parent.getRealPosition(translation_coordinate)


    def _getRenderTreeText(self):
        render_text = Node._getRenderTreeText(self)
        render_text += " [x: {x}, y: {y}]".format(x=self.offset_x
                                                 ,y=self.offset_y)

        return render_text