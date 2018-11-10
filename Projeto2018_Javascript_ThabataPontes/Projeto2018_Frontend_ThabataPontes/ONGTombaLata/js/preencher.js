
window.onload = initPage;
function initPage(){
    var xhr = new XMLHttpRequest();
    
    xhr.open("GET", "https://cors.io/?http://www.mocky.io/v2/5ad3f0132e000029005838fb");
    xhr.addEventListener("load", function(){
        var resposta = xhr.responseText;
        var animais = JSON.parse(resposta);
        animais.forEach(function(resgatado){
            adicionarAnimalResgatado(resgatado);
        });
    });
    xhr.send();
}