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