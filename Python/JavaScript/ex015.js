/* let num=[5,8,9,3]
num.push(99)
num.sort()
console.log(`o tamanho do nosso vetor é de ${num.length} elementos`)
console.log(`nosso valores são ${num}`)
 */
let num = [5,8,9,3,2,2,2,1,21,3,2]
var rep=0
/* for(var rep=0;rep<num.length;rep++){
    console.log(`a posição ${rep}, tem o valor ${num[rep]}`)
} */
for(let rep in num){
    console.log(`a posição ${rep}, tem o valor ${num[rep]}`)
}