import os
import markdown
from pathlib import Path

# Paths
CONTENT_DIR = "content"
OUTPUT_DIR = "html"
TEMPLATE_FILE = "template.html"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load the HTML template
with open(TEMPLATE_FILE, "r") as template_file:
    template = template_file.read()

# Process each Markdown file
for md_file in Path(CONTENT_DIR).glob("*.md"):
    # Determine the output HTML file name
    output_file = Path(OUTPUT_DIR) / f"{md_file.stem}.html"

    # Generate a title from the file name
    title = md_file.stem.replace("-", " ").capitalize()

    # Convert Markdown to HTML
    with open(md_file, "r") as file:
        md_content = file.read()
    html_content = markdown.markdown(md_content)

    # Insert the title and content into the template
    final_html = template.replace("{{ title }}", title).replace("{{ content }}", html_content)

    # Save the resulting HTML file
    with open(output_file, "w") as file:
        file.write(final_html)

    print(f"Generated: {output_file}")
