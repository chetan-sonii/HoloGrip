document.addEventListener("DOMContentLoaded", () => {
    const nav = document.getElementById("mainNav");

    document.querySelectorAll(".navbar .nav-link").forEach((link) => {
        link.addEventListener("click", () => {
            if (nav && nav.classList.contains("show")) {
                bootstrap.Collapse.getOrCreateInstance(nav).hide();
            }
        });
    });

    const revealElements = document.querySelectorAll(".reveal");

    if (!("IntersectionObserver" in window)) {
        revealElements.forEach((element) => element.classList.add("visible"));
        return;
    }

    const observer = new IntersectionObserver((entries, currentObserver) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                currentObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12 });

    revealElements.forEach((element) => observer.observe(element));
});
