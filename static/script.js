const movieCardTemplate = document.querySelector("[data-movie-template]")
const movieCardContainer = document.querySelector("[data-movie-cards-container]")
const searchInput = document.querySelector("[data-search]")

function openModal(movie){
    var modal = document.querySelector("[playlist-display]");
    var span = document.querySelector(".close");

    modal.style.display = "block";

    span.onclick = function() {
        modal.style.display = "none";
    }
}

searchInput.addEventListener("input", e => {
    const query = e.target.value
    
    if (!query){
        movieCardContainer.innerHTML = "";
    }

    fetch(`http://127.0.0.1:8002/search-api?q=${encodeURIComponent(query)}`)
    .then(res => res.json())
    .then(data => {
        data.forEach(movie => {
            console.log(movie)
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

