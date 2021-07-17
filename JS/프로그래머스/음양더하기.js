function solution(absolutes, signs) {
    let answer =0
    let a =0;
    let b;
    let L = absolutes.length
    
    for (a; a<L;a++){
        // console.log(absolutes[a])
        if (signs[a]===true){
            answer+=absolutes[a]
        
        }
        else{
            answer-=absolutes[a]
        }
        
    }
    // console.log(answer)
    return answer
}

solution([4,7,12],[true,false,true])

