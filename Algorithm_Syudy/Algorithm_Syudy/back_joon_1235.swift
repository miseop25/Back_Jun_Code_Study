//
//  back_joon_1235.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2022/05/11.
//

import Foundation


class StudentNum {
    let N:Int
    let maxLen:Int
    var studentArr : Array<String> = []
    
    
    init(num : Int) {
        N = num
        for _ in 0..<N {
            if let word = readLine() {
                studentArr.append(word)
            }
        }
        maxLen = studentArr.first!.count
    }
    
    func checkStudentId(idLen : Int) -> Bool{
        if maxLen <= idLen {
            return false
        }
        var checkIdArr = Set<String>()
        for person in studentArr {
            let arCnt = checkIdArr.count
            let index = person.index(person.startIndex, offsetBy: maxLen - idLen)
            let newId = String(person[index...])
            checkIdArr.insert(newId)
            if arCnt == checkIdArr.count {
                return false
            }
        }
        if N != checkIdArr.count {
            return false
        } else {
            return true
        }
    }
    
    func getAnswer() -> Int {
        for i in stride(from: maxLen-1, to: 0, by: -1) {
            if !checkStudentId(idLen: i) {
                return i + 1
            }
        }
        return maxLen
    }
    
}


//let n = Int(readLine()!)
//let stId = StudentNum(num: n!)
//print(stId.getAnswer())
