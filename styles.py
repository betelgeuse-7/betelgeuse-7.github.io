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
  background-color: #6c8f5b;
  color: black;
}

html {
    border-left: 2.3em solid #6c8f5b;
    border-right: 0.5em solid #a5d190;
}

body {
    font-family: 'Merriweather', serif;
    background-color: #faf9b9;
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
    margin-bottom: 1rem;
}

h2, h3, h4, h5, h6 {
    background-color: #c4e8b3;
}

h1 {
    font-size: 3rem;
}

h1::after {
    content: " ✦";
    color: #6c8f5b;
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

li::before {    
  content: "⬊ ";
  color: #359e02;
  font-weight: bold;
  margin-left: -2em;
}

li {
    margin-bottom: 0.5rem;
}

::-webkit-scrollbar {
  width: 4px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
  background: #a5d190;
}

::-webkit-scrollbar-thumb:hover {
  background: #568241;
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

::-webkit-scrollbar {
  width: 4px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
  background: #a5d190;
}

::-webkit-scrollbar-thumb:hover {
  background: #568241;
}

"""