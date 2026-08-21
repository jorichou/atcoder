fun main() {
  val a = readLine() ?: ""
  val b = readLine() ?: ""
  
  val aScores = a.split(" ").map {it.toInt()}
  val bScores = b.split(" ").map {it.toInt()}
  
  val aTotal = aScores.sum()
  val bTotal = bScores.sum()
  
  println(aTotal - bTotal + 1)
}