
document.addEventListener("DOMContentLoaded", () => {
    // Hamburger Menu
    const hamburger = document.querySelector(".hamburger");
    const nav = document.querySelector(".nav");

    if (hamburger && nav) {
        hamburger.addEventListener("click", () => {
            nav.classList.toggle("active");
            hamburger.classList.toggle("active");
        });

        // Close nav when a link is clicked (for smooth scroll)
        document.querySelectorAll(".nav-list a").forEach(link => {
            link.addEventListener("click", () => {
                if (nav.classList.contains("active")) {
                    nav.classList.remove("active");
                    hamburger.classList.remove("active");
                }
            });
        });
    }

    // Smooth Scroll to Anchors
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Dynamic Year in Footer
    const currentYearSpan = document.getElementById("currentYear");
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }

    // Scroll Reveal with IntersectionObserver
    const revealElements = document.querySelectorAll(".reveal");

    const observerOptions = {
        root: null,
        rootMargin: "0px",
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("active");
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    revealElements.forEach(el => observer.observe(el));

    // Animated Counters
    const counterObserverOptions = {
        root: null,
        rootMargin: "0px",
        threshold: 0.7
    };

    const animateCounter = (entry) => {
        if (entry.isIntersecting) {
            const counters = entry.target.querySelectorAll(".stat-number, .metric-number");
            counters.forEach(counter => {
                const target = parseInt(counter.getAttribute("data-counter"));
                let current = 0;
                const increment = target / 200; // Adjust speed

                const updateCounter = () => {
                    if (current < target) {
                        current += increment;
                        counter.textContent = Math.ceil(current);
                        requestAnimationFrame(updateCounter);
                    } else {
                        counter.textContent = target;
                    }
                };
                updateCounter();
            });
            counterObserver.unobserve(entry.target);
        }
    };

    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(animateCounter);
    }, counterObserverOptions);

    document.querySelectorAll(".stats, .equipo-metrics").forEach(section => {
        counterObserver.observe(section);
    });

    // Form Validation and Submission
    const contactForm = document.getElementById("contactForm");
    const formMessage = document.getElementById("formMessage");

    if (contactForm) {
        contactForm.addEventListener("submit", function (e) {
            e.preventDefault();

            const name = document.getElementById("name").value;
            const phone = document.getElementById("phone").value;
            const city = document.getElementById("city").value;
            const description = document.getElementById("description").value;

            if (name && phone && city && description) {
                // Simulate form submission
                setTimeout(() => {
                    formMessage.textContent = "¡Gracias! Tu mensaje ha sido enviado. Nos pondremos en contacto contigo pronto.";
                    formMessage.classList.remove("error");
                    formMessage.classList.add("success");
                    formMessage.style.display = "block";
                    contactForm.reset();
                }, 1000);
            } else {
                formMessage.textContent = "Por favor, completa todos los campos requeridos.";
                formMessage.classList.remove("success");
                formMessage.classList.add("error");
                formMessage.style.display = "block";
            }
        });
    }
});