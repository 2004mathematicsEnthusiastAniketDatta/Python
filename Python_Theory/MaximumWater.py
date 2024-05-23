class Solution(object):
    
    def maxarea(self, height):
        max_water = -1
        front_wall = 0
        back_wall = len(height)-1
        tallest_wall = max(height)
        while ( front_wall < back_wall ):
            max_water = max(min(height[front_wall],height[back_wall]) * (back_wall - front_wall),max_water)
            if height[front_wall] <= height[back_wall]: front_wall += 1
            else: back_wall -= 1
            if max_water > tallest_wall * (back_wall - front_wall): break
        return max_water
    
    