/* Minimal interactivity for the GALDC static site.
 * Handles the mobile menu toggle and click-to-open dropdowns on
 * touch / no-hover devices. No fetches, no framework.
 */
(function () {
  "use strict";

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    var toggle = document.querySelector("[data-mobile-toggle]");
    var menu = document.querySelector("[data-mobile-menu]");

    if (toggle && menu) {
      toggle.addEventListener("click", function (e) {
        e.stopPropagation();
        var open = menu.classList.toggle("is-open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
      });

      document.addEventListener("click", function (e) {
        if (!menu.contains(e.target) && !toggle.contains(e.target)) {
          menu.classList.remove("is-open");
          toggle.setAttribute("aria-expanded", "false");
        }
      });
    }

    var canHover = window.matchMedia("(hover: hover)").matches;

    var dropdowns = document.querySelectorAll(".dropdown");
    Array.prototype.forEach.call(dropdowns, function (dd) {
      var trigger = dd.querySelector(".dropdown-trigger");
      if (!trigger) return;
      trigger.addEventListener("click", function (e) {
        if (canHover && window.innerWidth >= 1024) return;
        e.preventDefault();
        e.stopPropagation();
        var isOpen = dd.classList.toggle("is-open");
        trigger.setAttribute("aria-expanded", isOpen ? "true" : "false");
        Array.prototype.forEach.call(dropdowns, function (other) {
          if (other !== dd) {
            other.classList.remove("is-open");
            var t = other.querySelector(".dropdown-trigger");
            if (t) t.setAttribute("aria-expanded", "false");
          }
        });
      });
    });

    document.addEventListener("click", function (e) {
      Array.prototype.forEach.call(dropdowns, function (dd) {
        if (!dd.contains(e.target)) {
          dd.classList.remove("is-open");
          var t = dd.querySelector(".dropdown-trigger");
          if (t) t.setAttribute("aria-expanded", "false");
        }
      });
    });

    document.addEventListener("keydown", function (e) {
      if (e.key !== "Escape") return;
      if (menu) menu.classList.remove("is-open");
      if (toggle) toggle.setAttribute("aria-expanded", "false");
      Array.prototype.forEach.call(dropdowns, function (dd) {
        dd.classList.remove("is-open");
        var t = dd.querySelector(".dropdown-trigger");
        if (t) t.setAttribute("aria-expanded", "false");
      });
    });
  });
})();
