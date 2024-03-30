/* var idade = 19
if (idade<16){
    console.log('não vota')
} else{
    if (idade<18 || idade>65){
        console.log('voto opcional')
    } else{
        console.log('Voto obrigatório')
    }
    
} */
var agora = new Date()
var hora = agora.getHours()
console.log(`Agora são exatamente${hora}`)
if (hora<12){
console.log('Bom dia')
} else{
    if (hora<=18){
    console.log('Boa tarde')
    } else{
    console.log('Boa noite')
    }
}