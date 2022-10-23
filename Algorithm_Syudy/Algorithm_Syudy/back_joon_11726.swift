//
//  back_joon_11726.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2022/04/14.
//

import Foundation


class Tile2N {
    var n = 0
    var dp : [Int64] =  [1, 2]
    var answer : Int64 = 0
    
    func inputParm() {
        let input = readLine()!
        n = Int(input)!
    }
    
    func makeAnswer() {
        if n < 3 {
            answer = Int64(dp[n-1])
            return
        }
        
        for i in 2..<n {
            dp.append( Int64(  (dp[i-2] + dp[i-1])%10007) )
        }
        answer = Int64(dp.last!%10007)
    }
    
    func printAnswer() {
        print(answer)
    }
    
}


//let t = Tile2N()
//t.inputParm()
//t.makeAnswer()
//t.printAnswer()
