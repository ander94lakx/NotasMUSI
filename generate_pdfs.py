import markdown
from pathlib import Path
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="referrer" content="no-referrer" />
    <meta name="referrer" content="unsafe-url" />
    <meta name="referrer" content="origin" />
    <meta name="referrer" content="no-referrer-when-downgrade" />
    <meta name="referrer" content="origin-when-cross-origin" />
    <title>Page Title</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            font-family: Helvetica,Arial,sans-serif;
        }
        code, pre {
            font-family: monospace;
        }
        table {
            padding: 0; 
        }
        table tr {
            border-top: 1px solid #cccccc;
            background-color: white;
            margin: 0;
            padding: 0;
        }
        table tr:nth-child(2n) {
            background-color: #f8f8f8; 
        }
        table tr th {
            font-weight: bold;
            border: 1px solid #cccccc;
            text-align: left;
            margin: 0;
            padding: 6px 13px; 
        }
        table tr td {
            border: 1px solid #cccccc;
            text-align: left;
            margin: 0;
            padding: 6px 13px; 
        }
        table tr th :first-child, table tr td :first-child {
            margin-top: 0; 
        }
        table tr th :last-child, table tr td :last-child {
            margin-bottom: 0; 
        }
    </style>
</head>
<body>
<div class="container">
{{content}}
</div>
</body>
</html>
"""

if __name__ == "__main__": 
    paths = []
    excluded = ['links.md', 'README.md']
    for path in Path('.').rglob('*.md'):
        if (path.name not in excluded):
            paths.append(path)
            print(path)

    for path in paths:
        with open(path, encoding='utf8') as file:
            # Generate basic HTML from original markdown

            extensions = ['extra', 'smarty', 'tables']
            html = markdown.markdown(file.read(), extensions=extensions, output_format='html5')
            doc = TEMPLATE.replace('{{content}}', html)

            # Use weasyprint to generate quality html to use in PDF generator
            font_config = FontConfiguration()
            html = HTML(string=doc)
            css = CSS(string='@page { size: A4; margin: 2cm }')

            # Generated PDF files will be stored separatedly but with the same folder structure
            filepath = str(path).replace('.md', '.pdf').replace('Markdown', 'PDF')
            Path(filepath).parents[0].mkdir(parents=True, exist_ok=True)
            html.write_pdf(filepath, stylesheets=[css], font_config=font_config,)
