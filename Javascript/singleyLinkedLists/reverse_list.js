var reverseList = function(head) {
  let prev = null,
    current = head,
    next = null
  while (current) {
    next = current.next
    current.next = prev
    prev = current
    current = next
  }
  return prev
}