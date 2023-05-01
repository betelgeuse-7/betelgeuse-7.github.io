import styles, os, sys, datetime, string

TITLE = "[BLOG] betelgeuse-7"

def make_post_list():
    posts = []
    directories = [f.name for f in os.scandir(".") if f.is_dir()]

    for d in directories:
        if d in string.punctuation or d.startswith("_"):
            continue
        meta_file = os.path.join(d, "me.ta")
        
        if not os.path.exists(meta_file):
            continue

        with open(meta_file, 'r') as f:
            contents = f.read()
            dictionary = {}
            for line in contents.splitlines():
                splitted = line.split("=")
                k, v = splitted[0], splitted[1]
                dictionary[k] = v
            dictionary["url"] = d
            posts.append(dictionary)
        
    html = ""
    for p in posts:
        human_date = datetime.datetime.strptime(p["date"], '%d-%m-%Y').strftime('%B %d, %Y')
        html += f'<a class="post" target="_blank" href={p["url"]}>{p["title"]}</a><p class="date">{human_date}</p>'

    return (html, "No posts" if len(posts) == 0 else "Come in")

(posts_html, posts_title) = make_post_list()

index = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {styles.fonts}
    {styles.bootstrap}
    <style>
    {styles.index_css}

    </style>
    <title>{TITLE}</title>
</head>
<body class="container">
    <header>
    <h2 id="title">Abidin Durdu (betelgeuse-7)</h2>
    <div>
        <a class="link-primary link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover" target="_blank" href="https://github.com/betelgeuse-7/">Github (betelgeuse-7)</a>
    </div>
    <div>
        <a class="link-primary link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover" target="_blank" href="https://twitter.com/abidindrd_">Twitter (abidindrd_)</a>
    </div>
    <div>
        <h2>{posts_title}</h2>
    </div>

    {posts_html}
    
    </header>
</body>
</html>
"""

def make_index():
    with open("index.html", 'w') as f:
        f.write(index)
    print("Built index.html")
