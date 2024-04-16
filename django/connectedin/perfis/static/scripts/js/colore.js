var animaisResgatados = document.querySelectorAll(".resgatados");
var tabela = document.querySelector("#tabela-resgatados");

tabela.addEventListener("click",function(event){
    var alvoEvento = event.target;
    var paiAlvo = alvoEvento.parentNode;
    paiAlvo.classList.add("clicado");
});
