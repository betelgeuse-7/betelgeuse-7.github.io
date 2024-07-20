"""
structure of the markdown:

    title=""
    description=""
    keywords=""
    date="dd-mm-yyyy"
    ---
    <md>
"""
import markdown2, time, os, sys, re, styles
from pygments.formatters import HtmlFormatter

def mdtohtml(md_path):
    start_time = time.time()
    if not md_path.endswith(('.md', '.markdown')):
        sys.exit("the input file must have a .md or .markdown extension")
    pygments_formatter = HtmlFormatter(style='default')
    pygments_css = pygments_formatter.get_style_defs('.codehilite')
    with open(md_path, 'r') as f:
        md_text = f.read()
    metadata_match = re.search(r'^title="(.+)"\ndescription="(.+)"\nkeywords="(.+)"\ndate="(\d{2}-\d{2}-\d{4})"\n---\n', md_text, re.DOTALL | re.MULTILINE)
    if metadata_match:
        title = metadata_match.group(1)
        description = metadata_match.group(2)
        keywords = metadata_match.group(3)
        date = metadata_match.group(4)
    else:
        print(f"metadata section not found at the top of the file: {md_path}")
        sys.exit(1)
    md_text = re.sub(r'^title=".+"\ndescription=".+"\nkeywords=".+"\n---\n', '', md_text, count=1, flags=re.DOTALL | re.MULTILINE)
    pygments_formatter = HtmlFormatter(style='default')
    pygments_css = pygments_formatter.get_style_defs('.codehilite')
    html_text = markdown2.markdown(md_text, 
                                extras=['fenced-code-blocks', 'pygments', 'break-on-newline'])
    html_text = html_text.replace('<a ', '<a target="_blank" ')
    html_text = f"""<!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>{title}</title>\n<meta name="description" content="{description}">
            <meta name="keywords" content="{keywords}">
            {styles.fonts}
            {styles.bootstrap}
            <style>
            {styles.css}
            {pygments_css}
            </style>    

        <!-- Google Analytics -->
        
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-21L9B7E4DJ"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          const gtag = () => dataLayer.push(arguments)
          gtag("js", new Date());
        
          gtag("config", "G-21L9B7E4DJ");
        </script>
    
        <!-- END Google Analytics   -->

        </head>
            <body class="container">
                {html_text}
            </body>
        </html>
        """
    md_filename = md_path.split('.')[0]
    html_filename = f"{md_filename}.html"
    dir_name = md_filename
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    html_filename = os.path.join(dir_name, "index.html")
    with open(html_filename, 'w') as f:
        f.write(html_text)
    meta_filename = os.path.join(dir_name, "me.ta")
    with open(meta_filename, 'w') as f:
        f.write(f"title={title}\ndescription={description}\nkeywords={keywords}\ndate={date}\n")
    end_time = time.time()
    total_time_ms = int((end_time - start_time) * 1000)
    print(f"Compilation finished in {total_time_ms} ms")
