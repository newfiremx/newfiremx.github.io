# Genera las páginas HTML del sitio. Uso: python3 build.py
import os

LANGS = {
    "es": {
        "html": "es", "base": "",
        "nav": [("", "Inicio"), ("videos/", "Videos"), ("libros/", "Libros y novelas"), ("estudios/", "Estudios bíblicos")],
        "other": ("en/", "English"),
        "tagline": "Equipar, inspirar y transformar",
        "footer": "NEWFIRE México · Recursos cristianos gratuitos",
        "sub": "Suscríbete en YouTube",
    },
    "en": {
        "html": "en", "base": "en/",
        "nav": [("", "Home"), ("videos/", "Videos"), ("books/", "Books & novels"), ("studies/", "Bible studies")],
        "other": ("", "Español"),
        "tagline": "Equip, inspire & transform",
        "footer": "NEWFIRE Mexico · Free Christian resources",
        "sub": "Subscribe on YouTube",
    },
}
YOUTUBE = "https://www.youtube.com/@newfiremx"  # TODO: confirmar el canal

def page(lang, slug, title, body):
    L = LANGS[lang]
    path = L["base"] + slug
    depth = path.count("/")
    up = "../" * depth or "./"
    nav = "".join(
        f'<a href="{up}{L["base"]}{s}"{" aria-current=page" if s == slug else ""}>{t}</a>'
        for s, t in L["nav"])
    other_slug = LANGS["en" if lang == "es" else "es"]["nav"][[s for s, _ in L["nav"]].index(slug)][0]
    other = f'<a class="lang" href="{up}{L["other"][0]}{other_slug}" hreflang="{"en" if lang=="es" else "es"}">{L["other"][1]}</a>'
    html = f"""<!doctype html>
<html lang="{L['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · NEWFIRE</title>
<meta name="description" content="{L['tagline']}. {L['footer']}.">
<link rel="icon" href="{up}assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Lora:wght@600&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<header><div class="wrap bar">
<a class="brand" href="{up}{L['base']}"><img src="{up}assets/img/logo.png" alt="">NEWFIRE</a>
<nav>{nav}{other}</nav>
</div></header>
<main>
{body.replace('{up}', up).replace('{sub}', L['sub']).replace('{yt}', YOUTUBE)}
</main>
<footer><div class="wrap">{L['footer']}</div></footer>
<script src="{up}assets/content.js"></script>
<script src="{up}assets/site.js"></script>
</body>
</html>
"""
    os.makedirs(path or ".", exist_ok=True)
    with open(os.path.join(path, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

SUBBTN = '<p class="center"><a class="btn" href="{yt}" target="_blank" rel="noopener">{sub}</a></p>'

# ---------- Español ----------
page("es", "", "Inicio", f"""
<div class="hero"><img src="{{up}}assets/img/banner.jpg" alt="NEWFIRE: fe, paz y ánimo desde las Escrituras"></div>
<div class="wrap intro"><h1>Fe, paz y ánimo desde las Escrituras</h1>
<p>Videos, series, libros y estudios bíblicos gratuitos para equipar, inspirar y transformar vidas en México y América Latina.</p></div>
<section class="wrap"><h2>Videos recientes</h2><div class="grid" data-videos="6"></div>
<p class="center"><a class="btn" href="{{up}}videos/">Ver todos los videos</a></p></section>
<section class="wrap"><div class="cards">
<div class="card"><h3><a href="{{up}}libros/">Libros y novelas</a></h3><p>Historias bíblicas contadas como novela, como «La voz que estremece los huesos».</p></div>
<div class="card"><h3><a href="{{up}}estudios/">Estudios bíblicos</a></h3><p>Series de estudio sobre Mateo, Miqueas, Nahúm, Salmos y más.</p></div>
<div class="card"><h3><a href="{{up}}videos/">Senderos de Luz</a></h3><p>Nuestra serie de historias de fe para toda la familia.</p></div>
</div></section>""")

page("es", "videos/", "Videos", f"""
<div class="wrap intro"><h1>Videos</h1><p>Enseñanzas bíblicas, series y reflexiones para fortalecer tu fe. Míralos, compártelos y suscríbete para no perderte ninguno.</p></div>
<section class="wrap"><div class="grid" data-videos></div>{SUBBTN}</section>""")

page("es", "libros/", "Libros y novelas", """
<div class="wrap intro"><h1>Libros y novelas</h1><p>Historias de la Biblia contadas con el corazón de una novela.</p></div>
<section class="wrap"><div class="cards">
<div class="card"><h3>La voz que estremece los huesos</h3><p>Próximamente. Libro I: «La promesa que tardó».</p></div>
</div></section>""")

page("es", "estudios/", "Estudios bíblicos", """
<div class="wrap intro"><h1>Estudios bíblicos</h1><p>Estudios por libro de la Biblia, con video y material para leer.</p></div>
<section class="wrap"><div class="cards">
<div class="card"><h3>Bendiciones, obras y fe</h3><p>Serie basada en el Evangelio de Mateo. Próximamente.</p></div>
<div class="card"><h3>El libro de Miqueas</h3><p>Próximamente.</p></div>
<div class="card"><h3>El libro de Nahúm</h3><p>Próximamente.</p></div>
</div></section>""")

# ---------- English ----------
page("en", "", "Home", f"""
<div class="hero"><img src="{{up}}assets/img/banner.jpg" alt="NEWFIRE: Faith, peace and encouragement from Scripture"></div>
<div class="wrap intro"><h1>Faith, peace and encouragement from Scripture</h1>
<p>Free videos, series, books and Bible studies to equip, inspire and transform lives.</p></div>
<section class="wrap"><h2>Latest videos</h2><div class="grid" data-videos="6"></div>
<p class="center"><a class="btn" href="{{up}}en/videos/">See all videos</a></p></section>
<section class="wrap"><div class="cards">
<div class="card"><h3><a href="{{up}}en/books/">Books & novels</a></h3><p>Bible stories told as novels, like "The Voice That Shakes the Bones".</p></div>
<div class="card"><h3><a href="{{up}}en/studies/">Bible studies</a></h3><p>Study series on Matthew, Micah, Nahum, Psalms and more.</p></div>
<div class="card"><h3><a href="{{up}}en/videos/">Paths of Light</a></h3><p>Our series of faith stories for the whole family.</p></div>
</div></section>""")

page("en", "videos/", "Videos", f"""
<div class="wrap intro"><h1>Videos</h1><p>Bible teachings, series and reflections to strengthen your faith. Watch, share, and subscribe so you never miss one.</p></div>
<section class="wrap"><div class="grid" data-videos></div>{SUBBTN}</section>""")

page("en", "books/", "Books & novels", """
<div class="wrap intro"><h1>Books & novels</h1><p>Bible stories told with the heart of a novel.</p></div>
<section class="wrap"><div class="cards">
<div class="card"><h3>The Voice That Shakes the Bones</h3><p>Coming soon. Book I: "The Promise That Tarried".</p></div>
</div></section>""")

page("en", "studies/", "Bible studies", """
<div class="wrap intro"><h1>Bible studies</h1><p>Studies by book of the Bible, with video and reading material.</p></div>
<section class="wrap"><div class="cards">
<div class="card"><h3>Blessings, Works and Faith</h3><p>A series based on the Gospel of Matthew. Coming soon.</p></div>
<div class="card"><h3>The Book of Micah</h3><p>Coming soon.</p></div>
<div class="card"><h3>The Book of Nahum</h3><p>Coming soon.</p></div>
</div></section>""")
