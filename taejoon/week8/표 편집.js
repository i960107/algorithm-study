function solution(n, k, cmd) {
  let answer = '';
  let stack = [];
  let list = new DLL();
  for (let i = 0; i < n; i++) {
    list.add(i);
  }
  let curr = list.head;
  for (let i = 0; i < k; i++) {
    curr = curr.next;
  }

  for (let i = 0; i < cmd.length; i++) {
    let [command, num] = cmd[i].split(' ');
    if (command === 'U') {
      for (let i = 0; i < num; i++) {
        curr = curr.prev;
      }
    } else if (command === 'D') {
      for (let i = 0; i < num; i++) {
        curr = curr.next;
      }
    } else if (command === 'C') {
      stack.push(curr);
      if (curr.prev) {
        curr.prev.next = curr.next;
      }
      if (curr.next) {
        curr.next.prev = curr.prev;
      }
      curr = curr.next ? curr.next : curr.prev;
    } else if (command === 'Z') {
      let node = stack.pop();
      if (node.prev) {
        node.prev.next = node;
      }
      if (node.next) {
        node.next.prev = node;
      }
    }
  }

  let set = new Set();
  for (let i = 0; i < stack.length; i++) {
    set.add(stack[i].value);
  }
  for (let i = 0; i < n; i++) {
    if (set.has(i)) answer += 'X';
    else answer += 'O';
  }

  return answer;
}

class Node {
  constructor(value) {
    this.value = value;
    this.prev = null;
    this.next = null;
  }
}

class DLL {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  add(value) {
    let node = new Node(value);
    if (!this.head) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      node.prev = this.tail;
      this.tail = node;
    }
  }
}
