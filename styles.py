fonts="""
<!-- Title font -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500&display=swap" rel="stylesheet">

<!-- Paragraph font -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@300&display=swap" rel="stylesheet">

<!-- Code font -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@300;400&display=swap" rel="stylesheet">
"""

bootstrap="""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
"""

css="""
::selection {
  background-color: #fcbe95;
  color: black;
}

html {
    border-left: 5px solid #bc6ded;
}

body {
    font-family: 'Merriweather', serif;
    background-color: #fbfcf2;
}

.codehilite {
    font-family: 'Source Code Pro', monospace;
    padding: 0.5rem;
    border-top: 0.12rem solid #bc6ded;
    border-bottom: 0.12rem solid #bc6ded;
    margin: 0.4rem;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    background-color: #fffaed;
    margin-bottom: 1rem;
}

h1 {
    font-size: 3rem;
}

h1::after {
    content: " ✧";
    color: #bc6ded;
}

a {
    font-size: 1.1rem;
    font-style: italic;
}

a:hover {
    font-size: 1.11rem;
    color: #fa8d34;
}

ul {
    list-style: none;
}

ul li::before {
  content: "::> ";
  color: #6200a8;
  font-weight: bold;
  display: inline-block;
  width: 2em;
  margin-left: -1em;
  margin-right: 0.5rem;
}

li {
    margin-bottom: 0.5rem;
}
"""

index_css = """
body {
    font-family: 'Merriweather', serif;
    background-color: #fceede;
    margin-top: 2rem;
}

h1, h2, h3, h4, h5, h6 {
    font-family: monospace;
    font-style: italic;
    margin-bottom: 1rem;
    margin-top: 3rem;
}

#title {
    background-color: #cfdefa;
    font-size: 3rem;
    display: inline-block;
    padding: 0.15rem 1rem 0.15rem 1rem;
}

.post {
    font-size: 1.2rem;
}

.date {
    font-size: 0.8rem;
    color: black;
}
"""