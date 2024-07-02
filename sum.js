// a = [10,20,30]
// sum = 0
// for (i of a) {
//     sum += i
// }
// console.log(sum)
// avg = sum/a.length
// console.log(avg)



// var a = "madam"
// var b = ""
// for (i = a.length - 1; i >= 0; i--) {
//     b += a[i]
// }
// if (a == b) {
//     console.log("pallindrom");
// }else{
//     console.log("not a pallindrom");
// }


var a = "silent"
var b = "listen"
console.log(a.split(""));
if (a.length == b.length) {
    if (a.split("").sort().join("") == b.split("").sort().join("")) {
        console.log("anagram");
    }else{
        console.log("not anagram");
    }
}

