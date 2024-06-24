// var arr = [1,2,5,3,7,5,8,5]
// var x = {}
// for(var i = 0;i<arr.length;i++){
//     if(x[arr[i]]){
//         x[arr[i]] = x[arr[i]] + 1
//         }else{
//             x[arr[i]] = 1
//         }
// }
// var k = 5
// console.log(x[k]);


obj= {
    name: "Bhaskar",
    2:2,
    3:1,
    5:[1,2,3,4,5],
    fname:(name)=>{
        console.log(`My name is ${this.name}`);
    }
}
obj.fname("Bhaskarrrrrr")
// console.log(obj);

