function carregar(){
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    /* var hora = data.getHours() */
    var hora = 13
    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora >= 0 && hora < 12) {
        img.src = 'Amanhecer.png';
        document.body.style.background = '#939da7'
    } else if (hora >= 12 && hora < 18) {
        img.src = 'Tarde.png';
        document.body.style.background = '#f5b55b'
    } else {
        img.src = 'Anoitecer.png';
        document.body.style.background = '#ff676d'
    }
}