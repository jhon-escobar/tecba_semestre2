const btncart = document.querySelector('.container-icon')
const containercartproduct = document.querySelector('container-cart-product')

btncart.addEventListener('click', () => {
    containercartproduct.classList.toggle 
    ('hidden-cart')
})