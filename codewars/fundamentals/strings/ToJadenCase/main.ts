function ToJadenCase(s:string)  {
    return s.split(" ").map((word) => word.slice(0, 1).toUpperCase() + word.slice(1)).join(" ")
}


function main() {
    console.log(ToJadenCase("All the rules in this world were made by someone no smarter than you. So make your own."))
}

main()