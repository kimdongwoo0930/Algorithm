function solution(n) {
    let i = 1;
    while(1){
        if(calulate(n,i) == 1){
            return i;
        }
        i++;
    }
}

const calulate = (n,i) => {
    return n % i;
}