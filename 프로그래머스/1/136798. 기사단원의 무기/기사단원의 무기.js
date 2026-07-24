const calDivisor = (num) => {
    let cnt = 0;
    if(num === 1) return 1;
    for(let i = 1; i <= Number.parseInt(num**(1/2))  ; i++ ){
        if(i * i === num) cnt++;
        else{
            (num % i) ? null : cnt += 2
        }
    }
    return cnt;
}


function solution(number, limit, power) {
    // 1 ~ number 까지 순환
    // 순환하면서 그 숫자의 약수를 구함 
    // 약수의 수가 limit을 넘어간다면 power로 지정 
    // 모든 약수의 개수가 정해졌다면 리스트안의 수들을 더함
    
    let sum = 0;
    for(let i = 1; i <= number; i++){
        let pow = calDivisor(i);
        pow > limit ? sum += power : sum+= pow 
    }
    return sum;
}
