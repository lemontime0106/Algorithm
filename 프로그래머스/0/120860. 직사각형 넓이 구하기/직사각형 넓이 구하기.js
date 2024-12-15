function solution(dots) {
    
    const X = dots.map(dot => dot[0])
    const Y = dots.map(dot => dot[1])
    
    const x = Math.max(...X) - Math.min(...X)
    const y = Math.max(...Y) - Math.min(...Y)
    
    return x * y
}