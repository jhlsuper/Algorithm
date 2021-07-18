function solution(r, c) {
    let answer = 0;
    let min= Math.min(r,c)-1
    let n = r+c-2
    // console.log("min",min)
    answer =combination(n,min)
  
   
    return answer
}

function combination(n,c){
    let i =0
    let j =1
    let temp =n
    let up =1

    let down =1
    // console.log(n,c)
    for (i;i<c;i++){
        up*=temp
        temp-=1
        
    }
    for (j;j<c+1;j++){
        down*=j
    }
    return parseInt(up/down)
}
solution(2,4)
solution(3,3)