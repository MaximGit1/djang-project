document.addEventListener('DOMContentLoaded', function () {
    let authorInfoElements = document.querySelectorAll('.author_info');
    let biography = [];
    let authors = [];

    authorInfoElements.forEach(function (element) {
        let biographyUrl = element.getAttribute('data-biography');
        biography.push(biographyUrl.substring(0, 200));
        let authorUrl = element.getAttribute('data-page-url')
        authors.push(authorUrl)
    });

    authorInfoElements.forEach(function (element, index) {
        let description = document.createElement('p');
        description.innerHTML = biography[index] + ` <a href="${authors[index]}">Читать далее...</a>`;
        element.appendChild(description);
    });

});
