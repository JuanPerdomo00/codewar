function comp(a: number[] | null, b: number[] | null): boolean {
    // your code
    if (Array.isArray(a) && Array.isArray(b)) {
        return b.sort((a, b) => a - b).every((x, i) => x === Math.pow(a.sort((a, b) => a - b)[i], 2))
    } else if (!a || !b) {
        return false
    }

    return false
}

//                      14641
let a: Array<number> = [121, 144, 19, 161, 19, 144, 19, 11] // a1
let b: Array<number> = [121, 14641, 20736, 361, 25921, 361, 20736, 361] // a2

console.log(comp(a, b))