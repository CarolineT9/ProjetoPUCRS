function incrementarJuros(valor, taxa){
    const valorDeAcrescimo = ((taxa / 100)*valor)
    return valor + valorDeAcrescimo
}

console.log(incrementarJuros(100,10))
