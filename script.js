const lastLogin = document.getElementById('last-login');
if (lastLogin) {
    const formatter = new Intl.DateTimeFormat('vi-VN', {
        dateStyle: 'medium',
        timeStyle: 'medium'
    });
    lastLogin.textContent = formatter.format(new Date());
}

const navLinks = document.querySelectorAll('.nav-link');
const sections = [...document.querySelectorAll('.section')];

const activateLink = (id) => {
    navLinks.forEach((link) => {
        link.classList.toggle('is-active', link.getAttribute('href') === `#${id}`);
    });
};

const observer = new IntersectionObserver(
    (entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                activateLink(entry.target.id);
            }
        });
    },
    {
        rootMargin: '-40% 0px -40% 0px',
        threshold: 0.4
    }
);

sections.forEach((section) => observer.observe(section));

navLinks.forEach((link) => {
    link.addEventListener('click', (event) => {
        event.preventDefault();
        const targetId = link.getAttribute('href').slice(1);
        const target = document.getElementById(targetId);
        if (!target) return;
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        activateLink(targetId);
        history.replaceState(null, '', `#${targetId}`);
    });
});
