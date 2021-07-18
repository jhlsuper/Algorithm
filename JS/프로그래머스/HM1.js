function solution(numbers) {
    let answer = 0
    let temp_answer 
    let num={}
    let largest 
    for (index of numbers){
        
        if (num[index] ==undefined){
            num[index] = 1
        }
        else{
            num[index]+=1
        }
    
    }
    
    largest = get_largest(num)
    
    
    if (largest>parseInt(numbers.length)/2){
        temp_answer = largest
    }
    else{
        return -1
    }
    for (let key in num){
        if (num[key]==temp_answer){
            answer =key
        }
    }
    
    return answer
    
}
function get_largest(num){
    let largest=0
    for (let key in num){
        if (num[key]>largest){
            largest =num[key]
        }
    }
    return parseInt(largest)

}

solution([6, 1, 6, 6, 7, 6, 6, 7])


// function solution(numbers) {
//     var answer = 0;
    
//     return answer;
// }