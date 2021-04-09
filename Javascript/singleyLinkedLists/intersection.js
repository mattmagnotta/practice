while (curA != null) {
  map.set(curA, 1)
  curA = curA.next
}
while (curB != null) {

  if (map.has(curB)) {
    return curB
  } else {
    curB = curB.next
  }
}
return null