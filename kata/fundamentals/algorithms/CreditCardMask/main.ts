/**
 * 
 * 
 * 
 * 
 * 
 * sually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

    Your task is to write a function maskify, which changes all but the last four characters into '#'.
    Examples (input --> output):

    "4556364607935616" --> "############5616"
         "64607935616" -->      "#######5616"
                   "1" -->                "1"
                    "" -->                 ""

    // "What was the name of your first pet?"
    "Skippy" --> "##ippy"
    "Nananananananananananananananana Batman!" --> "####################################man!"
    
 */

// 4
function maskify(cc: string) {
    //return `${cc.split("").map((c) => c = "#").slice(0, cc.length - 4).join("")}${cc.slice(-4)}`
    return `${cc.split("").map((c, index) => index < cc.length - 4 ? "#" : c).join("")}`;
}

console.log("this:", "4556364607935616".length)
console.log(maskify("4556364607935616") === "############5616") // true
