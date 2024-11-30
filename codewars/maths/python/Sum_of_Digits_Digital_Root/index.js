class Tree {
    constructor(valor) {
        this.value = valor;
        this.left = null;
        this.right = null;
    }

    add(value) {
        if (value < this.value) {
            this.addLeft(value);
        } else {
            this.addRight(value);
        }
    }

    addLeft(value) {
        if (this.left) {
            this.left.add(value);
        } else {
            this.left = new Tree(value);
        }
    }

    addRight(value) {
        if (this.right) {
            this.right.add(value);
        } else {
            this.right = new Tree(value);
        }
    }
}

const tree = new Tree(999);

let con = 30;

while (con > 1) {
    tree.add(con);
    con--;
}

console.log(tree);
