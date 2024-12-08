from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_twitter_card_image(
    title: str,
    subtitle: str,
    width: int = 1200,
    height: int = 628,
    background_color: str = "#4747bf",
    title_color: str = "#FFFFFF",
    subtitle_color: str = "#FFFFFF",
    title_font_path: str = "fonts/Inter-Bold.ttf",
    subtitle_font_path: str = "fonts/Inter-Regular.ttf",
    title_font_size: int = 80,
    subtitle_font_size: int = 40,
    padding: int = 50
):
    img = Image.new('RGB', (width, height), color=background_color)
    draw = ImageDraw.Draw(img)
    title_font = ImageFont.truetype(title_font_path, title_font_size)
    subtitle_font = ImageFont.truetype(subtitle_font_path, subtitle_font_size)

    # Truncate and wrap text into multiple lines to fit
    title = textwrap.shorten(title, 75, placeholder='…')
    title_lines = textwrap.wrap(title, width=25)
    subtitle = textwrap.shorten(subtitle, 150, placeholder='…')
    subtitle_lines = textwrap.wrap(subtitle, width=50)

    # Calculate line heights based on the font used
    title_ascent, title_descent = title_font.getmetrics()
    title_line_height = title_ascent + title_descent
    subtitle_ascent, subtitle_descent = subtitle_font.getmetrics()
    subtitle_line_height = subtitle_ascent + subtitle_descent
    title_height = len(title_lines) * title_line_height
    subtitle_height = len(subtitle_lines) * subtitle_line_height
    gap = 30
    total_text_height = title_height + gap + subtitle_height

    # Center vertically
    start_y = (height - total_text_height) // 2

    # Draw the title
    y_text = start_y
    for line in title_lines:
        bbox = draw.textbbox((0,0), line, font=title_font)
        line_width = bbox[2] - bbox[0]
        x = padding
        draw.text((x, y_text), line, font=title_font, fill=title_color)
        y_text += title_line_height

    # Add spacing between title and subtitle
    y_text += gap

    # Draw the subtitle
    for line in subtitle_lines:
        bbox = draw.textbbox((0,0), line, font=subtitle_font)
        line_width = bbox[2] - bbox[0]
        x = padding
        draw.text((x, y_text), line, font=subtitle_font, fill=subtitle_color)
        y_text += subtitle_line_height

    return img

if __name__ == "__main__":
    title_text = "When Does a Service-as-Software Model Make Sense?"
    subtitle_text = "The service-as-software model is nacsent but expected to be experimented with in different fields as artificial intelligence techniques improve and enable new applications."
    image = create_twitter_card_image(title=title_text, subtitle=subtitle_text)
    image.save("output_image.png", optimize=True, quality=100)
    print("Image saved as output_image.png")
