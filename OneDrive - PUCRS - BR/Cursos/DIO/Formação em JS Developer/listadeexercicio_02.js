/*
IMC = peso / (altura * altura)

Elabore um algoritmo que dado o peso e a altura de um adulto mostre sua condição de acordo com a tabela abaixo. 


IMC em adultos Condições:

- abaixo de 18.5 = abaixo do peso;
- entre 18.5 e 25 peso normal;
- entre 25 e 30 acima do peso;
- entre 30 e 40 obeso;
- acima de 40 obesidade grave;

*/

const peso = 62;
const altura = 1.62;

const imc = peso/(altura*altura)
console.log(imc.toFixed(2))

if (imc<18.5){
    console.log('Abaixo do peso.')
}else if(imc>=18.5 & imc<25) {
    console.log('Peso normal.')
}else if (imc>=25 & imc<30){
    console.log('Acima do peso.')
}else if(imc>=30 & imc<=40){
    console.log('Obeso!')
}else{
    console.log("Obesidade grave!!")
}
