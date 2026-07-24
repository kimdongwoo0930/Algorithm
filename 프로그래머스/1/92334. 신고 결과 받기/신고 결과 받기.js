function solution(id_list, report, k) {
    let per = {}
    let obj = {}
    id_list.map((item) => {
        obj[item] = []
        per[item] = 0
    });
    
    report.map((item) => {
        const rep = item.split(" ");
        (obj[rep[1]].includes(rep[0])) ? null : obj[rep[1]].push(rep[0])
    })
    
    Object.entries(obj).forEach(([key,value]) => {
        (value.length >= k) ? 
            value.map((item) => per[item] += 1) : null    
    })
    return (Object.values(per))
    
}