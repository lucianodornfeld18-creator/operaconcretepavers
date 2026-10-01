(function () {
  "use strict";
  var d = document;
  function track(name, params) {
    try { (window.__opEvents = window.__opEvents || []).push([name, params || {}]); if (window.gtag) window.gtag("event", name, params || {}); } catch (e) {}
  }
  var b = d.getElementById("navb"), n = d.getElementById("nav");
  if (b && n) {
    b.addEventListener("click", function () {
      var open = n.classList.toggle("open");
      b.setAttribute("aria-expanded", open ? "true" : "false");
    });
    d.addEventListener("keydown", function (e) { if (e.key === "Escape" && n.classList.contains("open")) { n.classList.remove("open"); b.setAttribute("aria-expanded", "false"); b.focus(); } });
  }
  /* campaign parameters: kept for the session so a lead that converts on page 3 still carries them */
  var KEYS = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid", "fbclid"];
  var store = {};
  try { store = JSON.parse(sessionStorage.getItem("op_utm") || "{}"); } catch (e) {}
  try {
    var q = new URLSearchParams(location.search), got = false;
    KEYS.forEach(function (k) { var v = q.get(k); if (v) { store[k] = v.slice(0, 200); got = true; } });
    if (!store.landing) { store.landing = location.href.split("#")[0].slice(0, 300); got = true; }
    if (!store.ref && d.referrer && d.referrer.indexOf(location.host) < 0) { store.ref = d.referrer.slice(0, 300); got = true; }
    if (got) sessionStorage.setItem("op_utm", JSON.stringify(store));
  } catch (e) {}
  [].forEach.call(d.querySelectorAll('a[href^="tel:"]'), function (a) { a.addEventListener("click", function () { track("tel_click", { page: location.pathname }); }); });
  [].forEach.call(d.querySelectorAll("form.lead"), function (f) {
    KEYS.forEach(function (k) { var e = f.querySelector('[name="' + k + '"]'); if (e && store[k]) e.value = store[k]; });
    var pg = f.querySelector('[name="page"]'); if (pg) pg.value = location.href.split("#")[0].slice(0, 300);
    if (store.ref) { var r = d.createElement("input"); r.type = "hidden"; r.name = "referrer"; r.value = store.ref; f.appendChild(r); }
    var started = false;
    f.addEventListener("focusin", function () { if (!started) { started = true; track("form_start", { page: location.pathname }); } });
    f.addEventListener("submit", function () {
      track("form_submit", { page: location.pathname });
      var btn = f.querySelector('button[type="submit"]'); if (btn) { setTimeout(function () { btn.disabled = true; btn.textContent = "Sending…"; }, 0); }
    });
  });
  /* cost calculator */
  var calc = d.getElementById("calc");
  if (calc) {
    var R = JSON.parse(calc.getAttribute("data-rates"));
    var out = d.getElementById("calc-out");
    var run = function () {
      var L = parseFloat(calc.elements.len.value) || 0, W = parseFloat(calc.elements.wid.value) || 0, A = parseFloat(calc.elements.area.value) || L * W;
      var r = R[calc.elements.kind.value]; if (!A || !r) { out.textContent = "Enter a length and width, or an area."; return; }
      var lo = Math.round(A * r[0] / 50) * 50, hi = Math.round(A * r[1] / 50) * 50;
      var yd = A * (r[2] || 0) / 12 / 27;
      out.innerHTML = "<strong>" + Math.round(A).toLocaleString() + " sq ft:</strong> about $" + lo.toLocaleString() + " to $" + hi.toLocaleString() + " installed (market range, not a quote)." + (yd ? " Concrete volume at " + r[2] + " inches: about " + (yd * 1.08).toFixed(1) + " cubic yards with an 8% overage." : "");
    };
    calc.addEventListener("input", run); calc.addEventListener("submit", function (e) { e.preventDefault(); run(); });
  }
})();
