function verificar(){
    var data = new Date()
    var ano = data.getFullYear()
    var fano = window.document.getElementById('txtano')
    var res = window.document.getElementById('res')
    if (fano.value.length ==0||Number(fano.value)>ano){
        window.alert('Verifique eus dados e tente novamente!')
    } else{
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id','foto')
        if (fsex[0].checked){
            genero = 'Homem'
            if (idade >=0 && idade <5){
                img.setAttribute('src','Menino bebe.png')
            } else if (idade < 10){
                img.setAttribute('src','Menino criança.png')
                
            } else if (idade < 21) {
                img.setAttribute('src','Menino Adolescente.png')
                
            } else if (idade < 50) {
                img.setAttribute('src','Menino Adulto.png')
                
            } else {
                img.setAttribute('src','Menino Idoso.png')

            }
        } else if (fsex[1].checked){
            genero = 'Mulher'
            if (idade >=0 && idade <5){
                img.setAttribute('src','Menina bebe.png')
            } else if (idade < 10){
                img.setAttribute('src','Menina criança.png')
                
            } else if (idade < 21) {
                img.setAttribute('src','Menina Adolescente.png')
                
            } else if (idade < 50) {
                img.setAttribute('src','Menina Adulta.png')
                
            } else {
                img.setAttribute('src','Menina Idosa.png')

            }
        }
        res.innerHTML = `Detectamos ${genero} com ${idade} anos`
        res.appendChild(img)
    }
}