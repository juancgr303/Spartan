/*===== SCROLL REVEAL ANIMATION =====*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '40px',
    duration: 1000,
    reset: false,
})

/*====Blog and Articles====*/
sr.reveal('.title', {})
sr.reveal('.featured-item', {origin:'right', delay: 200})

/*====Article====*/
sr.reveal('.featured_img', {})
sr.reveal('.article-info', {delay: 200})
sr.reveal('h1', {delay: 250})
sr.reveal('h4', {delay: 300})
sr.reveal('p', {delay: 350})

