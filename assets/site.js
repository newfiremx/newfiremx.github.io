(function () {
  // Videos: thumbnail first, YouTube player loads on click.
  document.querySelectorAll("[data-videos]").forEach(function (grid) {
    var limit = parseInt(grid.getAttribute("data-videos"), 10) || 0;
    var lang = document.documentElement.lang === "en" ? "en" : "es";
    var ids = window.NEWFIRE.videos[lang] || [];
    if (limit) ids = ids.slice(0, limit);
    ids.forEach(function (v) {
      var id = v.id;
      var fig = document.createElement("figure");
      fig.className = "vcard";
      var card = document.createElement("div");
      card.className = "video";
      var btn = document.createElement("button");
      btn.type = "button";
      btn.setAttribute("aria-label", v.title);
      btn.style.backgroundImage = "url(https://i.ytimg.com/vi/" + id + "/hqdefault.jpg)";
      btn.addEventListener("click", function () {
        var f = document.createElement("iframe");
        f.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0";
        f.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
        f.allowFullscreen = true;
        f.title = v.title;
        card.replaceChild(f, btn);
      });
      card.appendChild(btn);
      var cap = document.createElement("figcaption");
      cap.textContent = v.title;
      fig.appendChild(card);
      fig.appendChild(cap);
      grid.appendChild(fig);
    });
  });

  // Resources filter.
  var chips = document.querySelectorAll(".chip");
  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      var cat = chip.getAttribute("data-cat");
      chips.forEach(function (c) { c.setAttribute("aria-pressed", c === chip ? "true" : "false"); });
      document.querySelectorAll(".res").forEach(function (card) {
        card.hidden = cat !== "all" && card.getAttribute("data-cat") !== cat;
      });
    });
  });

  // Contact form: opens the visitor's email app with the message filled in.
  var form = document.querySelector("form.form");
  if (form) {
    var params = new URLSearchParams(location.search);
    if (params.get("asunto")) form.subject.value = params.get("asunto");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var body = form.message.value + "\n\n" + form.fullname.value + "\n" + form.email.value + (form.phone.value ? "\n" + form.phone.value : "");
      location.href = "mailto:info@newfire.mx?subject=" + encodeURIComponent("[newfire.mx] " + form.subject.selectedOptions[0].text) + "&body=" + encodeURIComponent(body);
    });
  }
})();
