/*
    Faça um algoritmo que dado 3 notas tiradas por um aluno em um semestre de faculdade calcule e imprima a sua media

    media = (nota 1 + nota 2 + nota 3)/3

    classificiação:

    media < 5 = reprovado
    media 5 e 7, recuperaçao
    media acima de, passou de semestre

*/

const nota1 = 5
const nota2 = 7
const nota3 = 8

const media = (nota1 + nota2 + nota3)/3
console.log(media.toFixed(2))


if (media<5){
    console.log('Reprovado')
}
else if (media>=5 & media <= 7){
    console.log('Recuperação')
}else{
    console.log('Passou de semestre')
}