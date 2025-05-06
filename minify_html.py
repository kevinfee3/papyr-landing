import re

def minify_html(html_content):
    # Remove comments
    html_content = re.sub(r"<!--(.*?)-->", "", html_content, flags=re.DOTALL)
    # Remove newlines and tabs
    html_content = re.sub(r"\n+\s*", "", html_content)
    html_content = re.sub(r"\t+", "", html_content)
    # Remove multiple spaces
    html_content = re.sub(r"\s{2,}", " ", html_content)
    # Remove spaces between tags where appropriate
    html_content = re.sub(r">\s+<", "><", html_content)
    return html_content.strip()

input_file_path = "/home/ubuntu/papyr-landing-page/index.html"
output_file_path = "/home/ubuntu/papyr-landing-page/index.min.html"

with open(input_file_path, "r", encoding="utf-8") as f_in:
    original_html = f_in.read()

minified_html_content = minify_html(original_html)

with open(output_file_path, "w", encoding="utf-8") as f_out:
    f_out.write(minified_html_content)

print(f"Minified HTML saved to {output_file_path}")
