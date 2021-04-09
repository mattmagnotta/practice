function mergeTwolists(l1, l2) {
  if (l1 == null) return l1
  if (l2 == null) return l2

  if (l1.value < l2.val) {
    l1.next = mergeTwolists(l1.next, l2)
    return l1
  }
}