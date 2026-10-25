import html

def make_html(title, code_file, output_file):
    with open(code_file, 'r') as f:
        code_text = f.read()
    with open(output_file, 'r') as f:
        out_text = f.read()

    html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{
    background-color: #1e1e1e;
    color: #d4d4d4;
    font-family: 'Courier New', Courier, monospace;
    padding: 20px;
    margin: 0;
  }}
  .container {{
    max-width: 900px;
    margin: auto;
  }}
  h2 {{
    color: #4ec9b0;
    border-bottom: 1px solid #333;
    padding-bottom: 5px;
  }}
  pre {{
    background-color: #252526;
    border: 1px solid #333;
    border-radius: 6px;
    padding: 15px;
    overflow-x: auto;
    font-size: 14px;
    line-height: 1.5;
  }}
  .output-box {{
    background-color: #0f0f0f;
    border: 1px solid #007acc;
    border-radius: 6px;
    padding: 15px;
    color: #9cdcfe;
    white-space: pre-wrap;
    font-size: 14px;
    line-height: 1.5;
  }}
</style>
</head>
<body>
<div class="container">
  <h2>Python Source Code: {title}</h2>
  <pre><code>{html.escape(code_text)}</code></pre>

  <h2>Execution Output: {title}</h2>
  <div class="output-box">{html.escape(out_text)}</div>
</div>
</body>
</html>
"""
    return html_content

print("HTML generator ready")
