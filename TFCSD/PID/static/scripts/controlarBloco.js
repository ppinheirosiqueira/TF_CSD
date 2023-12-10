var abrindoFuncao = false
var abrindoControlador = false

function abrirFuncao(){
    var funcao = document.getElementsByClassName('funcaoAberta')[0]
    funcao.style.display = "grid"
    window.abrindoFuncao = true
    setTimeout(function() {
        window.abrindoFuncao = false
    }, 200)
}

function abrirControlador(){
    var controlador = document.getElementsByClassName('controladorAberto')[0]
    controlador.style.display = "grid"
    abrindoControlador = true
    setTimeout(function() {
        abrindoControlador = false
    }, 200)
}

document.addEventListener('click', function(event) {
    var funcao = document.getElementsByClassName('funcaoAberta')[0]
    if (!abrindoFuncao && event.target !== funcao && !funcao.contains(event.target) && funcao.style.display == "grid") {
        funcao.style.display = 'none'
    }
})

document.addEventListener('click', function(event) {
    var controlador = document.getElementsByClassName('controladorAberto')[0]
    if (!abrindoControlador && event.target !== controlador && !controlador.contains(event.target) && controlador.style.display == "grid") {
        controlador.style.display = 'none'
    }
})