import os
import base64
from openai import OpenAI

client = OpenAI()

os.makedirs("../../images/input_images", exist_ok=True)
os.makedirs("../../images/output_images", exist_ok=True)

def save_image(result, filename: str) -> None:
    """
    Saves the first returned image to the given filename inside the output_images folder.
    """
    image_base64 = result.data[0].b64_json
    out_path = os.path.join("../../images/output_images", filename)
    with open(out_path, "wb") as f:
        f.write(base64.b64decode(image_base64))

from IPython.display import HTML, Image, display

def display_image_grid(items, width=240):
    cards = []
    for item in items:
        title = item.get("title", "")
        label = f'<div style="font-weight:600;margin-bottom:8px">{title}</div>' if title else ""
        cards.append(
            '<div style="text-align:center">'
            + label
            + f'<img src="{item["path"]}" width="{width}" style="max-width:100%;height:auto;" />'
            + '</div>'
        )
    display(HTML('<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:flex-start">' + ''.join(cards) + '</div>'))