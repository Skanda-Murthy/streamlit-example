import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image, ImageDraw

def generate_circle_headshot(image, circle_diameter):
    # Resize the image to the specified circle diameter
    image = image.resize((circle_diameter, circle_diameter))
    
    # Create a circular mask
    mask = Image.new("L", (circle_diameter, circle_diameter), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, circle_diameter, circle_diameter), fill=255)
    
    # Apply the circular mask to the image
    circular_image = Image.new("RGBA", (circle_diameter, circle_diameter))
    circular_image.paste(image, (0, 0), mask)
    
    return circular_image

def generate_badge_with_headshot(headshot_path, template_path, output_path):
    # Open the headshot image
    headshot = Image.open(headshot_path)
    
    # Open the template image
    template = Image.open(template_path)
    
    # Specify the position where the circular headshot should be placed on the template
    headshot_position = (220, 220)  # Example coordinates, adjust as needed
    
    # Generate circular headshot
    circle_diameter = 6400  # Adjust the diameter as needed
    circular_headshot = generate_circle_headshot(headshot, circle_diameter)
    
    # Paste the circular headshot onto the template at the specified position
    template.paste(circular_headshot, headshot_position, circular_headshot)
    
    # Save the resulting badge image
    template.save(output_path, format="PNG")

if __name__ == "__main__":
    headshot_path = "/home/user/python files/IEEE Day app/Headshot/Matt (1).png"  # PNG format
    output_path = "badge_with_headshot.png"
    
    generate_badge_with_headshot(headshot_path, template_path, output_path)
