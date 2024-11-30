export function alphanumeric(string: string) {
    //your code here
    // let re = new RegExp("^[a-zA-Z0-9]+$")
    // return `${re.test(string)}, ${string}`
    return RegExp("^[a-zA-Z0-9]+$").test(string)
}


console.log(alphanumeric("Mazinkaiser")) // true
console.log(alphanumeric("hello world_")) // false
console.log(alphanumeric("PassW0rd")) // true
console.log(alphanumeric("     ")) // true