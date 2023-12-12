function abrirFuncao(){
    var funcao = document.getElementsByClassName('funcaoAberta')[0]
    funcao.style.display = "grid"
}

function fecharFuncao(){
    var funcao = document.getElementsByClassName('funcaoAberta')[0]
    funcao.style.display = "none"
}

function abrirHelp(){
    var help = document.getElementById('helpAberto')
    help.style.display = "grid"
}

function fecharHelp(){
    var help = document.getElementById('helpAberto')
    help.style.display = "none"
}

function abrirControlador(){
    var controlador = document.getElementsByClassName('controladorAberto')[0]
    controlador.style.display = "grid"
}

function fecharControlador(){
    var controlador = document.getElementsByClassName('controladorAberto')[0]
    controlador.style.display = "none"
}

function fecharInicial(){
    var inicial = document.getElementsByClassName('avisoInicial')[0]
    inicial.style.display = "none"
}

function makeDraggable(elementId) {
    let isDragging = false;
    let initialX;
    let initialY;

    const dragElement = document.getElementById(elementId);

    dragElement.addEventListener('mousedown', function (e) {
        isDragging = true
        initialX = e.clientX - dragElement.getBoundingClientRect().left
        initialY = e.clientY - dragElement.getBoundingClientRect().top
        dragElement.style.cursor = 'grabbing'
    });

    document.addEventListener('mousemove', function (e) {
        if (!isDragging) return

        const newX = e.clientX - initialX
        const newY = e.clientY - initialY

        if (elementId == "tituloControlador"){
            document.getElementById('controladorAberto').style.left = `${newX}px`
            document.getElementById('controladorAberto').style.top = `${newY}px`
        }
        else if(elementId == "tituloFuncao"){
            document.getElementById('funcaoAberta').style.left = `${newX}px`
            document.getElementById('funcaoAberta').style.top = `${newY}px`
        }
        else{
            document.getElementById('helpAberto').style.left = `${newX}px`
            document.getElementById('helpAberto').style.top = `${newY}px`
        }
    })

    document.addEventListener('mouseup', function () {
        isDragging = false;
        dragElement.style.cursor = 'grab'
    });
}

document.addEventListener('DOMContentLoaded', function () {
    makeDraggable('tituloControlador')
    makeDraggable('tituloFuncao')
    makeDraggable('tituloHelp')

    const helpMenuItems = document.querySelectorAll('.help-menu-item')

    helpMenuItems.forEach(item => {
        item.addEventListener('click', () => showContent(item.dataset.contentId))
    })

})

function showContent(contentId) {
    const contents = document.querySelectorAll('.content')
    const backBtns = document.querySelectorAll('.back-btn')

    document.getElementsByClassName('help-menu')[0].style.display = 'none'

    contents.forEach(content => {
        content.style.display = 'none'
    })

    document.getElementById(contentId).style.display = 'block'

    backBtns.forEach(btn => {
        btn.style.display = 'none'
    })

    document.querySelector(`#${contentId} .back-btn`).style.display = 'block'
}

function showMenu() {
    const contents = document.querySelectorAll('.content')
    const backBtns = document.querySelectorAll('.back-btn')
    const helpMenuItems = document.querySelectorAll('.help-menu-item')

    document.getElementsByClassName('help-menu')[0].style.display = 'block'

    contents.forEach(content => {
        content.style.display = 'none'
    })

    helpMenuItems.forEach(item => {
        item.style.display = 'block'
    })

    backBtns.forEach(btn => {
        btn.style.display = 'none'
    })
}