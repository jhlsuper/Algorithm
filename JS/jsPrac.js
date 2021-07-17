function practice(){
    let a = 10;
    if (a ===10){
        console.log("is 10")
    }
    else{
        console.log("else")
    }
    let b = 0;
    for (b; b<10;b++){
        // console.log(b);
        // document.write(b)
    }
    let temp=[]
    temp.push(1,2,3)
    console.log(temp)
    for (index in temp){
        console.log(index)
    }
    for (var i of temp){
        console.log(i)
    }
    temp.map((value, index)=>{
        console.log(value,index)
    })
}


practice()