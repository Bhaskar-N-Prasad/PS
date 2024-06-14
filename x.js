// var arr = [1,2,3,4,5]
// var x = arr.filter((x)=>(delete x))
// console.log(x);


var arr = [10,5,0,4,8,0,9,0,2]
var x = arr.filter((x)=>(x!=0)).concat(arr.filter((x)=>(x===0)))
console.log(x);

var arr = [1,2,3,2,4,1,5,3,6]
var x = new Set(arr)
console.log(typeof x);
console.log([...x]);

// books = []
// while(true){
//     console.log("1->add");
//     console.log("2->display");
//     console.log("3->exit");
//     console.log("4->remove");
//     console.log("enter a choice");
//     var x = prompt()
//     if(x==1){
//         console.log("enter book name");
//         var book = prompt()
//         books.push(book)
//     }
//     else if(x==2){
//         console.log(books)
//         }
//         else if(x==3){
//             break;
//         }
//     else if(x == 4){
//         books.pop()
//     }
//     else{
//         console.log("invalid choice")
//     }
// }
