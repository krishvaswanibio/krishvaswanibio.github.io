<!DOCTYPE html>
<html>

{% if site.title and site.title != page.title %}
<h1><a href="{{ "/" | absolute_url }}">{{ site.title }}</a></h1>
{% endif %}


<body style="background-color: powderblue;">
<h1>Krish Vaswani</h1>
 <br>
</body>

<body>
<p1><i>I am a human being who loves computer science.</i></p1>
<br>
<p2>Play around with this website to learn more about me.</p2>
<br>
<p3>The code for this page is attached in a github page below. I personally prefer to write more dynamic websites, using flask, python, html, css, and javascript, but I had to make a more static website.</p3>
<a href="https://github.com/krishvaswanibio/krishvaswanibio.github.io"><br>Github</a>
</body>

<body>
<br>
<button id="alertButton" type="button">Click Here if you love the website!</button>
    <script>
    const button = document.getElementById('alertButton');
        //I love writing readable code :)
        button.addEventListener('click', () => {
            alert('I love it.');
        });
     </script>
</body>

</html>
