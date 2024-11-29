fn make_upper_case(s: &str) -> String {
    // code here
    s.to_string().to_uppercase()
}

fn main() {
    let s = make_upper_case("jakepys");   
    println!("{}", s);
}
