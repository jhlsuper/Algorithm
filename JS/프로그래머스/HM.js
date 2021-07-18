function solution(s) {
    let answer = 0;
    let divisor =[]
    let middle
    for (let i=1 ;i<s+1;i++){
        if (s%i===0){
            divisor.push(i)
        }
    }
    // console.log(divisor)
    
    middle = parseInt((divisor.length)/2)
    if ((divisor.length)%2 != 0){
        answer = (divisor[middle]*4)
    }
    else{
    // console.log(divisor[middle],divisor[middle-1])
    answer = (divisor[middle]+divisor[middle-1])*2
    }
    
    return answer
}

solution(9)