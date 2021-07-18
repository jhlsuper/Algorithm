function solution(k) {
    let answer = 0;
    let sequence =[]
    let index =1
    let i =1
    while (sequence.length<k){
        for (i=1; i<index+1;i++){
            sequence.push(i)
        }
        index+=1
    }
    // console.log(sequence[k-1])
    answer = sequence[k-1]
    return answer;
}

solution(4)
solution(10)