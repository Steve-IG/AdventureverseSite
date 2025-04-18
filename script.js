document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('nav');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            nav.classList.toggle('active');
            menuToggle.classList.toggle('active');
        });
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    const video = document.getElementById('hero-video');
    
    // Set playback rate when video metadata is loaded
    video.addEventListener('loadedmetadata', function() {
        video.playbackRate = 0.75;
    });
    
    // Also set it immediately in case the event has already fired
    video.playbackRate = 0.75;

    // Intersection Observer for fade-in animations
    const observerOptions = {
        root: null, // use viewport as root
        rootMargin: '0px',
        threshold: 0.4 // trigger when 20% of the element is visible
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                // Once the animation is triggered, we can stop observing this element
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all feature sections
    document.querySelectorAll('.feature-section').forEach(section => {
        observer.observe(section);
    });

    // Add immediate fade-in for hero logo since it's likely already visible
    const heroLogo = document.querySelector('.hero-logo');
    if (heroLogo) {
        // Small delay to ensure the transition is visible
        setTimeout(() => {
            heroLogo.classList.add('fade-in');
        }, 100);
    }
}); 