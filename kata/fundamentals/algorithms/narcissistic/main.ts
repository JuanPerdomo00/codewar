export function narcissistic(value: number) {
    // your code here
    let cap = value.toString().split("")
    let sum = 0
    value.toString().split("").map((a) => parseInt(a)).map((a) => a ** cap.length).forEach((a) => {
        sum += a
        return sum
    })

    return true ? sum === value : false
}



console.log(narcissistic(7))
console.log(narcissistic(153))
console.log(narcissistic(1634))
console.log(narcissistic(1652))

