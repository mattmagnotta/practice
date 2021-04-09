var hasCycle = function(head) {
  let slow = head,
    fast = head
  while (slow !== null && fast !== null) {
    slow = slow.next
    fast = fast.next.next
    if (slow === fast) {
      return true
    }
  }
  return false
};




function hasCycle(head) {

  let slow = head,
    fast = header
  while (slow !== null && fast.next !== null) {
    slow = slow.next
    fast = fast.next.next
    if (slow == fast) {
      return true
    }
  }
  return false

}