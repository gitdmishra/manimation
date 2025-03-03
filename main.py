import manim
from manim import *


class MultiplicationScene(Scene):
    def construct(self):
        self.show_multiplication(3, 3)
    
    def show_multiplication(self, num1, num2):
        # Create initial title
        title = MathTex(f"{num1} \\times {num2} = {num1 * num2}").scale(1.5)
        title.to_edge(UP, buff=1.5)

        # Create horizontal row of num1 circles with different colors
        circles = []
        colors = [BLUE, RED, GREEN, YELLOW, PURPLE, ORANGE]
        spacing = 4.5 / max(num1, 4)  # Reduced from 6 to 4.5 for closer horizontal spacing
        
        # Create first row of circles
        for i in range(num1):
            circle = Circle(radius=0.4).set_fill(colors[i % len(colors)], opacity=0.5)  # Reduced radius from 0.5 to 0.4
            circle.move_to(LEFT * (spacing * (num1-1)/2) + RIGHT * (spacing * i))
            circles.append(circle)

        # Group the circles together for first row
        circle_group = VGroup(*circles)
        
        # Create vertical copies for num2 rows
        copies = []
        vertical_spacing = 0.9  # Slightly reduced from 1.0 for closer vertical spacing
        
        # Calculate available vertical space (excluding title area)
        available_height = 7  # Increased from 6 to give more space
        title_buffer = 2  # Space reserved for title
        bottom_buffer = 1  # Space reserved for bottom
        usable_height = available_height - title_buffer - bottom_buffer
        
        # Calculate total height needed and scale spacing if necessary
        total_height = vertical_spacing * (num2 - 1)
        if total_height > usable_height:
            vertical_spacing = usable_height / (num2 - 1)
            total_height = usable_height

        # Calculate starting y-position to center in available space
        # Shift up by adding bottom_buffer/2 to prevent bottom overflow
        start_y = (total_height / 2) - (title_buffer - bottom_buffer/2)
        
        for i in range(num2):
            copy = circle_group.copy()
            # Position each row from top to bottom with fixed spacing
            y_pos = start_y - (i * vertical_spacing)
            copy.shift(UP * y_pos)
            copies.append(copy)

        # Show title
        self.play(Write(title))
        self.wait(1)

        # Show first group
        self.play(Create(copies[0]))
        self.wait(1)

        # Show remaining groups emerging from original
        for i in range(1, num2):
            self.play(
                TransformFromCopy(copies[0], copies[i], run_time=1.5),
            )
            self.wait(1)
        self.wait(5)
        # Create new title for the doubled groups
        new_title = MathTex(f"{num1} \\times {num2} \\times 2 = {num1 * num2 * 2}").scale(1.5)
        new_title.to_edge(UP, buff=1.5)

        # Group all circles together
        all_circles = VGroup(*copies)
        
        # Create two copies of all circles and scale them down
        left_copy = all_circles.copy().scale(0.5)
        right_copy = all_circles.copy().scale(0.5)
        
        # Position the copies
        left_copy.move_to(LEFT * 4)
        right_copy.move_to(RIGHT * 4)

        # Create subtitles for left and right copies
        left_subtitle = MathTex(f"{num1} \\times {num2} = {num1 * num2}").scale(0.8)
        right_subtitle = MathTex(f"{num1} \\times {num2} = {num1 * num2}").scale(0.8)
        
        # Position subtitles below the circle groups
        left_subtitle.next_to(left_copy, DOWN, buff=0.5)
        right_subtitle.next_to(right_copy, DOWN, buff=0.5)

        # Animate the transformation, title changes, and subtitles
        self.play(
            TransformFromCopy(all_circles, left_copy, run_time=1.5),
            TransformFromCopy(all_circles, right_copy, run_time=1.5),
            FadeOut(all_circles, run_time=1.5),
            FadeOut(title, run_time=1),
            FadeIn(new_title, run_time=1.5),
            FadeIn(left_subtitle, run_time=1.5),
            FadeIn(right_subtitle, run_time=1.5),
        )
        
        self.wait(2)


# Example usage:
class Create4x5(MultiplicationScene):
    def construct(self):
        self.show_multiplication(4, 5)  # Will create animation for 4 × 5


# Example usage:
class Create3x2(MultiplicationScene):
    def construct(self):
        self.show_multiplication(3, 2)  # Will create animation for 3 × 2

class Create3x4(MultiplicationScene):
    def construct(self):
        self.show_multiplication(3, 4)  # Will create animation for 3 × 4

