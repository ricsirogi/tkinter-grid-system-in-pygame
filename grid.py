import pygame
import json
import os
from typing import Optional


class Grid():
    def __init__(self, x: int, y: int, parent: Optional['Grid'] = None) -> None:
        self.members = {}
        self.margin = 0  # margin between each member in pixels
        self.parent = parent
        self.x, self.y = (parent.x + x, parent.y + y) if parent is not None else (x, y)
        # will be used to store the original position of the grid when updating members positions
        self.pos = (self.x, self.y)
        self.width = 0
        self.height = 0

        self.row = 0
        self.column = 0

    def add(self, member, new_member_row, new_member_column) -> tuple[int, int]:
        """
        Step 1)
        Add the new member into the dictionary

        Step 2)
        Generate a dictionary that will have all the members of the grid in the order that
        they should be displayed. This is because dictionaries are unordered.

        Step 3)
        Calculate each member's position in the grid.

        Step 4)
        Return the position of the member in the grid
        """

        # * Step 1)

        # Firstly, remove the member from the grid if it was there previously
        for row_key, row_value in self.members.items():
            if member in row_value.values():
                self.members[row_key].pop(self.get_key(member, row_key))
                print("found it")

        # Add the row to self.members if it doesn't exist
        if str(new_member_row) not in self.members.keys():
            self.members[str(new_member_row)] = {}

        # Add the new member into self.members
        self.members[str(new_member_row)][str(new_member_column)] = member

        # * Step 2)
        # order the members in the grid
        # Sort outer dictionary
        sorted_members = dict(sorted(self.members.items(), key=lambda item: int(item[0])))

        # Sort inner dictionaries
        for key, value in sorted_members.items():
            sorted_members[key] = dict(sorted(value.items(), key=lambda item: int(item[0])))

        self.members = sorted_members

        # * Step 3)
        self.update_members_positions()

        # * Step 4)
        return (self.members[str(new_member_row)][str(new_member_column)].x, self.members[str(new_member_row)][str(new_member_column)].y)

    def update_members_positions(self):
        """
        Updates the positions of the members in the grid.

        This function iterates over the members in the grid and updates their x and y positions 
        based on the grid's x and y coordinates, as well as the margin between members.
        It also calculates the height and width of the grid based on the size of the members.
        """

        y = self.y
        widest_width = 0
        for row_value in self.members.values():
            x = self.x
            highest_height = 0
            for column_value in row_value.values():
                column_value.x = x
                column_value.y = y

                x += column_value.width + self.margin
                if column_value.height > highest_height:
                    highest_height = column_value.height
            if x > widest_width:
                widest_width = x
            y += highest_height + self.margin
        self.height = y - self.pos[1]
        self.width = widest_width - self.pos[0]

    def grid(self, row, column):
        if self.parent is not None:
            self.row = row
            self.column = column

            new_pos = self.parent.add(self, row, column)

            self.x = new_pos[0]
            self.y = new_pos[1]
            self.pos = (self.x, self.y)

    def draw_members(self):
        for row in self.members.values():
            for member in row.values():
                if isinstance(member, Grid):
                    member.update_members_positions()
                    member.draw_members()
                else:
                    member.draw()

    def get_key(self, target_value, row):
        for key, value in self.members[row].items():
            if value == target_value:
                return key
        return None
