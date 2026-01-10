// document.addEventListener("DOMContentLoaded",function(){
//     const btn=document.getElementById("toggle-theme");
//     const html=document.documentElement;
//     btn.addEventListener('click',function(){
//         const current=html.getAttribute("data-bs-theme");
//         const next=current ==="dark" ? "light":"dark";
//         html.setAttribute("data-bs-theme", next);
        
//     })
// })


document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("toggle-theme");
    const html = document.documentElement;

    // 👉 1. Cargar tema guardado
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme) {
        html.setAttribute("data-bs-theme", savedTheme);
    }

    // 👉 2. Alternar y guardar tema
    btn.addEventListener("click", function () {
        const current = html.getAttribute("data-bs-theme");
        const next = current === "dark" ? "light" : "dark";

        html.setAttribute("data-bs-theme", next);
        localStorage.setItem("theme", next);
    });
});
// mostrar/ocultar contraseña
function togglePassword(fieldId){
    const field=document.getElementById(fieldId);
    const icon = document.getElementById('icon-'+ fieldId);
    if(field.type==="password"){
        field.type="text";
        icon.classList.remove('fa-eye');
        icon.classList.add('fa-eye-slash');

    }else{
        field.type="password";
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
    }
}
// MENSAJES FLOTANTES
document.addEventListener("DOMContentLoaded", function(){
    const toastElList =[].slice.call(document.querySelectorAll('.toast'));
    toastElList.forEach(function(toastEl){
        const toast= new bootstrap.Toast(toastEl,{
            delay:3000
        });
        toast.show();
    })
})
// Funcion de Fecht

//  document.addEventListener("DOMContentLoaded", function () {

//     const container = document.getElementById("juegos-container");

//     if (!container) {
//         console.warn("No existe #juegos-container en esta página");
//         return;
//     }

//     fetch("/api/juegos/")
//         .then(response => response.json())
//         .then(data => {

//             container.innerHTML = "";

//             data.results.forEach(juego => {

//                 const imagen = juego.imagen || DEFAULT_IMAGE;

//                 container.innerHTML += `
//                     <div class="col-12 col-md-4 mb-4">
//                         <div class="card h-100 shadow-sm">
//                             <img src="${imagen}" class="card-img-top" alt="${juego.nombre}">
//                             <div class="card-body">
//                                 <h5>${juego.nombre}</h5>
//                                 <p>${juego.plataforma}</p>
//                                 <strong>$${juego.precio}</strong>
//                             </div>
//                         </div>
//                     </div>
//                 `;
//             });
//         })
//         .catch(err => console.error("Error fetch:", err));
// });


let currentPage = 1;

document.addEventListener("DOMContentLoaded", function () {

    const container = document.getElementById("juegos-container");
    const btnPrev = document.getElementById("btn-prev");
    const btnNext = document.getElementById("btn-next");

    if (!container) return;

    function cargarJuegos(page = 1) {
        fetch(`/api/juegos/?page=${page}`, { cache: "no-store" })
            .then(res => res.json())
            .then(data => {

                container.innerHTML = "";

                data.results.forEach(juego => {
                    const imagen = juego.imagen || DEFAULT_IMAGE;

                    container.innerHTML += `
                        <div class="col-12 col-md-4 mb-4">
                            <div class="card h-100 shadow-sm">
                                <img src="${imagen}" class="card-img-top">
                                <div class="card-body">
                                    <h5>${juego.nombre}</h5>
                                    <p>${juego.plataforma}</p>
                                    <strong>$${juego.precio}</strong>
                                </div>
                            </div>
                        </div>
                    `;
                });

                // estado botones
                btnPrev.disabled = !data.previous;
                btnNext.disabled = !data.next;

                currentPage = page;
            })
            .catch(err => console.error("Error fetch:", err));
    }

    btnPrev.addEventListener("click", () => {
        if (currentPage > 1) {
            cargarJuegos(currentPage - 1);
        }
    });

    btnNext.addEventListener("click", () => {
        cargarJuegos(currentPage + 1);
    });

    cargarJuegos();
});
