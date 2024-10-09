function countBits(n: number) {
	return n.toString(2).split("").filter((bit) => bit ? bit === "1": "").length
}
console.log(countBits(0)) // 0
console.log(countBits(4)) // 1
console.log(countBits(7)) // 2 
console.log(countBits(9)) //  2
console.log(countBits(10)) // 2
