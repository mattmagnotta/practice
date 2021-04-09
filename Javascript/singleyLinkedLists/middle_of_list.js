var middleNode = function(head) {
  let slow = head,
    fast = head
  while (slow !== null && fast.next !== null) {
    slow = slow.next
    fast = fast.next.next
    console.log(slow, fast)
  }
  return slow
}