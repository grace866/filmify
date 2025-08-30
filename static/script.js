const movieCardTemplate = document.querySelector("[data-movie-template]")
const movieCardContainer = document.querySelector("[data-movie-cards-container]")
const searchInput = document.querySelector("[data-search]")

function openModal(movie){
    const modal = document.querySelector("[playlist-display]");
    const span = document.querySelector(".close");
    const ul = document.querySelector(".playlist");
    const movie_id = encodeURIComponent(movie.id);

    modal.style.display = "block";
    fetch(`http://127.0.0.1:8002/make-playlist?movie_id=${movie_id}`)
    .then(res => res.json())
    .then(data => {
        ul.innerHTML = '';
        data.forEach(track => {
            console.log(track)
            const li = document.createElement("li");
            li.textContent = `${track.name}`;
            ul.appendChild(li)
        })
    })

    span.onclick = function() {
        modal.style.display = "none";
    }
}

searchInput.addEventListener("input", e => {
    movieCardContainer.innerHTML = "";
    const query = e.target.value
    
    if (!query){
        movieCardContainer.innerHTML = "";
    }

    fetch(`http://127.0.0.1:8002/search-api?q=${encodeURIComponent(query)}`)
    .then(res => res.json())
    .then(data => {
        data.forEach(movie => {
            const card = movieCardTemplate.content.cloneNode(true).children[0]
            const header = card.querySelector("[data-header]")
            const body = card.querySelector("[data-body]")
            header.textContent = movie.title
            body.textContent = movie.release_date
            movieCardContainer.append(card)

            card.addEventListener("click", () => {
                openModal(movie);
            })
        })
    })
})

