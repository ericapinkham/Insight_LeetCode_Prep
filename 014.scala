import scala.annotation.tailrec

def longestCommonPrefix(words: List[String]): String = {
  def compareWords(left: String, right: String): String = {
    @tailrec
    def acc(pre: String, left: String, right: String): String = {
      (left.length, right.length) match {
        case (x, y) if x > 0 && y > 0 && left.charAt(0) == right.charAt(0) => acc(pre + left.charAt(0), left.substring(1), right.substring(1))
        case (_, _) => pre
      }
    }
    acc("", left, right)
  }
  words match {
    case Nil => ""
    case _ => words.tail.foldLeft(words.head)(compareWords)
  }
}
