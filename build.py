# Genera todas las páginas del sitio en español (raíz) e inglés (/en/).
# Uso: python3 build.py
import os

T = {
 "es": dict(
  base="", lang="es",
  nav=[("", "Inicio"), ("nosotros/", "Nosotros"), ("recursos/", "Recursos"), ("videos/", "Videos"), ("contacto/", "Contacto")],
  footer_tag="Encendiendo corazones para Cristo en Estados Unidos, México y Sudamérica.",
  nav_h="Navegación", contact_h="Contacto", country="México", rights="© 2026 NewFire. Todos los derechos reservados.",
 ),
 "en": dict(
  base="en/", lang="en",
  nav=[("", "Home"), ("about/", "About"), ("resources/", "Resources"), ("videos/", "Videos"), ("contact/", "Contact")],
  footer_tag="Igniting hearts for Christ across the United States, Mexico, and South America.",
  nav_h="Navigation", contact_h="Contact", country="Mexico", rights="© 2026 NewFire. All rights reserved.",
 ),
}
PAGES = ["", "about", "resources", "videos", "contact"]  # orden igual al menú

def write(lang, idx, title, desc, body):
    L = T[lang]
    slug = L["nav"][idx][0]
    path = L["base"] + slug
    up = "../" * path.count("/") or "./"
    nav = "".join(f'<a href="{up}{L["base"]}{s}"{" aria-current=page" if i == idx else ""}>{t}</a>' for i, (s, t) in enumerate(L["nav"]))
    es_href = up + T["es"]["nav"][idx][0]
    en_href = up + "en/" + T["en"]["nav"][idx][0]
    fnav = "".join(f'<li><a href="{up}{L["base"]}{s}">{t}</a></li>' for s, t in L["nav"])
    body = body.replace("{up}", up).replace("{root}", up + L["base"])
    html = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{up}assets/img/favicon.png">
<link rel="alternate" hreflang="es" href="https://newfire.mx/{T['es']['nav'][idx][0]}">
<link rel="alternate" hreflang="en" href="https://newfire.mx/en/{T['en']['nav'][idx][0]}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;1,400&family=Nunito:wght@400;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<header class="site-header"><div class="wrap bar">
<a class="brand" href="{up}{L['base']}" aria-label="NewFire"><img src="{up}assets/img/logo.png" alt="NewFire"></a>
<nav class="nav">{nav}</nav>
<div class="langs"><a href="{en_href}" hreflang="en"{" aria-current=true" if lang=="en" else ""}>EN</a><a href="{es_href}" hreflang="es"{" aria-current=true" if lang=="es" else ""}>ES</a></div>
</div></header>
<main>
{body}
</main>
<footer class="site-footer"><div class="wrap fgrid">
<div><div class="logo-box"><img src="{up}assets/img/logo-full.png" alt="NewFire"></div><p>{L['footer_tag']}</p></div>
<div><h4>{L['nav_h']}</h4><ul>{fnav}</ul></div>
<div><h4>{L['contact_h']}</h4><ul><li>{L['country']}</li><li><a href="mailto:info@newfire.mx">info@newfire.mx</a></li></ul></div>
</div><div class="copy">{L['rights']}</div></footer>
<script src="{up}assets/content.js"></script>
<script src="{up}assets/site.js"></script>
</body>
</html>
"""
    os.makedirs(path or ".", exist_ok=True)
    with open(os.path.join(path, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

def cards(items, link, more):
    return "".join(f'<div class="card"><div class="icon" aria-hidden="true">{i}</div><h3>{h}</h3><p>{p}</p><a class="more" href="{link}">{more} →</a></div>' for i, h, p in items)

# ---------------- Recursos (contenido real de NEWFIRE) ----------------
# (categoría, formato, título ES, texto ES, título EN, texto EN, tipo) tipo: video | solicitar
RES = [
 ("study", "Video", "Bendiciones, obras y fe", "Serie basada en el Evangelio de Mateo sobre cómo vemos la bendición de Dios y la fe que se demuestra con obras.",
  "Blessings, Works and Faith", "A series from the Gospel of Matthew on how we see God's blessing and a faith shown by works.", "video"),
 ("study", "Video", "El mensaje de Miqueas", "Un recorrido por el libro del profeta Miqueas: justicia, misericordia y humildad delante de Dios.",
  "The Message of Micah", "A journey through the book of the prophet Micah: justice, mercy, and walking humbly with God.", "video"),
 ("study", "Video", "El libro de Nahúm", "La justicia de Dios y su refugio para quienes confían en Él, contados en una narración visual.",
  "The Book of Nahum", "God's justice and His refuge for those who trust Him, told as a visual narrative.", "video"),
 ("study", "PDF", "La vida cristiana: 1 Juan", "Estudio de la primera carta de Juan sobre la comunión con Dios, el amor y la seguridad de la salvación.",
  "The Christian Life: 1 John", "A study of John's first letter on fellowship with God, love, and the assurance of salvation.", "solicitar"),
 ("study", "PDF", "Profetas: Isaías, Jeremías y Ezequiel", "Estudios sobre la visión de Isaías 6, Baruc en Jeremías 45 y la gloria de Dios en Ezequiel.",
  "Prophets: Isaiah, Jeremiah and Ezekiel", "Studies on Isaiah's vision in chapter 6, Baruch in Jeremiah 45, and God's glory in Ezekiel.", "solicitar"),
 ("series", "Serie en video", "Senderos de Luz", "Historias de fe para toda la familia que muestran la Biblia en la vida diaria.",
  "Paths of Light", "Faith stories for the whole family that bring the Bible into everyday life.", "video"),
 ("prayer", "Video", "Jesucristo te espera", "Una invitación a volver a casa y encontrar en Jesús perdón y una vida nueva.",
  "Jesus Christ Is Waiting", "An invitation to come home and find forgiveness and new life in Jesus.", "video"),
 ("prayer", "Video", "Salmo 23: El Pastor", "Meditación sobre el Señor como nuestro pastor, para descansar y confiar en Él.",
  "Psalm 23: The Shepherd", "A meditation on the Lord as our shepherd, to rest and trust in Him.", "video"),
 ("novel", "Novela", "La voz que estremece los huesos", "Novela bíblica en tres libros. Libro I: «La promesa que tardó». Próximamente.",
  "The Voice That Shakes the Bones", "A biblical novel in three books. Book I: “The Promise That Tarried”. Coming soon.", "solicitar"),
]
CATS = {"es": [("all", "Todos"), ("study", "Estudio bíblico"), ("series", "Series"), ("prayer", "Oración"), ("novel", "Novelas")],
        "en": [("all", "All"), ("study", "Bible Study"), ("series", "Series"), ("prayer", "Prayer"), ("novel", "Novels")]}
FMT_EN = {"Video": "Video", "PDF": "PDF", "Serie en video": "Video series", "Novela": "Novel"}

def resources(lang):
    names = dict(CATS[lang])
    chips = "".join(f'<button class="chip" type="button" data-cat="{k}" aria-pressed="{"true" if k=="all" else "false"}">{v}</button>' for k, v in CATS[lang])
    out = []
    for cat, fmt, tes, pes, ten, pen, kind in RES:
        t, p = (tes, pes) if lang == "es" else (ten, pen)
        f = fmt if lang == "es" else FMT_EN[fmt]
        if kind == "video":
            btn = f'<a class="btn btn-flame" href="{{root}}videos/">{"Ver videos" if lang=="es" else "Watch"}</a>'
            foot = "Gratis" if lang == "es" else "Free"
        else:
            page = "contacto/" if lang == "es" else "contact/"
            btn = f'<a class="btn btn-flame" href="{{root}}{page}?asunto=resources">{"Solicitar" if lang=="es" else "Request"}</a>'
            foot = "Por correo" if lang == "es" else "By email"
        out.append(f'<article class="card res" data-cat="{cat}"><div class="tags"><span class="tag">{names[cat]}</span><span class="fmt">{f}</span></div><h3>{t}</h3><p>{p}</p><div class="foot"><span>{foot}</span>{btn}</div></article>')
    return f'<div class="chips" role="group">{chips}</div><div class="grid-3">{"".join(out)}</div>'

def hero(img, eyebrow, h1, p, extra="", page=True):
    return f'<section class="hero{" page" if page else ""}" style="background-image:url({{up}}assets/img/{img})"><div class="wrap"><div class="hero-inner"><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p>{p}</p>{extra}</div></div></section>'

def verse(q, ref, light=False):
    return f'<section class="verse {"light" if light else "band on-dark"}"><div class="wrap"><blockquote>{q}<cite>{ref}</cite></blockquote></div></section>'

for lang in ("es", "en"):
    es = lang == "es"
    R = "{root}"
    res_slug, about_slug, contact_slug = (("recursos/", "nosotros/", "contacto/") if es else ("resources/", "about/", "contact/"))

    # ---------- Inicio / Home ----------
    cat_items = [
     ("📖", "Estudios bíblicos" if es else "Bible Studies", "Guías profundas para conocer la Palabra de Dios, desde la fe básica hasta la teología avanzada." if es else "In-depth guides for knowing the Word of God, from foundational faith to advanced theology."),
     ("🎵", "Música de adoración" if es else "Worship Music", "Letras, partituras y recursos de adoración para enriquecer tu tiempo de oración y alabanza." if es else "Lyrics, sheet music, and worship resources to enrich your time of prayer and praise."),
     ("🙏", "Guías de oración" if es else "Prayer Guides", "Planes devocionales y modelos de oración para fortalecer tu vida espiritual y tu relación con Dios." if es else "Devotional plans and prayer models to strengthen your spiritual life and relationship with God."),
     ("👨‍👩‍👧", "Familia y fe" if es else "Family and Faith", "Recursos para familias: devocionales, actividades y materiales para crecer juntos en la fe." if es else "Resources for families: devotionals, activities, and materials to grow together in faith."),
     ("✝️", "Evangelismo" if es else "Evangelism", "Herramientas prácticas para compartir el Evangelio con tu comunidad, familia y amigos." if es else "Practical tools for sharing the Gospel with your community, family, and friends."),
     ("🌱", "Discipulado" if es else "Discipleship", "Materiales para el crecimiento espiritual y la formación de nuevos creyentes en la fe cristiana." if es else "Materials for spiritual growth and the formation of new believers in the Christian faith."),
    ]
    home = hero("hero-home.jpg",
        "Bienvenidos a NewFire México" if es else "Welcome to NewFire",
        ("Encendiendo Corazones <em>para Cristo</em>" if es else "Setting Hearts on Fire <em>for Christ</em>"),
        ("Recursos cristianos en español e inglés para equipar, inspirar y transformar vidas en los Estados Unidos, México, Sudamérica y el Mundo." if es else
         "Free Christian resources in English and Spanish to equip, inspire, and transform lives across the United States, Mexico, South America, and the World."),
        f'<div class="actions"><a class="btn btn-flame" href="{R}{res_slug}">{"Explorar Recursos" if es else "Explore Resources"}</a><a class="link-under" href="#mision">{"Conoce nuestra misión" if es else "Learn about our mission"}</a></div>', page=False)
    home += verse("“Porque yo sé los pensamientos que tengo acerca de vosotros, dice Jehová, pensamientos de paz, y no de mal, para daros el fin que esperáis.”" if es else
                  "“For I know the plans I have for you,” declares the Lord, “plans to prosper you and not to harm you, plans to give you hope and a future.”",
                  "Jeremías 29:11" if es else "Jeremiah 29:11")
    home += f'''<section id="mision"><div class="wrap split">
<div class="photo"><img src="{{up}}assets/img/mission.jpg" alt="" loading="lazy"><span class="badge">▲ {"Desde 2020" if es else "Est. 2020"}</span></div>
<div><p class="eyebrow">{"Nuestra misión" if es else "Our mission"}</p><h2>{"Un fuego nuevo para las Américas" if es else "A new fire for the Americas"}</h2>
<p>{"NewFire nació con un propósito claro: llevar recursos cristianos de calidad a cada hogar, iglesia y corazón en Estados Unidos, México y Sudamérica. Creemos que la Palabra de Dios tiene el poder de transformar vidas." if es else "NewFire was born with one clear purpose: to bring quality Christian resources to every home, church, and heart across the United States, Mexico, and South America. We believe the Word of God has the power to transform lives."}</p>
<p>{"Desde estudios bíblicos hasta materiales de evangelismo, todo lo que encuentras aquí ha sido preparado con oración y amor, para que crezcas en tu fe y la compartas con otros." if es else "From Bible studies to evangelism materials, everything you find here has been prepared with prayer and love, so that you can grow in your faith and share it with others."}</p>
<p style="margin-top:30px"><a class="btn btn-flame" href="{R}{about_slug}">{"Conoce más de nosotros" if es else "Learn more about us"}</a></p></div>
</div></section>
<section class="alt"><div class="wrap center"><h2>{"Todo lo que necesitas para crecer en la fe" if es else "Everything you need to grow in faith"}</h2>
<p class="lead">{"Materiales diseñados para apoyar tu vida espiritual, tu iglesia y tu familia." if es else "Materials designed to support your spiritual life, your church, and your family."}</p>
<div class="grid-3" style="text-align:left">{cards(cat_items, R + res_slug, "Ver recursos" if es else "View resources")}</div>
<p style="margin-top:48px"><a class="btn btn-flame" href="{R}{res_slug}">{"Ver todos los recursos" if es else "View all resources"}</a></p></div></section>
<section><div class="wrap center"><p class="eyebrow">{"Videos" if es else "Videos"}</p><h2>{"Videos recientes" if es else "Latest videos"}</h2>
<div class="vgrid" data-videos="6"></div><p style="margin-top:44px"><a class="btn btn-outline" href="{R}videos/">{"Ver todos los videos" if es else "See all videos"}</a></p></div></section>
<section class="photo-band" style="background-image:url({{up}}assets/img/community.jpg)"><div class="wrap"><h2>{"Únete a la comunidad NewFire" if es else "Join the NewFire community"}</h2>
<p>{"Miles de creyentes en Estados Unidos, México y Sudamérica creciendo juntos en la fe." if es else "Thousands of believers across the United States, Mexico, and South America growing together in faith."}</p>
<a class="btn btn-gold" href="{R}{contact_slug}">{"Contáctanos hoy" if es else "Contact us today"}</a></div></section>
<section class="band on-dark center"><div class="wrap"><div class="flame-mark" aria-hidden="true">▲</div><h2>{"¿Listo para encender tu fe?" if es else "Ready to ignite your faith?"}</h2>
<p class="lead" style="margin-bottom:32px">{"Descubre todos nuestros recursos o ponte en contacto con nuestro equipo." if es else "Discover all our resources or get in touch with our team."}</p>
<div class="actions" style="justify-content:center"><a class="btn btn-flame" href="{R}{res_slug}">{"Ver Recursos" if es else "View Resources"}</a><a class="btn btn-outline" href="{R}{contact_slug}">{"Contáctanos" if es else "Contact Us"}</a></div></div></section>'''
    write(lang, 0, "NewFire México – Recursos cristianos" if es else "NewFire – Free Christian Resources",
          "Recursos cristianos gratuitos en español e inglés." if es else "Free Christian resources in English and Spanish.", home)

    # ---------- Nosotros / About ----------
    vals = [("▲", "La Palabra de Dios" if es else "The Word of God", "Creemos que la Biblia es la Palabra inspirada de Dios, la autoridad final para la fe y la vida cristiana." if es else "We believe the Bible is the inspired Word of God, the ultimate authority for faith and Christian life."),
            ("♥", "Amor al prójimo" if es else "Love for Others", "Servimos a nuestra comunidad con amor genuino, siguiendo el ejemplo de Cristo en cada acción y recurso." if es else "We serve our community with genuine love, following the example of Christ in every action and resource."),
            ("☆", "Excelencia" if es else "Excellence", "Todo lo que hacemos, lo hacemos con excelencia, ofreciendo recursos de calidad que honren a Dios." if es else "Everything we do, we do with excellence, offering quality resources that honor God."),
            ("👥", "Comunidad" if es else "Community", "Creemos en el cuerpo de Cristo. Cada creyente tiene un lugar y un propósito en la familia de Dios." if es else "We believe in the body of Christ. Every believer has a place and a purpose in the family of God.")]
    about = hero("hero-about.jpg", "Nuestra historia" if es else "Our story", "Sobre NewFire" if es else "About NewFire",
                 "Conoce quiénes somos, de dónde venimos y hacia dónde vamos." if es else "Learn who we are, where we come from, and where we are going.")
    about += f'''<section><div class="wrap split">
<div><p class="eyebrow">{"Cómo empezamos" if es else "How we started"}</p><h2>{"Un llamado, una llama" if es else "A calling, a flame"}</h2>
<p>{"NewFire nació en 2020 de la visión de un grupo de creyentes en la Ciudad de México que soñaban con un ministerio que llegara a cada rincón del país. En un mundo donde la información abunda pero los recursos espirituales confiables escasean, sentimos que Dios nos llamaba a hacer algo diferente." if es else "NewFire was born in 2020 from the vision of a group of believers in Mexico City who dreamed of a ministry that would reach every corner of the country. In a world where information is abundant but trustworthy spiritual resources are scarce, we felt God calling us to do something different."}</p>
<p>{"Hoy compartimos estudios bíblicos, series en video, oraciones y novelas bíblicas en español e inglés, para que la Palabra llegue a más personas." if es else "Today we share Bible studies, video series, prayers, and biblical novels in Spanish and English, so the Word can reach more people."}</p></div>
<div class="photo"><img src="{{up}}assets/img/mission.jpg" alt="" loading="lazy"></div></div></section>
<section class="band on-dark center"><div class="wrap"><p class="eyebrow">{"Nuestra misión" if es else "Our mission"}</p>
<blockquote style="margin:0 auto 22px;max-width:780px;font:italic 600 clamp(26px,3.4vw,40px)/1.25 var(--display);color:#fbf1e6">{"Equipar al pueblo de Dios en Estados Unidos, México y Sudamérica con recursos que transforman vidas." if es else "To equip the people of God across the United States, Mexico, and South America with resources that transform lives."}</blockquote>
<p class="lead">{"Cada recurso que creamos, cada guía que publicamos y cada comunidad que formamos tiene un solo propósito: que más personas conozcan, amen y sirvan a Jesucristo." if es else "Every resource we create, every guide we publish, and every community we form has one single purpose: that more people across the United States, Mexico, and South America come to know, love, and serve Jesus Christ."}</p></div></section>
<section class="alt"><div class="wrap center"><p class="eyebrow">{"Lo que nos mueve" if es else "What drives us"}</p><h2>{"Nuestros valores" if es else "Our Values"}</h2>
<div class="grid-4">{"".join(f'<div class="card value"><div class="icon" aria-hidden="true">{i}</div><h3>{h}</h3><p>{p}</p></div>' for i,h,p in vals)}</div></div></section>
<section class="band on-dark center"><div class="wrap"><h2>{"¿Quieres ser parte?" if es else "Want to be part of it?"}</h2>
<p class="lead" style="margin-bottom:30px">{"Hay un lugar para ti en la familia NewFire. Juntos podemos encender más vidas para Cristo." if es else "There is a place for you in the NewFire family. Together we can ignite more lives for Christ."}</p>
<a class="btn btn-flame" href="{R}{contact_slug}">{"Contáctanos" if es else "Contact Us"}</a></div></section>'''
    write(lang, 1, "Nosotros – NewFire" if es else "About – NewFire", "Quiénes somos." if es else "Who we are.", about)

    # ---------- Recursos / Resources ----------
    resp = hero("hero-resources.jpg", "Biblioteca" if es else "Library", "Recursos gratuitos" if es else "Free Resources",
                "Materiales bíblicos, de oración y discipulado para equiparte a ti, a tu familia y a tu iglesia." if es else "Biblical, prayer, and discipleship materials to equip you, your family, and your church.")
    resp += f'<section><div class="wrap">{resources(lang)}</div></section>'
    resp += verse("“Toda la Escritura es inspirada por Dios, y útil para enseñar, para redargüir, para corregir, para instruir en justicia.”" if es else
                  "“All Scripture is God-breathed and is useful for teaching, rebuking, correcting and training in righteousness.”",
                  "2 Timoteo 3:16" if es else "2 Timothy 3:16", light=True)
    write(lang, 2, "Recursos – NewFire" if es else "Resources – NewFire", "Recursos cristianos gratuitos." if es else "Free Christian resources.", resp)

    # ---------- Videos ----------
    vid = hero("hero-home.jpg", "NewFire TV", "Videos",
               "Enseñanzas bíblicas, series y reflexiones para fortalecer tu fe. Míralos y compártelos." if es else "Bible teachings, series, and reflections to strengthen your faith. Watch and share them.")
    vid += '<section><div class="wrap"><div class="vgrid" data-videos></div></div></section>'
    write(lang, 3, "Videos – NewFire", "Videos de NewFire." if es else "NewFire videos.", vid)

    # ---------- Contacto / Contact ----------
    opts = [("resources", "Recursos" if es else "Resources"), ("prayer", "Petición de oración" if es else "Prayer request"),
            ("join", "Quiero unirme a NewFire" if es else "I want to join NewFire"), ("other", "Otro" if es else "Other")]
    con = hero("hero-contact.jpg", "Escríbenos" if es else "Write to us", "Contáctanos" if es else "Contact Us",
               "¿Tienes una pregunta, necesitas oración o quieres unirte a NewFire? Aquí estamos." if es else "Have a question, need prayer, or want to join NewFire? We are here.")
    con += f'''<section><div class="wrap contact-grid">
<div><h2>{"Estamos aquí para ti" if es else "We are here for you"}</h2>
<p>{"Ya sea que busques recursos, necesites oración o quieras unirte a nuestro equipo, nos encanta saber de ti." if es else "Whether you are looking for resources, need prayer, or want to join our team, we love hearing from you."}</p>
<ul class="info">
<li><span class="ico" aria-hidden="true">📍</span><span class="lbl">{"Ubicación" if es else "Location"}</span><span class="val">{"Ciudad de México, México" if es else "Mexico City, Mexico"}</span></li>
<li><span class="ico" aria-hidden="true">💌</span><span class="lbl">{"Correo" if es else "Email"}</span><span class="val"><a href="mailto:info@newfire.mx">info@newfire.mx</a></span></li>
<li><span class="ico" aria-hidden="true">🕒</span><span class="lbl">{"Horario" if es else "Response hours"}</span><span class="val">{"Siempre estamos disponibles,<br><em>si el enemigo no descansa, nosotros tampoco.</em>" if es else "We are always open,<br><em>if the enemy doesn't rest, neither should we.</em>"}</span></li>
</ul>
<div class="side-quote">{"“Clama a mí, y yo te responderé, y te enseñaré cosas grandes y ocultas que tú no conoces.”" if es else "“Call to me and I will answer you and tell you great and unsearchable things you do not know.”"}<cite>{"Jeremías 33:3" if es else "Jeremiah 33:3"}</cite></div></div>
<form class="form"><h3 style="font-size:26px;margin-bottom:26px">{"Envíanos un mensaje" if es else "Send us a message"}</h3>
<div class="row"><div class="f"><label for="fullname">{"Nombre completo" if es else "Full name"} *</label><input id="fullname" name="fullname" required placeholder="{"Tu nombre" if es else "Your name"}"></div>
<div class="f"><label for="email">{"Correo electrónico" if es else "Email address"} *</label><input id="email" name="email" type="email" required placeholder="{"tu@correo.com" if es else "you@email.com"}"></div></div>
<div class="row"><div class="f"><label for="phone">{"Teléfono" if es else "Phone"} <small>({"opcional" if es else "optional"})</small></label><input id="phone" name="phone" type="tel" placeholder="+52 55 0000 0000"></div>
<div class="f"><label for="subject">{"Asunto" if es else "Subject"} *</label><select id="subject" name="subject" required>{"".join(f'<option value="{v}">{t}</option>' for v,t in opts)}</select></div></div>
<div class="f"><label for="message">{"Mensaje" if es else "Message"} *</label><textarea id="message" name="message" required placeholder="{"¿Cómo podemos ayudarte?" if es else "How can we help you?"}"></textarea></div>
<button class="btn btn-flame" type="submit">{"Enviar mensaje" if es else "Send message"}</button>
<p class="note">{"Se abrirá tu aplicación de correo con el mensaje listo para enviar a info@newfire.mx." if es else "Your email app will open with the message ready to send to info@newfire.mx."}</p></form>
</div></section>'''
    write(lang, 4, "Contacto – NewFire" if es else "Contact – NewFire", "Contáctanos." if es else "Contact us.", con)
