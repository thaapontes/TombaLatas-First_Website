var botao = document.querySelector("#botao");

botao.addEventListener("click",function(event){
    event.preventDefault();

    var form = document.querySelector("#form-adiciona");

    var animalResgatado = obtemDoForm(form);

    var erros = validaAnimal(animalResgatado,form);

    if(erros.length > 0){
        exibeMensagem(erros);
        return;
    }
    adicionarAnimalResgatado(animalResgatado);
    form.reset();
    
});
function adicionarAnimalResgatado(animalResgatado){
    var animalTr = montaTr(animalResgatado);
    var tabela = document.querySelector("#tabela-resgatados");
    tabela.insertBefore(animalTr, tabela.firstChild);
}

function obtemDoForm(form){
    var type = form.querySelector("#tipo");
    var animalResgatado = {
        nome: form.nomeanimal.value,
        local: form.endereco.value,
        caracteristicas: form.caracteristicas.value,
        animal: type[type.selectedIndex].value
    }
    return animalResgatado;
}

function montaTr(animalResgatado){
    var resgatadoTr = document.createElement("tr");
    resgatadoTr.classList.add("resgatados");

    var nomeTd = montaTd(animalResgatado.nome,"info-nome");
    var animalTd = montaTd(animalResgatado.animal,"info-tipo");
    var localTd = montaTd(animalResgatado.local,"info-local");
    var caracteristicasTd = montaTd(animalResgatado.caracteristicas,"info-caracteristicas");

    resgatadoTr.appendChild(nomeTd);
    resgatadoTr.appendChild(animalTd);
    resgatadoTr.appendChild(localTd);
    resgatadoTr.appendChild(caracteristicasTd);

    return resgatadoTr;
}

function montaTd(dado, classe){
    var td = document.createElement("td"); 
     td.textContent = dado;
     td.classList.add(classe);
     return td;
}

function validaAnimal(animalResgatado, form){
    var erros = [];
    if(!validaNome(animalResgatado.nome)){
        erros.push("Nome inválido");
        form.nomeanimal.classList.add("erro");
    }
    if(validaNome(animalResgatado.nome) == "Desconhecido"){
        animalResgatado.nome = "Desconhecido";
    }
    if(!validaLocal(animalResgatado.local)){
        erros.push("Local inválido");
        form.endereco.classList.add("erro");
    }
    if(!validaTipo(animalResgatado.animal)){
        erros.push("Escolha um animal");
    }
    if(!validaCaracteristicas(animalResgatado.caracteristicas)){
        erros.push("Características inválidas");
        form.caracteristicas.classList.add("erro");
    }
    return erros;
}

function exibeMensagem(erros){
    var ul = document.querySelector("#mensagens-erro");
    erros.forEach(function(erro){
        var li = document.createElement("li");
        li.textContent = erro;
        ul.appendChild(li);
    });
}