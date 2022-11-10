const modal1 = document.querySelector("#modal1");
const openModal1 = document.querySelector(".openModal1");
const closeModal = document.querySelector("#closeModal1");

openModal1.addEventListener('click', () => {
    modal1.showModal();
} )

closeModal1.addEventListener('click', () => {
    modal1.close();
})
