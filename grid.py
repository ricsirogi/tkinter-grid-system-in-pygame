import pygame
import json
import os


class Grid():
    def __init__(self, x: int, y: int) -> None:
        self.members = {}
        self.margin = 5  # margin between each member in pixels
        self.x = 0
        self.y = 0

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

        # Add the new member into self.members if the row doesn't exists
        if str(new_member_row) not in self.members.keys():
            self.members[str(new_member_row)] = {}
            self.members[str(new_member_row)][str(new_member_column)] = member

        # Add the new member into self.members if the row exists
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
        y = self.y
        for row_value in self.members.values():
            x = self.x
            highest_height = 0
            for column_value in row_value.values():
                column_value.x = x
                column_value.y = y

                x += column_value.width + self.margin
                if column_value.height > highest_height:
                    highest_height = column_value.height
            y += highest_height + self.margin

        # * Step 4)
        return (self.members[str(new_member_row)][str(new_member_column)].x, self.members[str(new_member_row)][str(new_member_column)].y)

    def draw_members(self):
        for row in self.members.values():
            for member in row.values():
                member.draw()

    def get_key(self, target_value, row):
        for key, value in self.members[row].items():
            if value == target_value:
                return key
        return None
