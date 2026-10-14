(function () {
  var grid = document.querySelector("[data-videos]");
  if (!grid) return;
  var limit = parseInt(grid.getAttribute("data-videos"), 10) || 0;
  var ids = window.NEWFIRE.videos;
  if (limit) ids = ids.slice(0, limit);
  ids.forEach(function (id) {
    var card = document.createElement("div");
    card.className = "video";
    var btn = document.createElement("button");
    btn.type = "button";
    btn.setAttribute("aria-label", "Play");
    btn.style.backgroundImage = "url(https://i.ytimg.com/vi/" + id + "/hqdefault.jpg)";
    btn.addEventListener("click", function () {
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0";
      f.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
      f.allowFullscreen = true;
      f.title = "YouTube";
      card.replaceChild(f, btn);
    });
    card.appendChild(btn);
    grid.appendChild(card);
  });
})();
