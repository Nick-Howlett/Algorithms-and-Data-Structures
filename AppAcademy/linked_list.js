// ============================================================================
// Implementation Exercise: Singly Linked List
// ============================================================================
//
// -------
// Prompt:
// -------
//
// Implement a Singly Linked List and all of its methods below!
//
// ------------
// Constraints:
// ------------
//
// Make sure the time and space complexity of each is equivalent to those 
// in the table provided in the Time and Space Complexity Analysis section
// of your Linked List reading!
//
// -----------
// Let's Code!
// -----------

// TODO: Implement a Linked List Node class here
class Node {
    constructor(val) {
        this.value = val;
        this.next = null;
    }

}

// TODO: Implement a Singly Linked List class here
class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    // TODO: Implement the addToTail method here
    addToTail(val) {
        const node = new Node(val);
        if(this.length == 0){
            this.head = node;
            this.tail = node;
        } else {
            this.tail.next = node;
            this.tail = node;
        }
        this.length++;
        return this;
    }

    // TODO: Implement the removeTail method here
    removeTail() {
        let ret;
        if(this.length == 0) return;
        if(this.length === 1){
            this.head = null;
            this.tail = null;
        } else {
            let curr = this.head;
            while(curr.next != this.tail){
                curr = curr.next;
            }
            ret = curr.next;
            curr.next = null;
            this.tail = curr;
        }
        this.length--;
        return ret;
    }

    // TODO: Implement the addToHead method here
    addToHead(val) {
        const node = new Node(val);
        if(this.length === 0){
            this.head = node;
            this.tail = node;
        } else {
            node.next = this.head;
            this.head = node;
        }
        this.length++;
        return this;
    }

    // TODO: Implement the removeHead method here
    removeHead() {
        let ret;
        if(this.length == 0) return;
        if(this.length === 1){
            this.head = null;
            this.tail = null;
        } else {
            ret = this.head;
            this.head = this.head.next;
        }
        this.length--;
        return ret;
    }

    // TODO: Implement the contains method here
    contains(target) {
        for(let curr = this.head; curr != null; curr = curr.next){
            if(curr.value === target) return true;
        }
        return false;
    }

    // TODO: Implement the get method here
    get(index) {
        let i = 0;
        let curr = this.head;
        while(i < index){
            if(!curr) return null;
            curr = curr.next;
            i++;
        }
        return curr;
    }

    // TODO: Implement the set method here
    set(index, val) {
        let i = 0;
        let curr = this.head;
        while(i < index){
            curr = curr.next;
            if(!curr) return false;
            i++;
        }
        curr.value = val;
        return true;
    }

    // TODO: Implement the insert method here
    insert(index, val) {
        let i = 0;
        let curr = this.head;
        while(i < index - 1){
            curr = curr.next;
            if(!curr) return false;
            i++;
        }
        if(i === this.length - 1) return false;
        const temp = curr.next;
        const node = new Node(val);
        curr.next = node;
        node.next = temp;
        this.length++;
        return true;
    }

    // TODO: Implement the remove method here
    remove(index) {
        let i = 0;
        let curr = this.head;
        while(i < index - 1){
            curr = curr.next;
            if(!curr) return undefined;
            i++;
        }
        const ret = curr.next;
        curr.next = curr.next.next;
        this.length--;
        return ret;
    }

    // TODO: Implement the size method here
    size() {
        return this.length;
    }
}

exports.Node = Node;
exports.LinkedList = LinkedList;
