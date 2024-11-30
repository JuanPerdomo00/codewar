# a = 011 -> 3
# b = 010 -> 2

## Xor
## 011
## 010
#--------
## 001


function add(a, b)
    while b != 0
        com = a & b
        a = a ⊻ b
        b = com << 1
    end
    return a
end

add(2, 5)