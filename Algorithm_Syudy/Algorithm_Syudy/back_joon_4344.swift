//
//  back_joon_4344.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2022/04/20.
//

import Foundation

class OverAverage {
    var n : Int = 0
    
    init(N: Int) {
        n = N
    }
    
    func inputParm() -> [Int] {
        var arr :[Int] = []
        if let word = readLine() {
            arr = word.components(separatedBy: " ").map({ (value) in Int(value)! })
        }
        return arr
    }
    
    func getCase() -> Double{
        let strArr = inputParm()
        let len = strArr[0]
        var sum = 0
        for i in 1...len {
            sum += strArr[i]
        }
        let average = Double(Double(sum) / Double(len))
        var overAvr = 0
        for i in 1...len {
            if Double(strArr[i]) > average {
                overAvr += 1
            }
        }
        
        return Double(Double(overAvr) / Double(len) * 100.0)
    }
    
    func makeAnswer() {
        for _ in 0..<n {
            let answer = getCase()
            var str = String(format: "%.3f", answer)
            str += "%"
            print(str)
        }
    }
}


//let n = Int(readLine()!)
//let over = OverAverage(N: n!)
//over.makeAnswer()
