function validaNome(nome){
    if( nome.length > 30){
        return false;
    }else if( nome.length == 0){
        var nomeAnimal = "Desconhecido";
        return nomeAnimal;
    }else{
        return true;
    }
}
function validaLocal(local){
    if( local.length < 5 || local.length > 50){
        return false;
    }else{
        return true;
    }
 }

 function validaCaracteristicas(caracteristicas){
    if( caracteristicas.length < 10 || caracteristicas.length > 200){
        return false;
    }else{
        return true;
    }
 }

 function validaTipo(tipo){
    if( tipo == "escolher"){
        return false;
    }else{
        return true;
    }
 }