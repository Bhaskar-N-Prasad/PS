const promiseFour = new Promise((resolve, reject) => {
    setTimeout(function(){
        let error = false;
        if (!error) {
            resolve({username: "Bhaskar", password:"1234"})
        }else{
            reject('ERROR: Something Went Wrong')
        }
    }, 1000)
})

promiseFour.then((user)=>{
    console.log(user);
    return user.username
}).then((username)=>{
    console.log(username);
}).catch(function(error){
    console.log(error);
}).finally(()=>{
    console.log("The Promise is either resolved or rejected");
})