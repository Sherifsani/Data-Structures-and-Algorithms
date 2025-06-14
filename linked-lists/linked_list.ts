class node{
    data: string;
    next: node | null;

    constructor(data: string, next = null) {
        this.data = data
        this.next = next
    }
}

class LinkedList{
    head: node | null
    length: number;

    constructor(){
        this.head = null
        this.length = 0
    }
    append(data:string): void{
        if (!this.head) {
            this.head = new node(data)
            this.length += 1;
            return
        }
        let current = this.head
        while (current.next) {
            current = current.next
        }
        current.next = new node(data)
        this.length += 1
    }
    print(): void{
        let current = this.head
        while (current) {
            console.log("data: ", current.data)
            current = current.next
        }
    }
    find(item:string): boolean {
        let current = this.head
        while (current) {
            if (current.data == item) {
                return true
            } else {
                current = current.next
            }
        }
        return false
    }
    remove(target: string) {
        if (!this.head) return;

        if (this.head?.data == target) {
            this.head = this.head.next
            this.length -= 1
            return
        }
        let current: node | null = this.head
        while (current) {
            if (current.next?.data == target) {
                current.next = current.next.next
                this.length -= 1
                return
            }
            current = current.next
        }
    }
    reverse(): void{
        let current = this.head
        let previous: node | null = null

        while (current) {
            let next = current.next
            current.next = previous
            previous = current
            current = next
        }

        this.head = previous
    }
    // detect_cycle(): boolean{
    //     let slow = this.head
    //     let fast = this.head

    //     while(fast && fast.next) {
    //         slow = slow?.next
    //         fast = fast.next.next

    //         if (slow === fast) {
    //             return true // 
    //         }
    //     }
    //     return false 
    // }
}


